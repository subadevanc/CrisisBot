from flask import Flask, render_template, request
import pyttsx3

app = Flask(__name__)

chat_history = []
last_user_message = ""

# Preload text-to-speech engine
engine = pyttsx3.init()

def generate_response(user_input):
    user_input = user_input.lower().strip()

    # Basic keyword-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you?"
    elif "water" in user_input:
        return "Water is on the way. Stay calm and safe."
    elif "food" in user_input:
        return "We are dispatching food supplies to your area."
    elif "help" in user_input:
        return "Help is being organized. Can you share your exact location?"
    elif "jce" in user_input:
        return "Received your location as JCE. A team will reach you soon."
    else:
        return "I understand. We'll take action shortly."

@app.route("/", methods=["GET", "POST"])
def index():
    global last_user_message

    if request.method == "POST":
        user_message = request.form["message"].strip()

        if user_message and user_message != last_user_message:
            bot_response = generate_response(user_message)

            # Store chat log
            chat_history.append(("You", user_message))
            chat_history.append(("CrisisBot", bot_response))
            
            # Speak it
            engine.say(bot_response)
            engine.runAndWait()

            last_user_message = user_message  # update for repetition check

    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)