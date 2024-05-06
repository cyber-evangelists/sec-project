import docker
from decouple import config

container_Name = config("CONTAINER_NAME")

client = docker.from_env()
def construct_hydra_command(username, target_url,error_msg,passField,endpoint):
    hydra_command = f'hydra -l {username} -P /usr/list.txt {target_url} http-post-form "{endpoint}:tfUName={username}&tfUPass=^{passField}^:{error_msg}"'
    container = client.containers.get(container_Name)
    exec_command = f"bash -c '{hydra_command}'"
    exec_response = container.exec_run(exec_command)
    print(exec_response.output.decode('utf-8'))

def main():
  
    username = input("Enter the username: ")
    pass_field = input("Enter the password field: ")
    target_url = input("Enter the target URL: ")
    error_msg = input("Enter the Error Message: ")
    endpoint = input("Enter the Endpoint: ")

   
    construct_hydra_command(username, target_url,error_msg,pass_field,endpoint)

   
  
if __name__ == "__main__":
    main()

