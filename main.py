from core.intent import detect_intent
from core.actions import perform_action

def jarvis():
    user_input = input("You: ").lower()
    intent = detect_intent(user_input)
    response = perform_action(intent)
    print(f"JARVIS: {response}")

if __name__ == "__main__":
    print("JARVIS activated. Type 'exit' to stop.")
    while True:
        jarvis()

