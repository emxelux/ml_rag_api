from fastapi import FastAPI
from schema import Prompt_send
from engine import ask, search

app = FastAPI(tags=['CHAT'])


@app.get('/')
def homepage():
    return "This is ML Q&A Home page"


@app.post('/search')
def chat(query: Prompt_send):
    return ask(query.question)