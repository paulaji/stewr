# stewr/planner.py
def generate_plan(text: str) -> dict:
    """
    Dummy planner: returns a static JSON plan based on keywords in the text.
    """
    text = text.lower()
    steps = []

    # Check for Python/Flask
    if "flask" in text:
        steps.append({
            "title": "Create virtual environment",
            "explanation": "Isolate Python dependencies",
            "command": "python -m venv venv"
        })
        steps.append({
            "title": "Install Flask",
            "explanation": "Backend framework",
            "command": "venv\\Scripts\\pip install flask"  # Windows path
        })

    # Check for React
    if "react" in text:
        steps.append({
            "title": "Create React app",
            "explanation": "Frontend scaffold",
            "command": "npx create-react-app frontend"
        })

    # Check for Express
    if "express" in text:
        steps.append({
            "title": "Setup Express backend",
            "explanation": "Node.js backend scaffold",
            "command": "npm init -y && npm install express"
        })

    return {"steps": steps}