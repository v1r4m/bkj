import subprocess
import os

# Change directory to "2143"
os.chdir("2143")

import random
while True:
# 파이썬 코드 실행
    with open("input.txt", "w") as file:
        # Write the value for variable n on the first line
        t = random.randint(1,20)  # You can replace this with your desired value for n
        file.write(str(t) + "\n")

        # Write the value for variable m on the second line
        n = random.randint(1,5)  # You can replace this with your desired value for m
        file.write(str(n) + "\n")

        for i in range(n):
            file.write(str(random.randint(1,10))+" ")
        
        file.write("\n")

        m = random.randint(1,5)  # You can replace this with your desired value for m
        file.write(str(m) + "\n")

        for i in range(m):
            file.write(str(random.randint(1,10))+" ")
        
        file.write("\n")
        
    python_command = "python 2143.py < input.txt"
    python_process = subprocess.Popen(python_command, shell=True, stdout=subprocess.PIPE)
    python_output, python_error = python_process.communicate()

    # 자바 코드 실행
    java_command = "java Main.java < input.txt"
    java_process = subprocess.Popen(java_command, shell=True, stdout=subprocess.PIPE)
    java_output, java_error = java_process.communicate()

    # 두 결과 비교
    if python_output != java_output:
        print("두 코드의 결과는 다릅니다.")
        exit()
