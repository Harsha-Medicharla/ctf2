from flask import Flask, render_template, request, redirect, url_for
import pyotp
import base64

app = Flask(__name__)

# Define the correct answers and keys
correct_answer = 2524  # The correct answer for the problem page
otp_secret_key = "sherlock1729"  # Key for generating OTP
otp_secret = base64.b32encode(otp_secret_key.encode('utf-8')).decode('utf-8')


# Routes
@app.route('/')
def index():
    # Page 1: Story with hints
    return render_template('index.html')


@app.route('/problem', methods=['GET', 'POST'])
def problem():
    # Page 2: Coding problem
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        if user_answer and int(user_answer) == correct_answer:
            # Redirect to login page with security key
            return redirect(url_for('login', key=otp_secret_key))
        return render_template('problem.html',
                               error="Incorrect answer. Try again!")
    return render_template('problem.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login page with OTP validation
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        otp = request.form.get('otp')

        if username == "sherlock" and password == "221B-SH3RLOCK":
            totp = pyotp.TOTP(otp_secret)
            if totp.verify(otp):
                return render_template('success.html')
            return "Invalid OTP", 400
        return "Invalid credentials", 400

    # Display login page
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
