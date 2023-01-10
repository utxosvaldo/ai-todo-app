from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    advice: str = ""
    done: bool

tasks = []

@app.get("/tasks/")
async def read_tasks():
    return tasks

@app.post("/tasks/")
async def create_task(task: Task):
    prompt = f"Write a consice and actionable three step plan to achieve the task titled '{task.title}' and description '{task.description}'",
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    task.advice = response.choices[0]["text"]
    tasks.append(task)
    return {"id": len(tasks), "advice": response}

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    tasks[task_id - 1] = task
    return {"success": True}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    tasks.pop(task_id - 1)
    return {"success": True}
