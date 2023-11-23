import subprocess
import os

def run_bash_process(location, filename):
    cmd = "cd " + location + " && git log -p -- " + filename + "|grep commit |wc -l"
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    output = output.decode('utf-8')
    return str(output).strip()

location = "ADD_LOCATION_HERE"

dict = {}
skip_list = [".git", ".idea", "venv", "vendor"]
for root, dirs, files in os.walk(location):
    for name in files:
        skip = 0
        for i in skip_list:
            if i in root:
                skip = 1
                break
        if skip:
            continue
        filename = os.path.join(root, name)
        # print(filename)
        commits = run_bash_process(location, filename)
        dict[filename] = int(commits)

# Dictionary sort by value descending
dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
# Dictionary print pretty
for key, value in dict.items():
    print(key + ": " + str(value))