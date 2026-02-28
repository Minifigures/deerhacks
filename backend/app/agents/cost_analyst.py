"""
Node 5 — The COST ANALYST (Financial)
"No-surprises" auditor: scrapes true cost and compares to Snowflake history.
Tools: Firecrawl, Jina Reader
"""

from app.models.state import PathfinderState


def cost_analyst_node(state: PathfinderState) -> PathfinderState:
    """
    Compute Total Cost of Attendance (TCA) per venue.

    Steps
    -----
    1. Scrape venue websites via Firecrawl / Jina Reader.
    2. Extract hidden fees, equipment rentals, minimum spends.
    3. Query Snowflake Cortex for historical price baselines.
    4. Flag seasonal spikes or misleading discounts.
    5. Return updated state with cost_profiles.
    """
    # TODO: implement scraping + Snowflake comparison
    return state
