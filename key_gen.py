import secrets

def generate_secret_key(length=50): # You can change the length of the secret key by passing a different value to the length parameter
    return secrets.token_urlsafe(length)

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print(f"Generated secret key: {secret_key}")