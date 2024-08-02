import subprocess

# Define the fixed parts of the serial
part1 = 20
part4 = 76

# Strings to pass to the executable
param1 = "abcd"
param2 = "abcd"

# Define the path to the executable
exe_path = r"E:\\Di hoc\\Intern\\RE Training\\week1\\Reverse Problems\\Keygen\\KeyGen me lv 2\\KeyGen me lv 2.exe"

# Brute force X and Y from 0 to 255
for X in range(256):
    for Y in range(256):
        # Format the parts to ensure 3 digits
        serial = f"{part1:03d}-{X:03d}-{Y:03d}-{part4:03d}"

        try:
            # Start the process and provide inputs
            process = subprocess.Popen(
                [exe_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Send the input values
            stdout, stderr = process.communicate(input=f"{param1}\n{param2}\n{serial}\n")

            # Print output for debugging
            # print(f"Testing Serial: {serial}, Output: {stdout.strip()}")

            # Check if the output contains the desired string
            if "Right" in stdout:
                print(f"Found the correct serial! X: {X:03d}, Y: {Y:03d}")
                print(f"Serial: {serial}")
                exit(0)

        except Exception as e:
            print(f"An error occurred with serial {serial}: {e}")

print("The correct serial was not found.")
