import os
import secrets

def generate_secret_key(length=50):
    return secrets.token_urlsafe(length)

def save_to_env_file(secret_key, file_path='.env'):
    with open(file_path, 'w') as file:
        file.write(f'SECRET_KEY={secret_key}\n')

if __name__ == "__main__":
    secret_key = generate_secret_key()
    save_to_env_file(secret_key)
    print(f'Secret key generated and saved to .env file')