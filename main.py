from fastapi import FastAPI
from schema import Prompt_send
from engine import ask, search
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(tags=['CHAT'])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      
    allow_credentials=True,
    allow_methods=["*"],     
    allow_headers=["*"],    




@app.get('/')
def homepage():
    return "This is ML Q&A Home page"


@app.post('/search')
def chat(query: Prompt_send):
    return ask(query.question)