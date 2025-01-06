from key_gen import generate_secret_key
import os

def save_to_env_file(secret_key, file_path='.env'):
    with open(file_path, 'w') as file:
        file.write(f'SECRET_KEY={secret_key}\n')

if __name__ == "__main__":
    secret_key = generate_secret_key()
    save_to_env_file(secret_key)
    print(f'Secret key generated and saved to .env file')