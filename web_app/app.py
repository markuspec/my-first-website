from flask import Flask, render_template, request

app = Flask(__name__)

SPORT_GOALS = {
    "strength": "strength building, power work, and controlled recovery",
    "speed": "acceleration drills, agility work, and dynamic mobility",
    "endurance": "conditioning, pacing, and low-impact recovery",
    "mobility": "joint mobility, stability, and restorative stretching",
}

SPORT_TEMPLATES = {
    "soccer": "ball control, deceleration, and lower-body stability",
    "basketball": "footwork, jump preparation, and quick change-of-direction work",
    "track": "sprint mechanics, hip mobility, and post-run recovery",
    "volleyball": "jump readiness, shoulder control, and landing mechanics",
    "swimming": "shoulder mobility, posture, and recovery breathing",
    "football": "explosive starts, mobility, and recovery between sessions",
    "general": "balanced movement skills, mobility, and confidence-building practice",
}

WORKOUTS = [
    {
        "title": "Dynamic Warmup Flow",
        "category": "Warmup",
        "description": "A quick activation sequence that prepares the hips, ankles, and shoulders for sport.",
        "benefit": "Better readiness before practice or competition",
        "video": "https://www.youtube.com/embed/5P0uHCaAGeU",
    },
    {
        "title": "Hip Mobility Reset",
        "category": "Mobility",
        "description": "Open the hips and improve range of motion with controlled movement patterns.",
        "benefit": "Improved stride length and lower-body control",
        "video": "https://www.youtube.com/embed/3mCgD285RQA",
    },
    {
        "title": "Lower Body Recovery Stretch",
        "category": "Recovery",
        "description": "A calming routine that targets quads, hamstrings, calves, and glutes.",
        "benefit": "Supports muscle recovery after hard sessions",
        "video": "https://www.youtube.com/embed/3Vfcm6lX3Ws",
    },
    {
        "title": "Shoulder Stability Circuit",
        "category": "Strength",
        "description": "Build shoulder control and posture through strength and stability work.",
        "benefit": "Helpful for overhead sports and injury prevention",
        "video": "https://www.youtube.com/embed/7rM-9uE0D7I",
    },
    {
        "title": "Agility Ladder Drill Set",
        "category": "Speed",
        "description": "Practice footwork, rhythm, and quick direction changes.",
        "benefit": "Boosts coordination and reaction speed",
        "video": "https://www.youtube.com/embed/JCw-AY1fSbo",
    },
    {
        "title": "Post-Training Mobility Flow",
        "category": "Recovery",
        "description": "A full-body reset designed to reduce tightness after a long day of training.",
        "benefit": "Improves recovery quality and movement comfort",
        "video": "https://www.youtube.com/embed/8Vn0nV8H0xM",
    },
]

ATHLETE_QUOTES = [
    {
        "name": "Alkin Chan, Hong Kong Rower",
        "quote": "Staying consistent with my mobility routine has been a game-changer for my rowing performance and recovery.",
    },
    {
        "name": "Jordan, Track Sprinter",
        "quote": "Once I trusted my mobility routine, my speed work felt smoother and more controlled.",
    },
    {
        "name": "Avery, Basketball Guard",
        "quote": "Having a clear plan for training and recovery made a huge difference in my routine.",
    },
]

THERAPISTS = [
    {
        "name": "Alex Rivera, Sports Physio",
        "focus": "Injury prevention, movement coaching, and return-to-play support",
    },
    {
        "name": "Priya Kapoor, Performance Therapist",
        "focus": "Recovery planning, training load management, and athlete mindset",
    },
    {
        "name": "Marcus Lee, Strength Coach",
        "focus": "Power development, jumping mechanics, and athletic conditioning",
    },
]

BOOKING_SLOTS = {
    "Alex Rivera, Sports Physio": [
        {"day": "Tue 24", "time": "9:00 AM", "available": True},
        {"day": "Tue 24", "time": "11:00 AM", "available": True},
        {"day": "Wed 25", "time": "3:00 PM", "available": True},
        {"day": "Thu 26", "time": "10:30 AM", "available": True},
    ],
    "Priya Kapoor, Performance Therapist": [
        {"day": "Tue 24", "time": "1:00 PM", "available": True},
        {"day": "Wed 25", "time": "4:30 PM", "available": True},
        {"day": "Thu 26", "time": "6:00 PM", "available": True},
        {"day": "Fri 27", "time": "5:00 PM", "available": True},
    ],
    "Marcus Lee, Strength Coach": [
        {"day": "Wed 25", "time": "8:00 AM", "available": True},
        {"day": "Fri 27", "time": "9:30 AM", "available": True},
        {"day": "Sat 28", "time": "11:00 AM", "available": True},
        {"day": "Sun 29", "time": "2:00 PM", "available": True},
    ],
}

