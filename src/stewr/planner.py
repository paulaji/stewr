# # stewr/planner.py
# def generate_plan(command_text):
#     """
#     Returns a structured JSON plan for setting up Flask backend + React frontend.
#     Steps are ordered for proper scaffolding.
#     """
#     return {
#         "steps": [
#             {
#                 "title": "Create backend folder",
#                 "explanation": "Create a folder for Python backend code",
#                 "command": "mkdir backend"
#             },
#             {
#                 "title": "Create virtual environment",
#                 "explanation": "Isolate Python dependencies inside backend/venv",
#                 "command": "python -m venv backend/venv"
#             },
#             {
#                 "title": "Install Flask",
#                 "explanation": "Backend framework",
#                 "command": "python -m pip install --upgrade pip && python -m pip install flask"
#             },
#             {
#                 "title": "Create Flask scaffold",
#                 "explanation": "Create app.py inside backend folder",
#                 "file_name": "backend/app.py",
#                 "file_content": """from flask import Flask

#                 app = Flask(__name__)

#                 @app.route('/')
#                 def home():
#                     return 'Hello from Stewr!'
#                 """
#             },
#             {
#             "title": "Create React app",
#             "explanation": "Frontend scaffold using Vite (non-interactive)",
#             "command": "npx degit vitejs/vite/packages/create-vite/template-react frontend"
#         },
#         {
#             "title": "Install frontend dependencies",
#             "explanation": "Install React dependencies",
#             "command": "cd frontend && npm install"
#         }
#         ]
#     }