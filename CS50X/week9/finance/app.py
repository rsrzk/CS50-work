import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    shares = db.execute(
        "SELECT symbol, SUM(shares) AS shares FROM shares WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
        user_id,
    )
    total_shares = 0
    total_value = 0
    for share in shares:
        share["price"] = lookup(share["symbol"])["price"]
        share["value"] = share["price"] * share["shares"]
        total_shares += share["shares"]
        total_value += share["value"]
    return render_template(
        "index.html",
        user_cash=user_cash,
        shares=shares,
        total_shares=total_shares,
        total_value=total_value,
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    user_id = session["user_id"]
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        try:
            shares = int(shares)
            if shares <= 0:
                return apology("Invalid number of shares", 400)
        except ValueError:
            return apology("Invalid number of shares", 400)
        stock = lookup(symbol)
        if stock is None:
            return apology("Invalid stock", 400)
        price = stock["price"]
        cost = shares * price
        if user_cash < price:
            return apology("Insufficient balance")
        else:
            db.execute(
                "UPDATE users SET cash = ? WHERE id = ?", user_cash - cost, user_id
            )
            db.execute(
                "INSERT INTO shares (user_id, symbol, shares, price, cost) VALUES(?, ?, ?, ?, ?)",
                user_id,
                symbol,
                shares,
                price,
                cost,
            )
        flash("Shares purchased successfully")
        return redirect("/")
    else:
        return render_template("buy.html", user_cash=user_cash)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    shares = db.execute(
        "SELECT dt, symbol, shares, price, cost FROM shares WHERE user_id = ?", user_id
    )
    total_shares = 0
    total_value = 0
    for share in shares:
        if share["shares"] > 0:
            share["order"] = "BUY"
        else:
            share["order"] = "SELL"
        total_shares += share["shares"]
        total_value += share["cost"]
    return render_template(
        "history.html",
        user_cash=user_cash,
        shares=shares,
        total_shares=total_shares,
        total_value=total_value,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        # Redirect user to home page
        flash("You were successfully logged in")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        stock = lookup(symbol)
        if stock is None:
            return apology("Invalid stock", 400)
        return render_template("quoted.html", stock=stock)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Invalid username", 400)
        if not password or password != confirmation:
            return apology("Invalid password or confirmation does not match", 400)
        usernames = db.execute("SELECT username FROM users")
        usernames = [user["username"] for user in usernames]
        if username in usernames:
            return apology("Username already in use. Please try another", 400)
        hash = generate_password_hash(password)

        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
        ## Auto sign-in feature. Need to remove for submission
        # user_id = db.execute("SELECT last_insert_rowid() AS id")[0]["id"]
        # session["user_id"] = user_id
        # flash('You were successfully logged in')
        return redirect("/")
    else:
        return render_template("register.html")

@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Change user password"""
    if request.method == "POST":
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        confirmation = request.form.get("confirmation")
        current_password = db.execute(
            "SELECT * FROM users WHERE id = ?", session["user_id"]
        )[0]["hash"]

        if not check_password_hash(current_password, old_password):
            return apology("The old password you entered does not match", 400)
        if not new_password or new_password != confirmation:
            return apology("Invalid new password or confirmation does not match", 400)
        hash = generate_password_hash(new_password)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, session["user_id"])
        flash("Your password has been updated.")
        return redirect("/")
    else:
        return render_template("password.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        try:
            user_shares = db.execute(
                "SELECT SUM(shares) AS shares FROM shares WHERE user_id = ? AND symbol = ? GROUP BY symbol",
                user_id,
                symbol,
            )[0]["shares"]
        except ValueError:
            return apology("Invalid shares", 400)
        try:
            shares = int(shares)
            if not 0 < shares <= user_shares:
                return apology("Invalid number of shares", 400)
        except ValueError:
            return apology("Invalid number of shares", 400)
        stock = lookup(symbol)
        if stock is None:
            return apology("Invalid stock", 400)
        price = stock["price"]
        value = shares * price
        db.execute("UPDATE users SET cash = ? WHERE id = ?", user_cash + value, user_id)
        db.execute(
            "INSERT INTO shares (user_id, symbol, shares, price, cost) VALUES(?, ?, ?, ?, ?)",
            user_id,
            symbol,
            shares * -1,
            price,
            value,
        )
        flash("Shares sold successfully")
        return redirect("/")
    else:
        shares = db.execute(
            "SELECT symbol, SUM(shares) AS shares FROM shares WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
            user_id,
        )
        return render_template("sell.html", user_cash=user_cash, shares=shares)
