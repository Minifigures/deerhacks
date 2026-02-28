"""
Node 2 — The SCOUT (Discovery)
Discovers candidate venues via Google Places API & Yelp Fusion,
then enriches them with Snowflake intelligence.
"""

from app.models.state import PathfinderState


def scout_node(state: PathfinderState) -> PathfinderState:
    """
    Discover 5-10 candidate venues.

    Steps
    -----
    1. Query Google Places API with parsed intent filters.
    2. Query Yelp Fusion for supplementary data.
    3. Merge & deduplicate results.
    4. Enrich via Snowflake (noise complaints, seasonal closures).
    5. Return updated state with candidate_venues.
    """
    # TODO: implement API calls + Snowflake enrichment
    return state
