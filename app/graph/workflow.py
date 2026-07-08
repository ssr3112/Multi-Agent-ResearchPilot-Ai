from langgraph.graph import (
    StateGraph,
    END
)

from app.graph.state import (
    ResearchState
)

from app.agents.researcher import (
    researcher_agent
)

from app.agents.extractor import (
    extractor_agent
)

from app.agents.fact_checker import (
    fact_checker_agent
)

from app.agents.writer import (
    writer_agent
)


workflow = StateGraph(
    ResearchState
)

workflow.add_node(
    "researcher",
    researcher_agent
)

workflow.add_node(
    "extractor",
    extractor_agent
)

workflow.add_node(
    "fact_checker",
    fact_checker_agent
)

workflow.add_node(
    "writer",
    writer_agent
)

workflow.set_entry_point(
    "researcher"
)

workflow.add_edge(
    "researcher",
    "extractor"
)

workflow.add_edge(
    "extractor",
    "fact_checker"
)

workflow.add_edge(
    "fact_checker",
    "writer"
)

workflow.add_edge(
    "writer",
    END
)

research_graph = workflow.compile()