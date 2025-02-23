## ml_model.py
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import joblib

def train_advanced_ml_model():
    """
    Train an advanced ML model using a Random Forest regressor with hyperparameter tuning.
    The input feature is the incident severity and the target is the penalty adjustment.
    
    GridSearchCV is used to find the best hyperparameters based on dummy training data.
    """
    # Dummy training data: severity -> penalty adjustment
    X = np.array([[10], [8], [6], [4], [2]])
    y = np.array([5, 4, 3, 1, 0])
    
    # Define a parameter grid for hyperparameter tuning
    param_grid = {
        'n_estimators': [10, 50, 100],
        'max_depth': [None, 3, 5],
        'min_samples_split': [2, 4]
    }
    
    # Initialize the Random Forest regressor
    rf = RandomForestRegressor(random_state=42)
    
    # Use GridSearchCV to tune hyperparameters with 3-fold cross-validation
    grid_search = GridSearchCV(rf, param_grid, cv=3, scoring='neg_mean_squared_error')
    grid_search.fit(X, y)
    
    # Retrieve the best model from the grid search
    best_model = grid_search.best_estimator_
    print("Advanced Model Best Parameters:", grid_search.best_params_)
    
    # Save the model to disk for future use
    joblib.dump(best_model, "advanced_incident_penalty_model.pkl")
    return best_model

def load_advanced_ml_model():
    """
    Load the advanced ML model from disk if available, otherwise train a new one.
    """
    try:
        model = joblib.load("advanced_incident_penalty_model.pkl")
        return model
    except Exception:
        print("Advanced model not found, training a new one.")
        return train_advanced_ml_model()

# Example usage:
if __name__ == "__main__":
    model = load_advanced_ml_model()
    # Test prediction: for an incident severity of 7
    predicted_penalty = model.predict([[7]])[0]
    print(f"Predicted penalty for severity 7: {predicted_penalty:.2f}")