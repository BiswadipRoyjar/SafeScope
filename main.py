from fastapi import FastAPI, Form, Request, BackgroundTasks
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import uuid
import json
import os
import time

from .crawler import crawl_site
from .analyzer import analyze_pages
from .report import generate_pdf

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

SCAN_JOBS = {}


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/start_scan", response_class=HTMLResponse)
def start_scan(request: Request, background_tasks: BackgroundTasks, url: str = Form(...)):
    scan_id = str(uuid.uuid4())

    SCAN_JOBS[scan_id] = {
        "status": "running",
        "progress": 0,
        "current_url": "",
        "pages_scanned": 0,
        "total_pages": 30,
        "result": None,
        "pdf_path": None
    }

    background_tasks.add_task(run_scan_process, url, scan_id)

    return templates.TemplateResponse("status.html", {
        "request": request,
        "scan_id": scan_id,
        "url": url
    })


def run_scan_process(url, scan_id):
    job = SCAN_JOBS[scan_id]

    pages = []
    total = job["total_pages"]
    start_time = time.time()

    # --- Modified crawler with live status updates ---
    for page_data, progress, current_url in crawl_site(url, total):
        pages.append(page_data)

        job["progress"] = progress
        job["current_url"] = current_url
        job["pages_scanned"] = len(pages)

    findings = analyze_pages(pages)

    pdf_path = generate_pdf(url, pages, findings, scan_id)

    job["status"] = "completed"
    job["result"] = {"url": url, "pages": pages, "findings": findings}
    job["pdf_path"] = pdf_path


@app.get("/scan_status/{scan_id}")
def scan_status(scan_id: str):
    job = SCAN_JOBS.get(scan_id)
    if not job:
        return {"error": "Invalid scan id"}

    return job


@app.get("/scan_result/{scan_id}", response_class=HTMLResponse)
def scan_result(request: Request, scan_id: str):
    job = SCAN_JOBS.get(scan_id)
    if not job:
        return HTMLResponse("Scan ID not found", status_code=404)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "scan_id": scan_id,
        "result": job["result"],
        "pdf_path": job["pdf_path"]
    })


@app.get("/download_pdf/{scan_id}")
def download_pdf(scan_id: str):
    job = SCAN_JOBS.get(scan_id)
    if not job or not job["pdf_path"]:
        return {"error": "PDF not ready"}

    return FileResponse(job["pdf_path"], filename=f"scan_{scan_id}.pdf")
