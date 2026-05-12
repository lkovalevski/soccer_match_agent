import os
from agent.agent_setup import create_agent
from config import OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
from framework.game_framework import tools  # o como se llame


ARTICLE_URL      = "https://www.conclusion.com.ar/deportes/newells-enfrenta-a-velez-en-su-ultima-funcion-del-apertura/05/2026/"#"https://www.cadena3.com/noticia/instituto/instituto-cayo-1-0-ante-estudiantes-y-complico-su-chances-de-meterse-en-playoffs_542605"
OPPONENT_TEAM_ID = "4937"  # Instituto Córdoba team_id in Sofascore

## "https://www.sofascore.com/es-la/football/team/acassuso/112491#tab:statistics"
## "https://elciudadanoweb.com/con-acassuso-en-la-mira-newells-trabaja-con-todos-sus-canones-apuntando-al-partido-de-copa-argentina/"
## "https://www.rosario3.com/deportes/en-newells-casi-todo-vuelve-a-estar-bajo-la-lupa-por-un-arranque-a-los-tumbos-20260209-0039.html"

if __name__ == "__main__":

    agent = create_agent()
    
    user_task = f"""
    Analyze the upcoming Newell's Old Boys match, focusing on the opponent.
    Opponent team_id for Sofascore: {OPPONENT_TEAM_ID}
    Article URL: {ARTICLE_URL}

    Steps:
    1. Fetch opponent statistics from Sofascore using fetch_sofascore_stats
    2. Fetch and extract the opponent article content
    3. Combine both sources into a structured pre-match report (in Spanish)
    4. Call terminate with the final analysis
    """ 

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
