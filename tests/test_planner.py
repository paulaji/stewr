# tests/test_planner.py
from stewr.planner import generate_plan

def test_flask_plan():
    """Planner should generate Flask steps"""
    plan = generate_plan("setup flask backend")
    steps = plan.get("steps", [])
    assert len(steps) >= 2
    assert steps[0]["title"] == "Create virtual environment"
    assert steps[1]["title"] == "Install Flask"

def test_react_plan():
    """Planner should generate React steps"""
    plan = generate_plan("setup react frontend")
    steps = plan.get("steps", [])
    titles = [step["title"] for step in steps]
    assert "Create React app" in titles

def test_express_plan():
    """Planner should generate Express steps"""
    plan = generate_plan("setup express backend")
    steps = plan.get("steps", [])
    titles = [step["title"] for step in steps]
    assert "Setup Express backend" in titles

def test_combined_plan():
    """Planner should combine multiple stacks"""
    plan = generate_plan("setup flask backend and react frontend")
    steps = plan.get("steps", [])
    titles = [step["title"] for step in steps]
    assert "Install Flask" in titles
    assert "Create React app" in titles
