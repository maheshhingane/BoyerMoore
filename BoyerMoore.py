"""
Project - String Matching: Plagiarism Detection
Module - Boyer-Moore Algorithm
References Used - 
1. https://en.wikipedia.org/wiki/boyer_moore
2. http://www.blackbeltcoder.com/articles/algorithms/fast-text-search-with-boyer-moore
3. http://www.cs.utexas.edu/users/moore/best-ideas/string-searching/fstrpos-example.html
"""

#!/usr/bin/env python

import sys
import re
import os

#accept command line arguments
if len(sys.argv) != 3:
    print "usage: python <script_name.py> <directory_with_text_files> <pattern_file>"
    sys.exit(0)

if os.path.isdir(sys.argv[1]) == 0:
    print "directory does not exist!"
    sys.exit(0)

for textfile in os.listdir(sys.argv[1]):
    print "Checking file: ", textfile

    text = open(os.path.join(sys.argv[1], textfile)).read()
    pattern_file = ''.join(open(sys.argv[2]).readlines())

    sentences = re.split(r'[\.\?!]', pattern_file)
    counter_matched = 0
    counter_total = 0

    for pattern in sentences:
        pattern = pattern.strip()

        if len(pattern) > 0:
            counter_total += 1
            pattern_start_pos = 0
            found = 0

            while pattern_start_pos + len(pattern) <= len(text):
                #select a substring of the text of equal length to the pattern, and search from right to left
                j = pattern_start_pos + len(pattern)

                for i in range(0,len(pattern))[::-1]:

                    #if the characters in text and pattern match - 
                    if pattern[i].lower() == text[j-1].lower():
                        j = j-1

                        if j == pattern_start_pos:
                            found = 1
                            break
                        else:
                            continue
                    
                    #if the characters in text and pattern do not match - 
                    else:
                    
                        #if the 'mismatched' character does not appear in the pattern, move the pattern 'n' charcters ahead
                        if pattern[0:i].rfind(text[j-1]) == -1:
                            pattern_start_pos = pattern_start_pos + len(pattern)
                            break
                    
                        #if the 'mismatched' character appears in the pattern, move the pattern so that the matching characters are aligned
                        else:
                            pattern_start_pos = pattern_start_pos + len(pattern) - pattern[0:i].rfind(text[j-1]) - 1
                            break
                    
                #the first if statement in the for loop above has found the complete pattern in the text
                if found == 1:
                    counter_matched = counter_matched+1
                    break
                    
    print "Match percentage = %s%%" % (counter_matched*100/counter_total)
    if (counter_matched*100/counter_total) >= 70 :
        print "The input file appears to be plagiarised. %s%% of its content matches with the file %s." % ((counter_matched*100/counter_total), textfile)
