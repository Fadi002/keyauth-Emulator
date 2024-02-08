# KeyAuth Emulator Server - drop a like

This is a Flask-based emulator server designed to mimic the behavior of the KeyAuth authentication system. It provides endpoints for initializing, logging in, and handling license requests which anyone can do, and it's not a bypass 


## Changeable Values

- `SECRET`: A secret key used for hashing and signature generation. *You need change this value*.
- `SESSION_ID`: A random session ID is generated for each session. You can change it if needed.
- `NONCE`: A unique identifier used for security purposes. It's recommended not to change it.
- `SUBSCRIPTION`: Default subscription level. You can leave it unchanged.
- `SUBSCRIPTION_LEVEL`: Default subscription level. You can leave it unchanged.
- `FAKE_LICENSE`: A fake license key used for testing. You can leave it unchanged.
- `EXPIRY`: Expiry date for licenses. You can leave it unchanged.
- `ENCKEY`: Encryption key. *Leave it unchanged and don't change it*.
- `IP_SPOOF`: Whether to enable IP spoofing if you dont want your real ip show up.

## Supported keyauth functions

- `init()`: emulate the init function
- `login()`: emulate the login function
- `license()`:emulate the license function

## Usage

1. Clone the repository.
2. Modify the changeable values as per your requirements.
3. Run the Flask application (`main.py`).
4. Access the server endpoints to test the authentication process.
5. Enjoy !!

## Endpoints

- `/`: Home page of the KeyAuth emulator server.
- `/api/1.2/`: API endpoint for initializing, logging in, and handling license requests.

## Is That a Bypass?

**Absolutely not.** This program is **not** a KeyAuth Bypass. Its sole purpose is to emulate the KeyAuth Server, and this can be achieved by any program or even manually.

Please refrain from referring to this emulator as a "Bypass" as it spreads false information.

It's important to note that this emulation is not the same as KeyAuth "bypasses." Here, emulation refers to replicating the behavior of a public server using the same KeyAuth application information. It does not interact with the program's memory in any way.

## License

This project is licensed under the MIT License

## Skids

Just enjoy it and don't sell it

## DMCA VIOLATIONS

Do these projects violate DMCA? Absolutely not.

This program only shows a method that can be done manually without any problem. It is a clone of the original KeyAuth Server. This can be done by everyone, and it does not interact with Process Memory.

It does not modify programs in any way.