from fastapi import FastAPI, Request ,APIRouter , Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.note import Note
from config.db import conn
from schema.note import noteEntity,notesEntity

import logging

# noteAPi app
note = APIRouter()


templates = Jinja2Templates(directory="templates")
# api to get the html page
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.Notes.Notes.find({})
    newDocs = []
    for doc in docs:
        if ("important" in doc):
            pass
        else:
            doc["important"] = True
        newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"],
            "important":doc["important"]
        })
    
    # logging dataof note to verify delete in production    
    for d in newDocs:
        print(d["title"])
        print("id -->",d["id"], "note--> ", d["desc"])
    
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@note.post("/")
async def create_item(request: Request,response_class=HTMLResponse):
    form = await request.form()
    print(dict(form)) 
    dict(form)["important"] = 1  if dict(form)["important"] =='on' else 0
    conn.Notes.Notes.insert_one(dict(form))
    return templates.TemplateResponse("success.html", {"request": request,"message": "success"})