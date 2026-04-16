import requests
import json

API_URL = 'https://script.google.com/macros/s/AKfycbzLvM9c0b3OAeHb_w1nj5JAugotWOtMaKgFa6eNh3SqVJQtd18l9KX8Xdjiy4EHUXbv/exec'

def send_message(name, email):
    response = requests.post(
        API_URL,
        json={"name": name, "email": email}
    )
    print(response.text)

def send_multiple_messages(messages):
    for message in messages:
        send_message(message['name'], message['email'])

def get_all_messages():
    response = requests.get(API_URL)
    data = response.json()
    print(json.dumps(data, indent=2))

def get_last_message():
    response = requests.get(API_URL)
    data = response.json()
    if data:
        last = data[-1]
        print(json.dumps(last, indent=2))
    else:
        print("No messages found.")

if __name__ == "__main__":
    print("Sending one message...")
    send_message("alice", "alice@example.com")

    print("\nSending multiple messages...")
    messages = [
        {"name": "bob", "email": "bob@example.com"},
        {"name": "charlie", "email": "charlie@example.com"}
    ]
    send_multiple_messages(messages)

    print("\nRetrieving all messages...")
    get_all_messages()

    print("\nRetrieving last message...")
    get_last_message()