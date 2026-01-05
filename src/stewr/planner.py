from typing import List, Dict

SUPPORTED_STACKS = {
    "flask": ["flask", "python flask"],
    "react": ["react", "reactjs", "react js"],
    "express": ["express", "expressjs", "node express"],
}

def detect_stacks(user_input: str) -> List[str]:
    user_input = user_input.lower()
    detected = []

    for stack, keywords in SUPPORTED_STACKS.items():
        for kw in keywords:
            if kw in user_input:
                detected.append(stack)
                break

    return detected


def generate_plan(user_input: str) -> Dict:
    stacks = detect_stacks(user_input)

    steps = []

    if "flask" in stacks:
        steps.extend([
            {
                "title": "Create Python virtual environment",
                "explanation": "Create isolated Python environment",
                "command": "python -m venv venv"
            },
            {
                "title": "Install Flask",
                "explanation": "Install Flask web framework",
                "command": "venv\\Scripts\\pip install flask"
            }
        ])

    if "react" in stacks:
        steps.append({
            "title": "Create React app",
            "explanation": "Scaffold React frontend",
            "command": "npx create-react-app frontend"
        })

    if "express" in stacks:
        steps.append({
            "title": "Setup Express app",
            "explanation": "Initialize Express backend",
            "command": "npx express-generator backend"
        })

    return {
        "input": user_input,
        "stacks": stacks,
        "steps": steps
    }