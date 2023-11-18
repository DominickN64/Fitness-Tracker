from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "You have been logged out"

@auth.route("/sign-up", methods = ["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
    
        if len(email) == 0:
            flash("Fill in email", category="error")
        elif len(firstName)==0:
            flash("Fill in first name", category="error")
        elif len(password1) == 0:
            flash("Fill in password", category="error")
        elif len(password2) == 0:
            flash("Fill in password confirmation", category="error")
        elif password1 != password2:
            flash("Passwords don't match", category="error")
        else:
            flash("Account created", category="success")
    

    
    
    return render_template("sign_up.html")
