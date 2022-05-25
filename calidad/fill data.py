# To make user data

from werkzeug.security import check_password_hash, generate_password_hash

if __name__ == "__main__":
    # Create a username and password
    username = input("Username: ")
    password = input("Password: ")
    password_hash = generate_password_hash(password)

    # Save the username and password in a file
    with open("users.txt", "a") as f:
        f.write(f"{username}::{password_hash}\n")
