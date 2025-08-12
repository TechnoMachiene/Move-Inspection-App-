
Project Report: Move Inspection
Overview
This project is a web-based Move-in/Move-out Inspection Automator. It allows users to upload "move-in" and "move-out" images of a property, sends them to a FastAPI backend for analysis, and displays an inspection report with detected damages and estimated costs. The backend can forward images to an n8n workflow for further processing.

Folder Structure
Main Components
1. Frontend (index.html)
Features:
Responsive UI for uploading move-in and move-out images.
Displays a formatted inspection report with damages and estimated costs.
Uses JavaScript to handle file uploads, API requests, and report rendering.
Key Elements:
File input fields for two images.
"Analyze Images" button triggers the analysis.
Inspection report area displays results in a table.
API Integration:
Sends a POST request to /analyze endpoint on the backend with both images as multipart/form-data.
Handles and displays the backend's JSON response.
2. Backend (forwarder.py)
Framework: FastAPI
Endpoints:
/ : Redirects to API docs.
/analyze : Accepts two image files, forwards them to an n8n webhook (as multipart or JSON), and returns the response.
Configurable:
n8n webhook URL and forwarding mode (multipart or JSON) are configurable via environment variables.
Error Handling:
Returns HTTP 400 on file read errors or unknown forwarding modes.
How It Works
User uploads images via the web interface.
Frontend sends images to the FastAPI backend.
Backend forwards images to the configured n8n webhook for analysis.
n8n processes images (e.g., using AI or image comparison) and returns a JSON report.
Frontend displays the report in a user-friendly table, including a summary and total estimated cost.
How to Run
Install dependencies:
Start the backend:
Open index.html in your browser (double-click or use Live Server in VS Code).
Upload images and analyze.
Customization
n8n Webhook: Set the N8N_WEBHOOK_URL environment variable to point to your n8n instance.
Forwarding Mode: Set FORWARD_MODE to multipart or json as needed.
Notes
The project is designed for local testing and demo purposes. For production, restrict CORS and secure the backend.
Some features (like PDF download) are present in code but commented out.
Summary
This project streamlines property inspection reporting by combining a modern web UI, a FastAPI backend, and n8n workflow automation. It is modular, easy to run locally, and ready for further extension or integration.
