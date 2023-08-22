This is the *Password Hacker (Python)* project I made myself.


<p>All sorts of creatures lurk around the Internet, including trolls, pirates, miners – and hackers. In this project you’ll wear the hat of a real hacker. You must connect to a secret server without knowing the password. Your task is to write a Python program that can hack this password, and do so in the quickest way possible.</p>

# Password Guesser Project

## Overview

The Password Guesser is a Python script designed to demonstrate the principle of guessing login credentials based on timing delays in server responses. It mimics a common technique used in hacking, but it's only intended for educational purposes and must be used responsibly.

## How it Works

1. **Guessing Logins**: The script attempts various logins from a predefined list with an empty password, looking for a specific error message that indicates a correct login.
2. **Guessing Password**: The password is guessed one character at a time by measuring the time delay in server responses. A delay indicates the correct starting symbol of the password. The process is repeated until the entire password is found.
3. **Printing Results**: Once the login and password are found, the script prints them in JSON format.

## Requirements

- **Python**: This script is written in Python and requires a Python interpreter to run.
- **Socket Library**: The script uses the built-in `socket` library to handle TCP connections.

## Usage

### Command Line Arguments

The script accepts the following command-line arguments:

- `ip`: The IP address of the server you are connecting to.
- `port`: The port number of the server you are connecting to.

### Example Usage

```
python password_guesser.py 127.0.0.1 12345
```

### Configuration

- **Login File**: The script reads a list of logins from a text file. You will need to modify the `open_file` function to point to the correct path of your login file.

## Important Notes

- **Educational Purpose Only**: This script is for educational and demonstrative purposes. Do not use it against systems you do not own or have explicit permission to test.
- **No Real Hacking Capability**: This is a hypothetical scenario and requires a specific server implementation to work. It does not possess real hacking capabilities.

## Understanding the Code

- `open_file(file_)`: Reads logins from a file.
- `guess_login(address_)`: Main function to guess login and password.
- Command-line parsing: Using `argparse` to handle command-line arguments.

## Disclaimer

This project is meant for educational purposes only. It should never be used to attempt unauthorized access to any system. Always obtain proper authorization before testing against any target.

## License

This project is open to modification, distribution, and educational use, provided it adheres to legal and ethical guidelines.

## Support and Contributions

For support or to contribute to this project, please contact the project owner.

---
Here's the link to the project: https://hyperskill.org/projects/80

Check out my profile: https://hyperskill.org/profile/103100057
