from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

SPORT_GOALS = {
    "strength": "strength building sessions, mobility warmups, and active recovery",
    "speed": "speed drills, agility training, and dynamic stretching",
    "endurance": "conditioning work, low-impact recovery, and mobility maintenance",
    "mobility": "mobility flow, stability drills, and restorative recovery",
}

WORKOUTS = [
    {
        "title": "Dynamic Warmup",
        "category": "Warmup",
        "description": "A guided routine to prepare joints and muscles for training.",
        "video": "https://www.youtube.com/embed/5P0uHCaAGeU",
    },
    {
        "title": "Hip Mobility Flow",
        "category": "Mobility",
        "description": "Improve hip range of motion with athlete-approved drills.",
        "video": "https://www.youtube.com/embed/3mCgD285RQA",
    },
    {
        "title": "Recovery Stretch Sequence",
        "category": "Recovery",
        "description": "Gentle stretches to support muscle recovery after tough training.",
        "video": "https://www.youtube.com/embed/3Vfcm6lX3Ws",
    },
]

ATHLETE_QUOTES = [
    {
        "name": "Mia, Soccer Midfielder",
        "quote": "Stretching before practice helps me move faster and recover stronger.",
    },
    {
        "name": "Jordan, Track Sprinter",
        "quote": "My performance improved once I trusted the mobility routine.",
    },
]

THERAPISTS = [
    {
        "name": "Alex Rivera, Sports Physio",
        "focus": "Injury prevention and movement coaching",
    },
    {
        "name": "Priya Kapoor, Performance Therapist",
        "focus": "Recovery planning and training load management",
    },
]


@app.route("/")
def home():
    return render_template("index.html", quotes=ATHLETE_QUOTES)


@app.route("/workouts")
def workouts():
    return render_template("workouts.html", workouts=WORKOUTS)


@app.route("/plan", methods=["GET", "POST"])
def plan():
    generated = None
    if request.method == "POST":
        name = request.form.get("name", "Athlete")
        sport = request.form.get("sport", "General")
        goal = request.form.get("goal", "mobility")
        days = int(request.form.get("days", 3))
        experience = request.form.get("experience", "Beginner")

        workout_focus = SPORT_GOALS.get(goal, SPORT_GOALS["mobility"])

        generated = {
            "name": name,
            "sport": sport,
            "goal": goal,
            "days": days,
            "experience": experience,
            "plan": [
                {
                    "day": f"Day {i + 1}",
                    "title": "Warmup + Skills",
                    "details": f"Start with a 10-minute dynamic warmup, then focus on {workout_focus}.",
                }
                for i in range(days)
            ],
            "advice": "Balance effort, recovery and mobility. Adjust the plan if you feel sore or need more recovery.",
        }

    return render_template("plan.html", generated=generated)


@app.route("/booking")
def booking():
    return render_template("booking.html", therapists=THERAPISTS)


if __name__ == "__main__":
    app.run(debug=True)
