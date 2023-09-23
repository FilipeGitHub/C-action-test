import os, subprocess

#Settings
TEST_DIR = "."
CODE_FILE = "main.c"
COMPILER_TIMEOUT = 10
RUN_TIMEOUT = 10

#Creste absolute path 
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")


# Compile the program
print("Building...")
try: 
    ret = subprocess.run(["gcc", code_path, "-o", app_path],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         timeout=COMPILER_TIMEOUT)
except Exception as e:
    print("ERROR: Compilation failed.", str(e))
    exit(1)


output = ret.stdout.decode('utf-8')
print(output)
output = ret.stdout.decode('utf-8')
print(output)

#Check to see if the program copmiled successfully
if ret.returncode != 0:
    print("compilation failed.")
    exit(1)

#Run the compilation program
print("Running")
try:
    ret = subprocess.run([app_path],
                         stdout=subprocess.PIPE,
                         timeout=RUN_TIMEOUT)
except Exception as e:
    print("Error: Runtime failed." , str(e))
    exit(1)

output = ret.stdout.decode("utf-8")
print(output)

#All test passed! Exit gracefully
print("All test passed!")
exit(0)