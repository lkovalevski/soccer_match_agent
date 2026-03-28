import os
from agent.agent_setup import create_agent
from config import OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
from framework.game_framework import tools  # o como se llame


ARTICLE_URL = "https://elciudadanoweb.com/con-acassuso-en-la-mira-newells-trabaja-con-todos-sus-canones-apuntando-al-partido-de-copa-argentina/"

##"https://www.rosario3.com/deportes/en-newells-casi-todo-vuelve-a-estar-bajo-la-lupa-por-un-arranque-a-los-tumbos-20260209-0039.html"

if __name__ == "__main__":

    agent = create_agent()

    user_task = f"""
Analyze the following article about Newell's Old Boys and produce
a structured pre-match report.

URL: {ARTICLE_URL}
"""
    
    agent = create_agent()
    
    memory = agent.run(user_task, max_iterations=5)

    print("\n" + "=" * 60)
    print("FINAL REPORT")
    print("=" * 60)

    final_output = "No final report found."

    for mem in reversed(memory.get_memories()):
        if mem.get("type") == "assistant":
            try:
                import json
                content = json.loads(mem["content"])
                if content.get("tool") == "terminate":
                    final_output = content["args"]["message"]
                    break
            except:
                continue

    print(final_output)
