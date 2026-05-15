from typing import TypedDict, List, Dict



class AgentState(TypedDict):
    query: str
    sub_questions: List[str]
    evidence: List[Dict]
    synthesis: str
    next_agent: str

    review_required: bool
    user_feedback: str
