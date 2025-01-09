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

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/mail-merger-simple.git

2. Navigate to the project directory:
   ```bash
   cd mail-merger-simple

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: You can double-click `app.py` to run it directly, provided Python is set up to execute `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.


---
**Created by Pranjal Sarnaik**  
*© 2024. All rights reserved.*

