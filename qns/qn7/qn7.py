import subprocess
import os

result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
print("Installed packages: \n\n",result.stdout)

env_vars = subprocess.check_output("set", shell=True).decode()
print(env_vars)

active_users = 0

try:
    active_users = subprocess.check_output("query user", shell=True).decode()
    print(active_users)
except subprocess.CalledProcessError:
    print("No other active users or command not supported.")

with open("qn7/snaphot.txt","w") as f:
    f.write(str(result))
    f.write(str(env_vars))
    if active_users:
        f.write(str(active_users))

