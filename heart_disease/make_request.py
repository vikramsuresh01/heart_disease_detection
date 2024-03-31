import requests

def main():
    # Define the URL of your FastAPI application
    url = "http://127.0.0.1:8000/input_data/"

    # Define the JSON payload containing the data
    data = {
        "age": 35,
        "sex": "male",
        "chest_pain_type": 1
    }

    # Make a POST request to the FastAPI application
    response = requests.post(url, json=data)

    # Print the response
    print(response.json())

if __name__ == "__main__":
    main()
