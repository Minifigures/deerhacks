"""
Shared state definition for the LangGraph workflow.
"""

from typing import TypedDict, List, Optional, Any


class PathfinderState(TypedDict, total=False):
    """Shared state passed between all LangGraph nodes."""

    # ── Commander outputs ──
    raw_prompt: str
    parsed_intent: dict
    complexity_tier: str          # "quick" | "full" | "adversarial"
    agent_weights: dict           # e.g. {"vibe": 0.3, "cost": 0.5, ...}

    # ── Scout outputs ──
    candidate_venues: List[dict]

    # ── Vibe Matcher outputs ──
    vibe_scores: dict             # venue_id → score

    # ── Access Analyst outputs ──
    accessibility_scores: dict    # venue_id → score
    isochrones: dict              # venue_id → GeoJSON

    # ── Cost Analyst outputs ──
    cost_profiles: dict           # venue_id → cost breakdown

    # ── Critic outputs ──
    risk_flags: dict              # venue_id → [risk strings]
    veto: bool                    # True if the Critic forced a retry
    veto_reason: Optional[str]

    # ── Final ranked output ──
    ranked_results: List[dict]

    # ── Snowflake context ──
    snowflake_context: Any
