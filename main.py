from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import List
# from selenium import webdriver

app = FastAPI()
# driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
# driver.get("http://python.org")
# driver.close()

# Permitir el acceso desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    pass
