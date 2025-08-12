# Move-in/Move-out Inspection Automator

A web application to automate property move-in/move-out inspections. Upload before and after images, analyze them via a FastAPI backend (with n8n workflow integration), and receive a detailed report of detected damages and estimated costs.

---

## Features

- Upload move-in and move-out images via a simple web interface
- FastAPI backend forwards images to an n8n webhook for analysis
- Displays a structured, user-friendly report of damages and estimated costs
- Modern, responsive UI

---

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/KeenSight-AI-Demo-Apps/Move-Inspection-App-.git
cd Move-Inspection-App-
```

### 2. Install Backend Dependencies

```sh
pip install fastapi uvicorn httpx
```

### 3. Run the Backend

```sh
uvicorn forwarder:app --reload
```

- The backend will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 4. Open the Frontend

- Open `index.html` in your browser (double-click or use Live Server in VS Code).

---

## Configuration

- **n8n Webhook URL:**  
  Set the `N8N_WEBHOOK_URL` environment variable to your n8n webhook endpoint.  
  Default: `http://localhost:5678/webhook/inspection`

- **Forwarding Mode:**  
  Set `FORWARD_MODE` to `multipart` or `json` (default: `multipart`).

---

## Usage

1. Upload both move-in and move-out images.
2. Click **Analyze Images**.
3. View the inspection report with damages and estimated costs.

---

## Project Structure

```
Move-Inspection-App-/
│
├── forwarder.py      # FastAPI backend
├── index.html        # Frontend web page
└── README.md         # Project documentation
```

---

## License

---

## Credits

- [FastAPI](https://fastapi.tiangolo.com/)
- [n8n](https://n8n.io/)
- [jsPDF](https://github.com/parallax/jsPDF) (optional, for PDF
