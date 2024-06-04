from fastapi import FastAPI, HTTPException

from engines import DDGS, BING, GITHUB, VT
from typing import Optional
import os

app = FastAPI()


@app.get("/search/bing/")
async def search_bing(q: str, l: Optional[str] = 'cn-zh', m: Optional[int] = 10):
    proxy_url = os.getenv('PROXY_URL', None)  # 默认值是你原来硬编码的代理路径
    try:
        with BING(proxies=proxy_url) as bing:
            res = bing.text(keywords=q)
            return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search/ddgs/")
async def search_ddgs(q: str, l: Optional[str] = 'cn-zh', m: Optional[int] = 10):
    proxy_url = os.getenv('PROXY_URL', None)  # 默认值是你原来硬编码的代理路径
    try:
        with DDGS(proxies=proxy_url,
                    timeout=20) as ddgs:
            res = ddgs.text(q, max_results=m , region=l,)
            return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search/github/")
async def search_github(q: str, l: Optional[str] = 'cn-zh', m: Optional[int] = 10):
    proxy_url = os.getenv('PROXY_URL', None)  # 默认值是你原来硬编码的代理路径
    try:
        with GITHUB(proxies=proxy_url,
                    timeout=20) as github:
            res = github.text(keywords=q,)
            return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search/vt/")
async def search_vt(q: str):
    proxy_url = os.getenv('PROXY_URL', None)  # 默认值是你原来硬编码的代理路径
    try:
        with VT(proxies=proxy_url, timeout=30) as vt:
            res = vt.api(q)
            return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))