from framework.game_framework import Goal

goals = [
    Goal(
        priority=1,
        name="Gather Opponent Statistics",
        description=(
            "Use fetch_sofascore_stats with the opponent's team_id to retrieve "
            "their current season statistics from Sofascore."
        )
    ),
    Goal(
        priority=2,
        name="Gather Article Information",
        description=(
            "Fetch the provided sports article and extract its readable content."
        )
    ),
    Goal(
        priority=3,
        name="Produce Final Structured Analysis",
        description=(
            "Combine the Sofascore statistics and the article content to generate "
            "a structured pre-match analysis and call terminate with the full report."
        )
    )
]
