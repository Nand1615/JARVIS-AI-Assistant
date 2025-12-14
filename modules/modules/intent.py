def detect_intent(text):
    if "hello" in text or "hi" in text:
        return "greeting"
    elif "time" in text:
        return "time"
    elif "exit" in text or "bye" in text:
        return "exit"
    else:
        return "unknown"

