from fastapi import FastAPI`napp = FastAPI()`n@app.get("/")`ndef read_root():`n    return {"mensagem": "API do Mackenzie rodando no Docker com sucesso!"}
