import sys
from stewr.planner import generate_plan
from rich import print

HELP_TEXT = """
stewr — plan your project from plain text
Usage: stewr "your project description"
Example: stewr "setup flask backend and react frontend"
"""

def main():
    # If no arguments or --help/-h, show help
    if len(sys.argv) == 1 or sys.argv[1] in ("--help", "-h"):
        print(HELP_TEXT)
        return

    # Combine all arguments into free text
    text = " ".join(sys.argv[1:])
    print("[bold green]stewr is stewing your project...[/bold green]\n")

    plan = generate_plan(text)
    steps = plan.get("steps", [])

    if not steps:
        print("[bold red]No plan could be generated for this description.[/bold red]")
        return

    for i, step in enumerate(steps, start=1):
        print(f"[bold]Step {i}: {step['title']}[/bold]")
        print(f"  {step['explanation']}")
        print(f"  Command: [dim]{step['command']}[/dim]\n")