BODY_PART_ROUTINES = {
    "shoulders": {
        "label": "Shoulders",
        "description": "Great for overhead sports, posture, and upper-body control.",
        "stretches": [
            {
                "title": "Cross-Body Shoulder Stretch",
                "description": "A gentle stretch that opens the rear shoulder and upper back.",
                "time": "30-45 sec each side",
            },
            {
                "title": "Doorway Chest Stretch",
                "description": "Helps open the chest and improve shoulder position for sports.",
                "time": "30 sec each side",
            },
            {
                "title": "Overhead Triceps Stretch",
                "description": "Targets the back of the shoulder and upper arm for recovery.",
                "time": "30 sec each side",
            },
        ],
        "exercises": [
            {
                "title": "Band External Rotations",
                "description": "Builds rotator cuff strength and shoulder stability.",
                "time": "2-3 sets of 12-15 reps",
            },
            {
                "title": "Scapular Wall Slides",
                "description": "Improves shoulder blade control and posture during training.",
                "time": "2 sets of 10-12 reps",
            },
            {
                "title": "Push-Up Plus",
                "description": "Strengthens the shoulders and upper chest while improving shoulder blade control.",
                "time": "3 sets of 8-10 reps",
            },
        ],
    },
    "arms": {
        "label": "Arms",
        "description": "Helpful for grip strength, pulling power, and recovery after training.",
        "stretches": [
            {
                "title": "Triceps Overhead Stretch",
                "description": "Releases tension in the back of the upper arm and elbow.",
                "time": "30 sec each side",
            },
            {
                "title": "Wrist Flexor Stretch",
                "description": "Useful after heavy grip work, ball handling, or lifting.",
                "time": "20-30 sec each side",
            },
            {
                "title": "Forearm Pronator Stretch",
                "description": "Helps reduce tightness in the forearms after repeated wrist use.",
                "time": "20 sec each side",
            },
        ],
        "exercises": [
            {
                "title": "Biceps Curl Hold",
                "description": "Builds arm strength while keeping tension on the target muscles.",
                "time": "3 sets of 10-12 reps",
            },
            {
                "title": "Push-Up Hold",
                "description": "Develops chest, triceps, and shoulder endurance with no equipment.",
                "time": "3 rounds of 20-30 sec",
            },
            {
                "title": "Hammer Curl",
                "description": "Builds forearm and biceps strength for stronger grip and pulling power.",
                "time": "3 sets of 10-12 reps",
            },
        ],
    },
    "back": {
        "label": "Back",
        "description": "Supports posture, power transfer, and safe lifting mechanics.",
        "stretches": [
            {
                "title": "Child's Pose Reach",
                "description": "Lengthens the spinal muscles and helps ease tension across the upper back.",
                "time": "30-45 sec",
            },
            {
                "title": "Thread the Needle",
                "description": "Gently opens the upper back and shoulder area for better mobility.",
                "time": "30 sec each side",
            },
            {
                "title": "Seated Spinal Twist",
                "description": "A great recovery stretch for the lower back and side body.",
                "time": "30 sec each side",
            },
        ],
        "exercises": [
            {
                "title": "Bird Dog",
                "description": "Improves core stability and back control while moving opposite limbs.",
                "time": "3 sets of 8 reps each side",
            },
            {
                "title": "Superman Hold",
                "description": "Strengthens the lower back and posterior chain support.",
                "time": "3 rounds of 20-30 sec",
            },
            {
                "title": "Hip Hinge Practice",
                "description": "Teaches safe posture and power transfer for lifting and sprinting.",
                "time": "2-3 sets of 10 reps",
            },
        ],
    },
    "core": {
        "label": "Core",
        "description": "Essential for balance, control, and efficient movement patterns.",
        "stretches": [
            {
                "title": "Cat-Cow Flow",
                "description": "Encourages spinal mobility and gentle abdominal release.",
                "time": "1-2 min",
            },
            {
                "title": "Standing Side Stretch",
                "description": "Targets the obliques and side body for better rotation.",
                "time": "30 sec each side",
            },
            {
                "title": "Kneeling Hip Flexor Stretch",
                "description": "Helps release tightness in the front of the hips and lower abdomen.",
                "time": "30 sec each side",
            },
        ],
        "exercises": [
            {
                "title": "Dead Bug",
                "description": "Teaches the core to stay steady while the limbs move.",
                "time": "3 sets of 8-10 reps each side",
            },
            {
                "title": "Plank Hold",
                "description": "Builds trunk stability and full-body control.",
                "time": "3 rounds of 20-40 sec",
            },
            {
                "title": "Side Plank",
                "description": "Improves oblique strength and lateral stability for sport.",
                "time": "2 rounds of 20 sec each side",
            },
        ],
    },
    "legs": {
        "label": "Legs",
        "description": "Critical for sprinting, jumping, and recovery after hard sessions.",
        "stretches": [
            {
                "title": "Hamstring Reach",
                "description": "Helps reduce tightness in the back of the legs after sprinting or jumping.",
                "time": "30 sec each side",
            },
            {
                "title": "Calf Wall Stretch",
                "description": "Supports ankle range and lower-leg recovery.",
                "time": "30 sec each side",
            },
            {
                "title": "Quad Stretch",
                "description": "Great for easing tension in the front of the thigh after running.",
                "time": "30 sec each side",
            },
        ],
        "exercises": [
            {
                "title": "Bodyweight Squats",
                "description": "Builds leg strength and movement control for everyday and sport performance.",
                "time": "3 sets of 12-15 reps",
            },
            {
                "title": "Split Squat Hold",
                "description": "Great for unilateral leg stability, balance, and knee control.",
                "time": "3 rounds of 30 sec each side",
            },
            {
                "title": "Lateral Lunges",
                "description": "Improves hip mobility, strength, and side-to-side control.",
                "time": "2-3 sets of 8 reps each side",
            },
        ],
    },
}


