Project: Mini WebScraper
Michael Davis
ver. python 2.7

*This webscraper uses html websites saved from individual members of the https://cs.txstate.edu/accounts/faculty/ website and retrieves their name, their education, research interests, email and webpage then outputs this information into a tagged output file.
*I have saved these HTMLs directly because the currnt website could be changed in the future where the tags I have used to search would be broken.
*Direct web functionality can easily be added using the urllib tool
*This webscraper uses the beautifulsoup python library to handle the HTML parsing by searching for the desired tags
*in order to compile the mini.py you must download and install bautifulsoup ver 4 for python 2.
*for python 2 use command "apt-get install python-bs4" to install (requires root)
*if you would like to avoid installation of BS4 I also included an already compiled mini.pyc to run
*I have included 3 html files for input, no special instructions are needed to load them
*The program can also handle many more input HTML files so if you have any more faculty HTML pages you wish to test, simply put them in the same folder as whichever version of mini you wish to execute
