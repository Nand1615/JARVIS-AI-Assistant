from datetime import datetime
import sys

def perform_action(intent):
    if intent == "greeting":
        return "Hello! How can I help you?"
    
    elif intent == "time":
        return datetime.now().strftime("Current time is %H:%M:%S")
    
    elif intent == "exit":
        print("JARVIS: Shutting down. Goodbye!")
        sys.exit()
    
    else:
        return "Sorry, I didn't understand that."

