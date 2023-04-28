# ISBN-Look-Up

DESCRIPTION: This is a simple GUI that is meant to take an ISBN and get the metadata so the book can be logged into a database. The code is written in Python and uses the packages tkinter, pyodbc, and isbnlib. It cycles through Google Books, Open Library, World Cat, and Wikidata to get the metadata from the ISBN given. 

CHANGES: The code is written at this point to write to an access database and has a hardcoded path on line 30, all you have to do is replace {YOUR PATH HERE} with the path to your file and possibly change the name of the file. 

CHANGES: In addition, this code uses SQL to write to the database from lines 67 - 69 and will need to be changed to fit your table. When adapting the SQL to your database replace 'Library' to be the name of your table and TITLE, AUTHOR, YEAR_PUBLISHED, PUBLISHER to be the name of your columns, this is where it will insert each of these variables. The number of values being added should also match the number of columns being listed before it (i.e. TITLE, AUTHOR, etc). 
      * Side note, theoretically in Python in order to use quotation marks within a string you should be able to use \" but for some reason there is a bug when using     that within an SQL statement it wont submit to the database, so chr(39) is my work around to this. It looks clunky but works like a charm. 
      
INSTALL: To run this script you will need the packages tkinter, pyodbc, and isbnlib. 
To install requirements use: 
pip3 install requirements.txt

RUN APPLICATION: Open command prompt and navigate to the directory by using 
cd {YOUR_PATH_TO_SCRIPT}
python ISBNscraper.py
