import pandas as pd
from zenml import step


@step
def dynamic_importer() -> str:
    """Dynamically imports data for testing out the model."""
    # Here, we simulate importing or generating some data.
    # In a real-world scenario, this could be an API call, database query, or loading from a file.
    data = {
        "propertyType": [3],
        "rooms": [2, 6],
        "size": [40, 188],
        "buildYear": [1888, 2022],
        "cluster_100m": [0, 57],
        "cluster_1000m": [0, 7],
        "avg_adjusted_sqm_price_100m": [35000, 50000],
        "avg_adjusted_sqm_price_1000m": [35000, 47000],
    }

    df = pd.DataFrame(data)

    # Convert the DataFrame to a JSON string
    json_data = df.to_json(orient="split")

    return json_data
