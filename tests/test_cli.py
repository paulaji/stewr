# # tests/test_cli.py
# import sys
# from io import StringIO
# from stewr.cli import main

# def test_help_output():
#     """Test --help output"""
#     old_stdout = sys.stdout
#     sys.stdout = StringIO()
#     sys.argv = ["stewr", "--help"]
#     main()
#     output = sys.stdout.getvalue().lower()
#     sys.stdout = old_stdout
#     assert "stewr — plan your project" in output

# def test_planner_output():
#     """Test CLI prints planner steps"""
#     old_stdout = sys.stdout
#     sys.stdout = StringIO()
#     sys.argv = ["stewr", "setup flask backend"]
#     main()
#     output = sys.stdout.getvalue()
#     sys.stdout = old_stdout
#     assert "Create virtual environment" in output
#     assert "Install Flask" in output