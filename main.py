#!/usr/bin/env python3
"""
LogAPI Service - システムログ監視サービス
Port 8005で動作
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import subprocess
import json
from typing import Dict, Any
import logging

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="LogAPI Service", version="1.0.0")

# 静的ファイルとテンプレート
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# サービス定義
SERVICES = {
    "aichat": "aichat",
    "crm-mcp": "crm-mcp", 
    "productmaster-mcp": "productmaster-mcp",
    "database-mgmt": "database-mgmt"
}

@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    """LogAPI メイン画面を表示"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/logs/{service}")
async def get_service_logs(service: str) -> Dict[str, Any]:
    """指定されたサービスのログを取得"""
    
    if service not in SERVICES:
        raise HTTPException(status_code=404, detail=f"Service {service} not found")
    
    service_name = SERVICES[service]
    
    try:
        # journalctlでログを取得
        cmd = ["journalctl", "-u", service_name, "--no-pager", "-n", "200"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            return {
                "success": True,
                "logs": result.stdout,
                "service": service_name
            }
        else:
            return {
                "success": False,
                "error": f"Failed to get logs: {result.stderr}",
                "service": service_name
            }
            
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Timeout while fetching logs",
            "service": service_name
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "service": service_name
        }

@app.get("/health")
async def health_check():
    """ヘルスチェック"""
    return {"status": "healthy", "service": "LogAPI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
