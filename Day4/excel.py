import pandas as pd
import secrets


def generate_login(name, last_name):
    return name[0] + last_name


def generate_password():
    password_length = 10
    return secrets.token_urlsafe(password_length)


def generate_passwords_list(rows):
    i = 1
    passwords = []
    while i <= rows:
        passwords.append(generate_password())
        i += 1
    return passwords


def add_login_password(input_file_name: str, output_file_name: str):
    data = pd.read_excel(input_file_name)
    data['Login'] = list(map(generate_login,data['Имя'],data['Фамилия']))
    data['Passwords'] = generate_passwords_list(len(data.index))
    data.to_excel(output_file_name)
