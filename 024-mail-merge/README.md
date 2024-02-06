# Mail Merge Project

## Overview
This Mail Merge project is a simple Python script designed to automate the process of generating personalized letters using a template and a list of names. The script reads a list of names from a file, replaces a specified placeholder in a letter template with each name, and saves individualized letters to an output directory.

## Usage
1. Open a terminal and navigate to the project directory.
2. Run the script using the following command:
   ```bash
   python main.py
   ```

## Output
The completed letters will be saved in the `Output/ReadyToSend` directory. Each generated letter will have a filename following the pattern: `letter_for_[name].txt`.

## Example
Suppose invited_names.txt contains the following names:
```
John Coltrane
Bill Evans
Miles Davis
```
And starting_letter.txt has the content:
```
Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

[Your Name]
```
Running the script will generate three files in the `Output/ReadyToSend` directory:
- letter_for_John Coltrane.txt
- letter_for_Bill Evans.txt
- letter_for_Miles Davis.txt

Each file will contain a personalized letter with the corresponding name.