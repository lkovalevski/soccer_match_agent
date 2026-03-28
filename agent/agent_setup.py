import agent.tools  # noqa: F401 — side effect import: registers tools via @register_tool
from framework.game_framework import (
    Agent,
    AgentFunctionCallingActionLanguage,
    PythonActionRegistry,
    Environment,
    generate_response
)
from agent.goals import goals

def create_agent():
    return Agent(
        goals=goals,
        agent_language=AgentFunctionCallingActionLanguage(),
        action_registry=PythonActionRegistry(
            tags=["news", "analysis", "system"]
        ),
        generate_response=generate_response, 
        environment=Environment()
    )