from framework.game_framework import Goal

goals = [
    Goal(
        priority=1,
        name="Gather Article Information",
        description=(
            "Fetch the provided sports article, extract its readable content, "
            "and analyze it in order to understand Newell's current situation "
            "ahead of the next match."
        )
    ),
    Goal(
        priority=2,
        name="Produce Final Structured Analysis",
        description=(
            "Generate a structured pre-match analysis and call terminate "
            "with the full final report."
        )
    )
]
