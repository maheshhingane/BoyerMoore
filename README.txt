Instructions for executing the program BoyerMoore.py - 
Author - Mahesh Hingane
======================================================

System Requirements - Any system having Python2.7 installed on it. (The program should run on other versions of Python as well, but it has been tested thoroughly on Python2.7.)


Input - 1. A directory containing text files
	2. A pattern text file


Expected Output - Console window will show the matching percentages of each text file in the directory with the pattern text file. If the match is more than a certain threshold (default value 60%), an additional line will get printed to the console - "The input file appears to be plagiarised. x% of its content matches with the file F." (F - name of the file with matching percentage >= threshold, x - the matching percentage.)


Steps to execute the code - 
1. Open command prompt.
2. Change directory to the location of the code file.
3. Execute the command - 
	python BoyerMoore.py <directory_name> <pattern_file_name>
   Example - 
	python BoyerMoore.py TextFiles/ pattern.txt
4. The output will be displayed on the console.