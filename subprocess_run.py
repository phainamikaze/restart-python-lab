import subprocess

# subprocess.run(["ls","-l","lab14"])

# command="uname"
# commandArgument="-a"
# print(f'Gathering system information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument])

command="ls"
commandArgument="-l"
print(f'Gathering system information with command: {command} {commandArgument}')
output = subprocess.run([command,commandArgument],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

print(output.stderr)