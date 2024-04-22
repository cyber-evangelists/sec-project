import subprocess

def search_exploit(query):
    try:
      
        result = subprocess.run(["searchsploit", query], capture_output=True, text=True)

     
        if result.returncode == 0:
            return result.stdout.splitlines()
        else:
            return [f"Error: {result.stderr}"]
    except FileNotFoundError:
        return ["Error: searchsploit command not found. Please make sure it is installed."]


query = "WordPress 4.7"
exploits = search_exploit(query)
for exploit in exploits:
    print(exploit)
