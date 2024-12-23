import pyotp

# Generate a random Base32 secret key
secret_key = pyotp.random_base32()
print(f"Your secret key: {secret_key}")

# Initialize the TOTP object with the secret key
totp = pyotp.TOTP("ONUGK4TMN5RWWMJXGI4Q====")

# Generate the current OTP
otp = totp.now()
print(f"Your OTP: {otp}")
