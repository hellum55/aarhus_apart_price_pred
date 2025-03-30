import json

import requests

# URL of the MLflow prediction server
url = "http://127.0.0.1:8000/invocations"

# Sample input data for prediction
# Replace the values with the actual features your model expects
input_data = {
    "dataframe_records": [
        {
            "propertyType": 3,
            "rooms": 2,
            "size": 96,
            "buildYear": 2017,
            "cluster_100m": 0,
            "cluster_1000m": 0,
            "avg_adjusted_sqm_price_100m": 46855,
            "avg_adjusted_sqm_price_1000m": 47731,
        }
    ]
}

# Convert the input data to JSON format
json_data = json.dumps(input_data)

# Set the headers for the request
headers = {"Content-Type": "application/json"}

# Send the POST request to the server
response = requests.post(url, headers=headers, data=json_data)

# Check the response status code
if response.status_code == 200:
    # If successful, print the prediction result
    prediction = response.json()
    print("Prediction:", prediction)
else:
    # If there was an error, print the status code and the response
    print(f"Error: {response.status_code}")
    print(response.text)
