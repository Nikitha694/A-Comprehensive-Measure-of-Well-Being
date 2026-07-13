from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load Resources
def load_resources():
    return (
        joblib.load("models/hdi_model.pkl"),
        joblib.load("models/scaler.pkl"),
        joblib.load("models/label_encoder.pkl")
    )

model, scaler, encoder = load_resources()


# Utility Functions
def get_hdi_category(score):
    categories = [
        (0.800, "Very High"),
        (0.700, "High"),
        (0.550, "Medium"),
        (0.000, "Low")
    ]

    for limit, category in categories:
        if score >= limit:
            return category


def category_details(category):
    details = {
        "Very High": (
            "very-high",
            "🌟",
            "This country ranks among the most developed nations with strong health, education, and income indicators."
        ),
        "High": (
            "high",
            "✅",
            "This country demonstrates strong human development with good performance across most indicators."
        ),
        "Medium": (
            "medium",
            "📈",
            "This country is developing. Improvements in health, education, and income can increase its HDI."
        ),
        "Low": (
            "low",
            "⚠️",
            "This country faces major development challenges in health, education, and economic growth."
        )
    }

    color, emoji, desc = details[category]
    return {
        "color": color,
        "emoji": emoji,
        "description": desc
    }


def validate(values):
    limits = {
        "Life Expectancy": (values[0], 20, 90),
        "Mean Years of Schooling": (values[1], 0, 20),
        "Expected Years of Schooling": (values[2], 0, 25),
        "GNI Per Capita": (values[3], 100, 200000)
    }

    for name, (value, minimum, maximum) in limits.items():
        if not minimum <= value <= maximum:
            raise ValueError(f"{name} must be between {minimum} and {maximum}.")


def predict_hdi(values):
    columns = [
        "Life_Expectancy",
        "Mean_Years_Schooling",
        "Expected_Years_Schooling",
        "GNI_Per_Capita"
    ]

    df = pd.DataFrame([values], columns=columns)

    scaled = scaler.transform(df)
    prediction = model.predict(scaled)[0]

    return round(float(np.clip(prediction, 0, 1)), 3)

# Routes

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        values = [
            float(request.form["life_expectancy"]),
            float(request.form["mean_years_schooling"]),
            float(request.form["expected_years_schooling"]),
            float(request.form["gni_per_capita"])
        ]

        validate(values)

        score = predict_hdi(values)

        category = get_hdi_category(score)

        info = category_details(category)

        return render_template(
            "result.html",
            hdi_score=score,
            tier=category,
            color=info["color"],
            emoji=info["emoji"],
            description=info["description"],
            life_expectancy=values[0],
            mean_years_schooling=values[1],
            expected_years_schooling=values[2],
            gni_per_capita=values[3]
        )

    except ValueError as error:
        return render_template("index.html", error=str(error))

    except Exception:
        return render_template(
            "index.html",
            error="Something went wrong. Please check your inputs."
        )


if __name__ == "__main__":
    app.run(debug=True)