@app.route("/")
def home():
    return render_template("index.html", quotes=ATHLETE_QUOTES)


@app.route("/workouts")
def workouts():
    return render_template("workouts.html", workouts=WORKOUTS)


@app.route("/body-map")
def body_map():
    selected_part = request.args.get("part", "shoulders")
    selected_focus = request.args.get("focus", "stretch")
    if selected_part not in BODY_PART_ROUTINES:
        selected_part = "shoulders"
    if selected_focus not in ("stretch", "exercise"):
        selected_focus = "stretch"

    part_data = BODY_PART_ROUTINES.get(selected_part, BODY_PART_ROUTINES["shoulders"])
    return render_template(
        "body_map.html",
        body_parts=BODY_PART_ROUTINES,
        selected_part=selected_part,
        selected_focus=selected_focus,
        part_data=part_data,
    )


@app.route("/plan", methods=["GET", "POST"])
def plan():
    generated = None
    if request.method == "POST":
        name = request.form.get("name", "Athlete").strip() or "Athlete"
        sport = request.form.get("sport", "General").strip() or "General"
        goal = request.form.get("goal", "mobility")
        days = max(1, min(7, int(request.form.get("days", 3) or 3)))
        experience = request.form.get("experience", "Beginner")

        sport_key = sport.lower()
        sport_focus = SPORT_TEMPLATES.get(sport_key, SPORT_TEMPLATES["general"])
        workout_focus = SPORT_GOALS.get(goal, SPORT_GOALS["mobility"])

        if experience.lower() == "advanced":
            warmup_time = "12-15 minutes"
            volume = "high-quality, focused sets"
        elif experience.lower() == "intermediate":
            warmup_time = "10-12 minutes"
            volume = "moderate sets with extra form cues"
        else:
            warmup_time = "8-10 minutes"
            volume = "light-to-moderate sets with coach feedback"

        generated = {
            "name": name,
            "sport": sport.title() if sport else "General",
            "goal": goal,
            "days": days,
            "experience": experience,
            "plan": [
                {
                    "day": f"Day {i + 1}",
                    "title": f"{goal.title()} Focus Session",
                    "details": (
                        f"Start with a {warmup_time} warmup, then work on {sport_focus}. "
                        f"Finish with {workout_focus} and a short recovery routine."
                    ),
                }
                for i in range(days)
            ],
            "advice": (
                f"For {sport or 'your sport'}, aim for consistency over intensity. Use {volume} "
                f"and keep one recovery day every week for the best long-term progress."
            ),
        }

    return render_template("plan.html", generated=generated)


@app.route("/booking", methods=["GET", "POST"])
def booking():
    booking_success = None
    if request.method == "POST":
        specialist = request.form.get("specialist", "a specialist")
        day = request.form.get("day", "TBD")
        time = request.form.get("time", "TBD")
        name = request.form.get("name", "Athlete").strip() or "Athlete"

        for therapist_name, slots in BOOKING_SLOTS.items():
            if therapist_name == specialist:
                for slot in slots:
                    if slot["day"] == day and slot["time"] == time:
                        slot["available"] = False
                        break
                break

        booking_success = {
            "name": name,
            "specialist": specialist,
            "date": f"{day} at {time}",
        }

    return render_template(
        "booking.html",
        therapists=THERAPISTS,
        booking_slots=BOOKING_SLOTS,
        booking_success=booking_success,
    )


if __name__ == "__main__":
    app.run(debug=True)
