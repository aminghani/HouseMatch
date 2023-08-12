import subprocess

# Specify the path to your Bash script file
bash_script_path = '/home/amin/vscode/HouseMatch/HouseMatch/start_scrape.sh'

# Execute the Bash script using the subprocess module
subprocess.run(['bash', bash_script_path])