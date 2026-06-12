from fastapi import FastAPI
from fastapi.responses import (
    StreamingResponse,
    FileResponse
)

from app.agent import agent

app = FastAPI()


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/chat")
async def chat(
    query: str,
    session_id: str = "default"
):

    async def generate():

        try:

            config = {
                "configurable": {
                    "thread_id": session_id
                }
            }

            for chunk in agent.stream(
                {
                    "messages": [
                        ("user", query)
                    ]
                },
                config=config,
                stream_mode="messages"
            ):

                try:

                    message = chunk[0]

                    if hasattr(message, "content"):

                        content = message.content

                        if isinstance(content, str):

                            yield content

                except Exception:
                    pass

        except Exception as e:
            yield f"\nERROR: {str(e)}"

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )