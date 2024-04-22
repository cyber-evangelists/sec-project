import docker

def run_command_in_container(container_name, command):
    client = docker.from_env()
    container = client.containers.get(container_name)
    exec_command = f"bash -c '{command}'"
    exec_response = container.exec_run(exec_command)
    return exec_response.output.decode('utf-8')

# Replace 'searchsploit_container' with the actual name of your container
container_name = 'quirky_khorana'
command = 'searchsploit vsftpd 2.3.4'

output = run_command_in_container(container_name, command)
print(output)
