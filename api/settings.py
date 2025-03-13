import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

CONFIG_PATH = Path(__file__).parent.parent / "config" / "prompt_styles.json"

class PromptStyle(BaseModel):
    name: str
    description: str
    template: str

@app.get("/api/prompt-styles")
async def get_prompt_styles():
    try:
        with open(CONFIG_PATH) as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="設定ファイルが見つかりません")

@app.post("/api/prompt-styles")
async def update_prompt_styles(styles: dict):
    try:
        with open(CONFIG_PATH, "w") as f:
            json.dump(styles, f, indent=2, ensure_ascii=False)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
