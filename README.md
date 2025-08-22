# Verse Formatter

This project is a simple Python script that takes raw verse text and formats it into a structured, organized output. It was built as a text-processing exercise using **regular expressions** and **Python dictionaries**.

---

## 📖 What it does

- Reads a block of text containing verses (with numbers and lines).  
- Uses **regular expressions** to find and extract verse numbers and their corresponding lines.  
- Organizes the results into a **dictionary** where each verse number maps to its lines.  
- Outputs the verses in a clean, structured format like this:

v15
a. everything such as the Father has is Mine
b. because of this I said that
c. He receives from Me
d. and He will tell you


---

## 🛠️ Technologies Used

- Python 3  
- Regular Expressions (`re` module)  
- Dictionaries and basic Python data structures  

---

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/verse-formatter.git
   cd verse-formatter
2. Place your raw text file (e.g., input.txt) in the project folder.
3. Run the script:
python verse_formatter.py

4. The formatted output will be printed to the console, and you can also redirect it to a file if needed:
python verse_formatter.py > output.txt

## Example Input
5:45	a.	do not think that
		ejgw; kathgorhvsw uJmw'n pro;" to;n patevra 
	b.	I will accuse you before the Father
		e[stin oJ kathgorw'n uJmw'n  
	c.	there is someone accusing you
		Mwu>sh'" eij" o}n uJmei'" hjlpivkate 
	d.	Moses on whom you have hoped
		eij ga;r ejpisteuvete Mwu>sei' 

## Example Output
###### v15
a. everything such as the Father has is Mine
b. because of this I said that
c. He receives from Me
d. and He will tell you

### Why this project?

This script demonstrates:
Practical use of regex to find patterns in text.
How to organize text using Python dictionaries.
Looping, sorting, and formatting data into human-readable output.
It’s a solid beginner-friendly project for anyone learning Python text processing.

### Future Improvements

Add support for exporting directly to PDF.
Add CLI arguments for input/output file paths.
Build a simple web interface for uploading raw verses and downloading formatted output.

📜 License
This project is licensed under the MIT License — you are free to use, modify, and distribute it.
