from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()

app = FastAPI()

class UserInput(BaseModel):
    Intent: str
    Text: str
    Style: str or "unchanged"

from model import invoke_model

@app.post("/rewrite")
def rewrite(user_input: UserInput):
    response = invoke_model(user_input.Intent, user_input.Text, user_input.Style)
    return {"rewritten_text": response}
