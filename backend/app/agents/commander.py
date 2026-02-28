"""
Node 1 — The COMMANDER (Orchestrator)
Central brain: intent parsing, complexity tiering, dynamic agent weighting.
Model: Gemini 1.5 Flash
"""

from app.models.state import PathfinderState


def commander_node(state: PathfinderState) -> PathfinderState:
    """
    Parse the raw user prompt into a structured execution plan.

    Steps
    -----
    1. Call Gemini 1.5 Flash to classify intent & extract parameters.
    2. Determine complexity tier (quick / full / adversarial).
    3. Compute dynamic agent weights based on keywords.
    4. Query Snowflake for historical risk pre-check.
    5. Return updated state with parsed_intent, complexity_tier, agent_weights.
    """
    # TODO: implement Gemini call + Snowflake pre-check
    return state
