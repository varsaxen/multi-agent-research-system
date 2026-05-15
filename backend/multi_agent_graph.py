from langgraph.graph import StateGraph, END
from models import AgentState
from tools import web_search


# -----------------------------
# ✅ SUPERVISOR (Brain)
# -----------------------------
def supervisor(state: AgentState):
    print("\n[SUPERVISOR] deciding...")

    if not state["sub_questions"]:
        print("→ Decomposer")
        return {"next_agent": "decomposer"}

    elif state["sub_questions"] and not state["evidence"]:
        print("→ Researcher")
        return {"next_agent": "research"}

    # ✅ HITL checkpoint
    elif state["evidence"] and not state.get("review_required"):
        print("→ Human Review ⏸")
        return {"next_agent": "review"}

    elif state.get("review_required") and not state["synthesis"]:
        print("→ Synthesizer")
        return {"next_agent": "synthesizer"}

    else:
        print("→ Finish ✅")
        return {"next_agent": "finish"}


# -----------------------------
# ✅ DECOMPOSER
# -----------------------------
def decomposer(state: AgentState):
    print("[DECOMPOSER] breaking query")

    q = state["query"]

    sub_questions = [
        f"What is {q}?",
        f"Benefits of {q}?",
        f"Challenges of {q}?"
    ]

    return {"sub_questions": sub_questions}


# -----------------------------
# ✅ RESEARCHER (Simulated Parallel)
# -----------------------------
def researcher(state: AgentState):
    print("[RESEARCHER] running tasks...")

    evidence = []

    for q in state["sub_questions"]:
        print(f"[TASK] {q}")

        results = web_search.invoke({"query": q})

        for r in results:
            if r not in evidence:
                evidence.append(r)

    return {"evidence": evidence}


# -----------------------------
# ✅ REVIEW NODE (HITL Pause)
# -----------------------------
def review_node(state: AgentState):
    print("[HITL] Waiting for user approval...")

    # ✅ mark review required (pause point)
    return {"review_required": True}


# -----------------------------
# ✅ SYNTHESIZER
# -----------------------------
def synthesizer(state: AgentState):
    print("[SYNTHESIZER] creating summary")

    summary = "Summary: "

    sources = []

    for item in state["evidence"]:
        if "content" in item:
            summary += item["content"] + " "
        if "url" in item:
            sources.append(item["url"])

    return {
        "synthesis": summary,
        "sources": list(set(sources)),
        "confidence": round(0.7 + 0.2, 2)   # simple mock confidence
    }
# -----------------------------
# ✅ ROUTER
# -----------------------------
def route(state: AgentState):
    return state["next_agent"]


# -----------------------------
# ✅ BUILD GRAPH
# -----------------------------
builder = StateGraph(AgentState)

builder.add_node("supervisor", supervisor)
builder.add_node("decomposer", decomposer)
builder.add_node("research", researcher)
builder.add_node("review", review_node)
builder.add_node("synthesizer", synthesizer)

builder.set_entry_point("supervisor")

# ✅ Supervisor routing logic
builder.add_conditional_edges(
    "supervisor",
    route,
    {
        "decomposer": "decomposer",
        "research": "research",
        "review": "review",
        "synthesizer": "synthesizer",
        "finish": END
    }
)

# ✅ Flow edges
builder.add_edge("decomposer", "supervisor")
builder.add_edge("research", "supervisor")

# ✅ HITL pause
builder.add_edge("review", END)

# ✅ Resume flow (from API)
builder.add_edge("synthesizer", "supervisor")

# ✅ FINAL GRAPH
graph = builder.compile()