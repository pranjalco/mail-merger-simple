from functions import *

"""
# Mail Merger
This program automates personalized letter creation by reading a template, replacing `[name]` placeholders with actual names from a text file, and saving the final letters in a designated folder. 

## Author
Pranjal Sarnaik

## Features
- Reads names from `invited_names_pr.txt`.  
- Uses `starting_letter.txt` as the template.  
- Replaces `[name]` with actual names.  
- Saves personalized letters in `Output/ReadyToSend`.  
- Automates bulk letter generation efficiently.

## Level
Simple

## Tech Stack
Python | File Handling | Automation  

## How to Run
1. Clone the repo:  
   ```bash  
   git clone https://github.com/pranjalco/mail-merger-simple.git

3. Run:
    ```bash  
   python app.py
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
