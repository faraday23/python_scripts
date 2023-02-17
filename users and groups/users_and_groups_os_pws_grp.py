import os
import pwd
import grp

def add_user_to_group(user, group):
    """
    Adds a user to a group. 
    If the group does not exist, creates it.

    Parameters:
    user (str): The user to add
    group (str): The group to add the user to
    """
    try:
        grp.getgrnam(group)
    except KeyError:
        os.system("groupadd " + group)
    os.system("usermod -a -G " + group + " " + user)

def add_group(group):
    """
    Adds a new group.

    Parameters:
    group (str): The group to add
    """
    os.system("groupadd " + group)

def list_users_in_group(group):
    """
    Lists all the users in a group.

    Parameters:
    group (str): The group to list
    """
    gid = grp.getgrnam(group).gr_gid
    members = grp.getgrgid