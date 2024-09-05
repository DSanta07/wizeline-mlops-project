import shutil


def deploy_model():
    shutil.copy(
        "models/random_forest_pipeline_updated.pkl",
        "/path/to/production/model/random_forest_pipeline.pkl",
    )
