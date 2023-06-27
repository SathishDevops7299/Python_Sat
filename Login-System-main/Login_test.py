import pytest
from tkinter import Tk
from tkinter import Entry
from tkinter import StringVar
from tkinter import Toplevel

def test_register_user():
    username_info = "test_user"
    password_info = "test_password"

    register_screen = Toplevel(Tk())
    username = StringVar()
    password = StringVar()
    username.set(username_info)
    password.set(password_info)

    username_entry = Entry(register_screen, textvariable=username)
    password_entry = Entry(register_screen, textvariable=password)

    test_register_user()

    file = open(username_info, "r")
    content = file.read()
    file.close()

    assert content == username_info + "\n" + password_info

def test_login_verify_with_valid_credentials():
    username_info = "test_user"
    password_info = "test_password"

    login_screen = Toplevel(Tk())
    username_verify = StringVar()
    password_verify = StringVar()
    username_verify.set(username_info)
    password_verify.set(password_info)

    username_login_entry = Entry(login_screen, textvariable=username_verify)
    password_login_entry = Entry(login_screen, textvariable=password_verify)

    with open(username_info, "w") as file:
        file.write(username_info + "\n" + password_info)

    test_login_verify_with_valid_credentials()

    assert login_success_screen.winfo_exists()

def test_login_verify_with_invalid_password():
    username_info = "test_user"
    password_info = "test_password"
    invalid_password = "wrong_password"

    login_screen = Toplevel(Tk())
    username_verify = StringVar()
    password_verify = StringVar()
    username_verify.set(username_info)
    password_verify.set(invalid_password)

    username_login_entry = Entry(login_screen, textvariable=username_verify)
    password_login_entry = Entry(login_screen, textvariable=password_verify)

    with open(username_info, "w") as file:
        file.write(username_info + "\n" + password_info)

   test_login_verify_with_invalid_password()

    assert password_not_recog_screen.winfo_exists()

def test_login_verify_with_invalid_username():
    username_info = "test_user"
    password_info = "test_password"
    invalid_username = "wrong_user"

    login_screen = Toplevel(Tk())
    username_verify = StringVar()
    password_verify = StringVar()
    username_verify.set(invalid_username)
    password_verify.set(password_info)

    username_login_entry = Entry(login_screen, textvariable=username_verify)
    password_login_entry = Entry(login_screen, textvariable=password_verify)

    with open(username_info, "w") as file:
        file.write(username_info + "\n" + password_info)

    test_login_verify_with_invalid_username()

    assert user_not_found_screen.winfo_exists()
