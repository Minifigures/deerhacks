"""
Node 3 — The VIBE MATCHER (Qualitative Analysis)
Aesthetic reasoning engine using Gemini 1.5 Pro multimodal.
"""

from app.models.state import PathfinderState


def vibe_matcher_node(state: PathfinderState) -> PathfinderState:
    """
    Score each candidate venue on subjective vibe / aesthetic match.

    Steps
    -----
    1. Retrieve venue photos & review text from candidate_venues.
    2. Call Gemini 1.5 Pro with images + text for multimodal analysis.
    3. Classify vibe (minimalist, cyberpunk, cozy, dark-academia, …).
    4. Compute normalised Vibe Score per venue.
    5. Return updated state with vibe_scores.
    """
    # TODO: implement Gemini multimodal call
    return state
