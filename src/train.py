# src/train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# Load the scraped data
data = pd.read_csv("data/matches_2025.csv")

# Feature engineering
data["goal_diff"] = data["home_goals"] - data["away_goals"]
data["result"] = data["goal_diff"].apply(lambda x: "home_win" if x > 0 else ("away_win" if x < 0 else "draw"))

# Encode teams numerically
le_team = LabelEncoder()
data["home_team_enc"] = le_team.fit_transform(data["home_team"])
data["away_team_enc"] = le_team.transform(data["away_team"])

# Prepare training data
X = data[["home_team_enc", "away_team_enc"]]
y = data["result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Model trained. Accuracy: {acc:.2f}")
print(classification_report(y_test, y_pred))

# Save model + encoders
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/match_predictor.pkl")
joblib.dump(le_team, "models/label_encoder.pkl")

print("💾 Model and encoders saved in 'models/' directory.")
