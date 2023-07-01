from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
import logging

app = FastAPI()




conn = MongoClient("mongodb+srv://binaybasnetoct13:Aqbfjotld-oct13@cluster0.cwsbqti.mongodb.net/")    

