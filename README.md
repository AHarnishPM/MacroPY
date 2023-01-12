# MacroPY
Python program that utilizes pynput to record and repeat sets of inputs to a Linux device.

The program takes inputs using argv and the input() function for scheduling execution

When running the code, use this format:
python3 macro.py filename function

Functions:

w: Writes a new input set to the filename, stops tracking inputs when ESC key is pressed.
r: Runs the input set in filename once\n
    - If r is followed by an integer (r5) it will run that many times in a row\n
    - If r is followed by L, the program will run for virtually forever.\n
       (Note there is no way to stop it without opening the terminal and using Ctrl C or shutting down the computer)\n
       
rS: Prompts the user to schedule a time/day of the week/month to run the inputs in filename\n
    Ex: Every Tuesday at 5:30 PM, the input set runs and tweets "It's 5:30 on Tuesday!"
