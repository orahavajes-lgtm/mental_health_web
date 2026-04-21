from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# טעינת שני המודלים
decision_tree_model = pickle.load(open("model.pkl", "rb"))
from tensorflow.keras.models import load_model
neural_network_model = load_model("nn_model.keras")

# Encoding maps
encoding_maps = {
    "Gender": {"Female": 0, "Male": 1},
    "Occupation": {
        "Corporate": 0,
        "Student": 1,
        "Business": 2,
        "Housewife": 3,
        "Others": 4
    },
    "self_employed": {"No": 0, "Yes": 1},
    "family_history": {"No": 0, "Yes": 1},
    "Growing_Stress": {"No": 0, "Maybe": 1, "Yes": 2},
    "Changes_Habits": {"No": 0, "Maybe": 1, "Yes": 2},
    "Mental_Health_History": {"No": 0, "Maybe": 1, "Yes": 2},
    "Mood_Swings": {"Low": 0, "Medium": 1, "High": 2},
    "Coping_Struggles": {"No": 0, "Yes": 1},
    "Work_Interest": {"No": 0, "Maybe": 1, "Yes": 2},
    "Social_Weakness": {"No": 0, "Maybe": 1, "Yes": 2},
    "mental_health_interview": {"No": 0, "Maybe": 1, "Yes": 2},
    "care_options": {"No": 0, "Not sure": 1, "Yes": 2}
}

days_map = {
    "Go out Every day": 0,
    "1-14 days": 7,
    "15-30 days": 22,
    "31-60 days": 45,
    "More than 2 months": 75
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.form

    # בחירת המודל
    selected_model = data["model_type"]

    if selected_model == "Decision Tree":
        model = decision_tree_model
    else:
        model = neural_network_model

    encoded = [
        encoding_maps["Gender"][data["Gender"]],
        encoding_maps["Occupation"][data["Occupation"]],
        encoding_maps["self_employed"][data["self_employed"]],
        encoding_maps["family_history"][data["family_history"]],
        encoding_maps["Growing_Stress"][data["Growing_Stress"]],
        encoding_maps["Changes_Habits"][data["Changes_Habits"]],
        encoding_maps["Mental_Health_History"][data["Mental_Health_History"]],
        encoding_maps["Mood_Swings"][data["Mood_Swings"]],
        encoding_maps["Coping_Struggles"][data["Coping_Struggles"]],
        encoding_maps["Work_Interest"][data["Work_Interest"]],
        encoding_maps["Social_Weakness"][data["Social_Weakness"]],
        encoding_maps["mental_health_interview"][data["mental_health_interview"]],
        encoding_maps["care_options"][data["care_options"]],
        days_map[data["Days_Indoors"]]
    ]

    features = np.array(encoded).reshape(1, -1)

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = f"⚠️ Using {selected_model}: It is recommended to seek professional psychological support."
    else:
        result = f"✅ Using {selected_model}: No immediate need for professional support was detected."

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)
