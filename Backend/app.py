from flask import Flask, render_template, request, jsonify
import Core.jarvis as jarvis  # ✅ adjust import to your actual Jarvis logic

app = Flask(__name__)

# Route for frontend
@app.route("/")
def home():
    return render_template("index.html")

# API route to handle commands
@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    user_command = data.get("command", "")

    if not user_command.strip():
        return jsonify({"response": "I didn’t catch that. Please try again."})

    try:
        # ✅ Call your Jarvis core function here
        response = jarvis.process_command(user_command)
        return jsonify({"response": response})
    except Exception as e:
        print("Error:", e)
        return jsonify({"response": "Oops! Something went wrong processing your command."})

if __name__ == "__main__":
    app.run(debug=True)
