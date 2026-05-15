from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
import asyncio

from multi_agent_graph import graph


# =========================
# ✅ Create FastAPI app
# =========================
app = FastAPI()


# =========================
# ✅ Enable CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# ✅ Request Models
# =========================
class QueryRequest(BaseModel):
    query: str


class ResumeRequest(BaseModel):
    query: str
    feedback: str


# =========================
# ✅ NORMAL API (Non-stream)
# =========================
@app.post("/research")
def research(request: QueryRequest):

    state = {
        "query": request.query,
        "sub_questions": [],
        "evidence": [],
        "synthesis": "",
        "next_agent": "",
        "review_required": False,
        "user_feedback": ""
    }

    result = graph.invoke(state)

    return {
        "sub_questions": result.get("sub_questions", []),
        "evidence": result.get("evidence", []),
        "synthesis": result.get("synthesis", "")
    }


# =========================
# ✅ SSE STREAM API
# =========================
@app.get("/research/stream")
async def research_stream(query: str):

    async def event_generator():

        # ✅ Step-by-step streaming
        yield "data: Supervisor: Starting research...\n\n"
        await asyncio.sleep(1)

        yield "data: Decomposer: Breaking query...\n\n"
        await asyncio.sleep(1)

        yield "data: Researcher: Gathering info...\n\n"
        await asyncio.sleep(1)

        # ✅ HITL trigger (very important)
        yield "data: Review required\n\n"

    return EventSourceResponse(event_generator())


# =========================
# ✅ RESUME API (HITL)
# =========================
@app.post("/research/resume")
def resume_research(request: ResumeRequest):

    state = {
        "query": request.query,
        "sub_questions": [],
        "evidence": [],
        "synthesis": "",
        "next_agent": "synthesizer",  # resume from synthesizer
        "review_required": True,
        "user_feedback": request.feedback
    }

    result = graph.invoke(state)

    return {
        "synthesis": result.get("synthesis", "")
    }