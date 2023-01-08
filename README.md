# Multi-factor Authentication System to Access Linux Terminal

MFA login screen for Linux terminal made by using Whiptail. *bashrc_append.txt* file could be modified based on your needs. In the current version, it's more suitable for remote devices. Unauthorized login attempts are limited to 3. If it's exceeded, SSH process is killed (its just a playground, you can disable or change it as you wish).

## Installation

```bash
sudo apt-get update
sudo apt-get install -y whiptail

git clone https://github.com/feyzikesim/mfa_login ~/mfa_login
touch ~/mfa.db

cat ~/mfa_login/bashrc_append.txt >> ~/.bashrc
```

## Instructions
```bash
cd ~/mfa_login

# To create a new email & secret key pair
python3 -c "import sqlite_ops; sqlite_ops.create_db_record('EMAIL', 'BASE32 ENCODED STRING')"

# To list all saved emails
python3 -c "import sqlite_ops; sqlite_ops.list_all_records()"
# or
python3 -c "import sqlite_ops; sqlite_ops.list_all_records(True)"  # pass True to view emails with secret keys

# To remove a email & secret key pair
python3 -c "import sqlite_ops; sqlite_ops.remove_db_record('EMAIL')"
```

## Sample Login Attempts
Use [here](https://dan.hersam.com/tools/gen-qr-code.php) to add login information to your authenticator app (KEY field should be Base32 encoded string). I created a db record *test@gmail.com* as email and *NBQWQYLIMFUGC===* as secret key. Here's a successful login attempt;

![](https://github.com/feyzikesim/mfa_login/blob/main/pictures/successful_login.gif)

And here's a failed login attempt;

![](https://github.com/feyzikesim/mfa_login/blob/main/pictures/failed_login.gif)

## P.S to keep myself away from responsibility

Use it on your own risk. It's only tested on Raspberry Pi 4 buster. Bash version and unsynchronized system clock can cause problems. Before giving it a shot, change the **sudo pkill -P $SSH_PID** lines into **break** in *bashrc_append.txt* file.

## License

[MIT](https://choosealicense.com/licenses/mit/)
