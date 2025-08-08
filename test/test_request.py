import requests

BASE_URL = "http://127.0.0.1:5050"

def print_response(title, response):
    print(f"\n--- {title} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print("Response JSON:", response.json())
    except ValueError:
        print("Raw Response Text:", response.text)

def main():
    # 1. General quote
    response1 = requests.get(f"{BASE_URL}/quote")
    print_response("General Quote (no category)", response1)

    # 2. Health quote
    response2 = requests.get(f"{BASE_URL}/quote?category=health")
    print_response("Health Quote (category = health)", response2)

    # 3. Invalid category
    response3 = requests.get(f"{BASE_URL}/quote?category=banana")
    print_response("Invalid Category (category = banana)", response3)

if __name__ == "__main__":
    main()
