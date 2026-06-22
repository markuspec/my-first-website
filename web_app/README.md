# Playbook Youth Sports

A starter Flask web app for young athletes:

- `index.html` landing page with athlete stories and app overview
- `workouts.html` workouts, mobility guides, and video demonstrations
- `plan.html` AI-style plan builder for personalized training schedules
- `booking.html` therapist booking placeholder
- `static/css/styles.css` styling for the site
- `app.py` Flask backend and routing logic

## Run locally

1. Create a Python environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000` in your browser.

## Notes

- The booking page is currently a placeholder for future pro scheduling.
- The AI plan builder returns a simple structured plan in the browser.
- You can add more sports-specific videos and therapist booking features next.
