from datetime import datetime


def add_log(state, agent_name, status):

    if "logs" not in state:
        state["logs"] = []

    state["logs"].append(
        {
            "agent": agent_name,
            "status": status,
            "timestamp": str(datetime.now())
        }
    )

    return state