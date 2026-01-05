# src/stewr/executor.py
import os
import subprocess
import time
from rich import print

ALLOWED_COMMANDS = ["pip", "python", "npm", "npx", "mkdir", "cd"]

def run_plan(plan):
    """
    Loops through all steps in the plan and executes them
    with confirmation and simple animation.
    """
    steps = plan.get("steps", [])
    for step in steps:
        print(f"\nStep: {step['title']}")
        print(f"  {step['explanation']}")

        cook = input("Cook this step? (y/n) ").lower()
        if cook != 'y':
            print("[yellow]Skipped.[/yellow]")
            continue

        # Animation: simple dot loader
        print("Stewr is stewing your project", end="", flush=True)
        for _ in range(3):
            print(" .", end="", flush=True)
            time.sleep(0.5)

        # If the step is file creation
        if "file_name" in step and "file_content" in step:
            file_path = step["file_name"]
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            content = step["file_content"].strip()  # remove leading indentation
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("[green]Stewing completed![/green]")
            continue

        # Otherwise, run shell command
        cmd = step.get("command", "")
        if not cmd.split()[0] in ALLOWED_COMMANDS:
            print("[red]Unsafe command detected! Skipping.[/red]")
            continue

        try:
            subprocess.run(cmd, shell=True, check=True)
            print("[green]Stewing completed![/green]")
        except subprocess.CalledProcessError:
            print("[red]Command failed![/red]")