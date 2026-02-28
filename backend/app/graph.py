"""
LangGraph workflow — assembles all agent nodes into the PATHFINDER graph.
"""

from langgraph.graph import StateGraph, END

from app.models.state import PathfinderState
from app.agents.commander import commander_node
from app.agents.scout import scout_node
from app.agents.vibe_matcher import vibe_matcher_node
from app.agents.access_analyst import access_analyst_node
from app.agents.cost_analyst import cost_analyst_node
from app.agents.critic import critic_node


def _should_retry(state: PathfinderState) -> str:
    """Conditional edge: retry if the Critic vetoed the plan."""
    if state.get("veto"):
        return "commander"
    return "end"


def build_graph() -> StateGraph:
    """Construct and compile the PATHFINDER LangGraph."""

    graph = StateGraph(PathfinderState)

    # ── Register nodes ──
    graph.add_node("commander", commander_node)
    graph.add_node("scout", scout_node)
    graph.add_node("vibe_matcher", vibe_matcher_node)
    graph.add_node("access_analyst", access_analyst_node)
    graph.add_node("cost_analyst", cost_analyst_node)
    graph.add_node("critic", critic_node)

    # ── Define edges ──
    graph.set_entry_point("commander")
    graph.add_edge("commander", "scout")
    graph.add_edge("scout", "vibe_matcher")
    graph.add_edge("scout", "access_analyst")
    graph.add_edge("scout", "cost_analyst")
    graph.add_edge("vibe_matcher", "critic")
    graph.add_edge("access_analyst", "critic")
    graph.add_edge("cost_analyst", "critic")

    # ── Conditional retry ──
    graph.add_conditional_edges("critic", _should_retry, {
        "commander": "commander",
        "end": END,
    })

    return graph.compile()


# Singleton compiled graph
pathfinder_graph = build_graph()
