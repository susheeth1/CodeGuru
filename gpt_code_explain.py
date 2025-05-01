import openai

# Initialize OpenAI API key
openai.api_key = "Your_API_key"

def explain_code(code_snippet):
    """
    Function to explain code using OpenAI's GPT model.
    Args:
        code_snippet (str): Python code to be explained.
    Returns:
        str: Explanation of the code.
    """
    try:
        # Prompt for the AI
        prompt = f"""
        Explain the following Python code in detail, in simple language, and mention its purpose step by step:
        ```python
        {code_snippet}
        ```
        """

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the latest available model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )

        # Extract explanation
        explanation = response['choices'][0]['message']['content']
        return explanation
    except Exception as e:
        return f"An error occurred: {e}"

# Web Interface (Flask-based)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    explanation = ""
    if request.method == "POST":
        code_snippet = request.form["code"]
        explanation = explain_code(code_snippet)
    return render_template("index.html", explanation=explanation)

if __name__ == "__main__":
    app.run(debug=True)
