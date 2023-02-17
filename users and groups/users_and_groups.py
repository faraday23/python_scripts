import subprocess

from passlib.hash 
import pbkdf2_sha256
import subprocess


def create_user(username, password):
    result = subprocess.run(["useradd", "-m", "-p", password, username])
    if result.returncode != 0:
        print(f"Error creating user {username}: {result.stderr}")

def create_user(username, password):
    hashed_password = pbkdf2_sha256.hash(password)
    result = subprocess.run(["useradd", "-m", "-p", hashed_password, username])
    if result.returncode != 0:
        print(f"Error creating user {username}: {result.stderr}")

def delete_user(username):
    # Delete an existing user
    subprocess.run(["userdel", "-r", username])

def add_user_to_group(username, group):
    result = subprocess.run(["usermod", "-aG", group, username])
    if result.returncode != 0:
        print(f"Error adding user {username} to group {group}: {result.stderr}")

def remove_user_from_group(username, group):
    # Remove a user from a group
    subprocess.run(["gpasswd", "-d", username, group])

def list_groups(username):
    # List all the groups a user is a member of
    result = subprocess.run(["groups", username], stdout=subprocess.PIPE)
    print(result.stdout.decode().strip())

# Example usage:
create_user("example_user", "password")
add_user_to_group("example_user", "example_group")
list_groups("example_user")
remove_user_from_group("example_user", "example_group")
delete_user("example_user")


