# src/stewr/cli.py
import sys
from rich import print
from stewr.planners.reactflaskplanner import generate_react_flask_plan
from stewr.executor import run_plan  # <- use run_plan now

HELP_TEXT = """stewr — your project scaffold assistant

Usage:
  stewr "your project description"

Example:
  stewr "setup flask backend and react frontend"
"""

def main():
    if len(sys.argv) == 1 or sys.argv[1] in ("--help", "-h"):
        print(HELP_TEXT)
        return

    text = " ".join(sys.argv[1:])
    print("[bold green]Stewr is stewing your project...[/bold green]\n")

    plan = generate_react_flask_plan(text)
    steps = plan.get("steps", [])

    if not steps:
        print("[yellow]No steps found for your description. Try another command.[/yellow]")
        return

    # Call the executor function that handles looping + animation
    run_plan(plan)

    print("[bold green]All done! Your project is ready to cook![/bold green]")
