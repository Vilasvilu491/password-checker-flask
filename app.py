from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
 
    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    
    if request.method == "POST":
        password = request.form.get("password")

        if check_password_strength(password):
            message = "Strong password! ✅"
        else:
            message = (
                "Weak password! ❌<br>"
                "Password must contain:<br>"
                "- At least 8 characters<br>"
                "- Uppercase and lowercase letters<br>"
                "- At least one digit<br>"
                "- At least one special character (!,@,#,$,%, etc.)"
            )

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)

