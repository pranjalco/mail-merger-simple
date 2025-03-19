from functions import *

"""
# Project 18: Mail Merger

## Description:
This program automates the creation of personalized invitation letters. It reads a template letter from a text file,
replaces the [name] placeholder with actual names from another text file, and saves each personalized letter in a
designated folder.

## How to Use:
1. `invited_names_pr.txt` contains the list of names to be used for personalizing the letters.  
2. `starting_letter.txt` contains the message template with a placeholder (e.g., `[name]`) for replacing names.  
3. You can modify the contents of both files (`invited_names_pr.txt` and `starting_letter.txt`) as needed.  
4. Run the program by executing `app.py`.  
5. After running the program, the output text files will be saved in the `Output/ReadyToSend` folder.   

## Level
- **Level**: Simple, Simple-level automation project, beginner-friendly, task automation.
- **Skills:** Python programming, file handling, string manipulation, automation.
- **Domain:** Automation and Simulation, Text processing, file management, basic automation

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 22 Dec 2024

## Features
- Automates personalized letter creation.
- Reads a template letter and list of names from text files.
- Replaces placeholders like `[name]` with actual names.
- Saves all generated letters in a designated folder (`ReadyToSend`).
- Efficiently handles bulk letter generation.
- Easily reusable for different templates and events.
- Simplifies repetitive tasks with minimal effort.
- Supports custom formatting within the template.
- Lightweight and uses Python’s standard library.
- Ensures organized output for easy access.
"""

with open("./Input/Names/invited_names_pr.txt", "r") as name_info:
    names = name_info.readlines()

# Here we are having new line at the end of each element in the names list so we are removing it.
clean_names = []
for _ in names:
    clean_names.append(_.strip())

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    letter_content = letter.read()

for name in clean_names:

    data = letter_content.replace("[name]", name)
    # Saving the letters
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(data)

name_l()
