import pickle
from sklearn.model_selection import train_test_split


def retrain_model(X, y):
    with open("models/random_forest_pipeline.pkl", "rb") as f:
        model_pipeline = pickle.load(f)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model_pipeline.fit(X_train, y_train)

    with open("models/random_forest_pipeline_updated.pkl", "wb") as f:
        pickle.dump(model_pipeline, f)

    print("Retrained model...")
    return model_pipeline.score(X_test, y_test)
