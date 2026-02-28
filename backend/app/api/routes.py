"""
PATHFINDER API routes.
"""

from fastapi import APIRouter

from app.schemas import PlanRequest, PlanResponse

router = APIRouter()


@router.post("/plan", response_model=PlanResponse)
async def create_plan(request: PlanRequest):
    """
    Accept a natural-language activity request and return ranked venues.

    Flow: prompt → Commander → Scout → [Vibe, Access, Cost] → Critic → results
    """
    from app.graph import pathfinder_graph

    initial_state = {
        "raw_prompt": request.prompt,
        "parsed_intent": {},
        "complexity_tier": "full",
        "agent_weights": {},
        "candidate_venues": [],
        "vibe_scores": {},
        "accessibility_scores": {},
        "isochrones": {},
        "cost_profiles": {},
        "risk_flags": {},
        "veto": False,
        "veto_reason": None,
        "ranked_results": [],
        "snowflake_context": None,
    }

    # Run the full LangGraph workflow
    result = await pathfinder_graph.ainvoke(initial_state)

    return PlanResponse(
        venues=result.get("ranked_results", []),
        execution_summary="Pipeline complete.",
    )


@router.get("/health")
async def api_health():
    return {"status": "ok"}
