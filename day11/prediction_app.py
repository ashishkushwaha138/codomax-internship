#!/usr/bin/env python3
"""
Day 11 - Prediction App
Simple program to predict exam scores based on study hours using Linear Regression.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import json


def train_model():
    """Train a simple linear regression model on sample data."""
    # Sample training data: study hours vs exam scores
    # This simulates realistic data where more study hours generally lead to higher scores
    study_hours = np.array([
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5,
        0.5, 1.2, 2.8, 3.2, 4.8, 5.2, 6.8, 7.2, 8.8, 9.2
    ]).reshape(-1, 1)

    scores = np.array([
        25, 35, 45, 52, 60, 68, 72, 78, 85, 90,
        30, 40, 50, 58, 65, 70, 75, 80, 88,
        20, 28, 42, 48, 62, 66, 73, 77, 86, 89
    ])

    model = LinearRegression()
    model.fit(study_hours, scores)

    return model


def predict_score(model, hours):
    """Predict score based on study hours."""
    hours_array = np.array([[hours]])
    predicted = model.predict(hours_array)[0]
    # Clamp between 0 and 100
    return max(0, min(100, round(predicted, 2)))


def main():
    print("=" * 50)
    print("   STUDY HOURS -> SCORE PREDICTION APP")
    print("=" * 50)
    print()

    # Train the model
    print("Training model...")
    model = train_model()
    print(f"Model trained! Coefficient: {model.coef_[0]:.2f}, Intercept: {model.intercept_:.2f}")
    print()

    while True:
        try:
            user_input = input("Enter study hours (or 'q' to quit): ").strip()

            if user_input.lower() in ['q', 'quit', 'exit']:
                print("Goodbye!")
                break

            hours = float(user_input)

            if hours < 0:
                print("Please enter a positive number of hours.")
                continue

            if hours > 24:
                print("That's more than 24 hours! Please enter a realistic value (0-24).")
                continue

            predicted_score = predict_score(model, hours)

            print(f"\n📊 Prediction: {predicted_score}%")
            print(f"   Based on {hours} hour(s) of study")
            print()

            # Give some feedback
            if predicted_score >= 90:
                print("🌟 Excellent! You're on track for a top score!")
            elif predicted_score >= 75:
                print("👍 Good! Solid preparation.")
            elif predicted_score >= 60:
                print("📚 Decent. Consider adding a bit more study time.")
            else:
                print("⚠️  You might want to increase your study hours for a better score.")

            print("-" * 50)

        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()