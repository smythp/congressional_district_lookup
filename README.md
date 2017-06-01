# Congressional District Lookup

Parses a .csv file with addresses and adds a column with congressional districts


### To run

1\. Install [Python 3](https://www.python.org/downloads/).  
2\. Install [Git](https://git-scm.com/downloads).  
3\. Open the terminal (or `cmd` on Windows). In OSX, click the magnifying glass in the top right of your desktop (the finder) and type `terminal`. It should be the first item that comes up. On Windows, open the start menu and type `cmd` in the search box.  
4\. Use Git to clone the repository to your computer. Enter this:

    git clone git@github.com:smythp/congressional_district_lookup.git
	
5\. Enter the cloned folder in the command line:

    cd congressional_district_lookup
	
6\. Get a Google API key [here](https://developers.google.com/maps/documentation/geocoding/get-api-key). Once you have the key, copy it exactly as presented..  
7\. Open the `key.py` file in a text editor (like Notepad or TextWrangler) and paste your key between the single quotes.  
8\. Install the `requests` library using the pip package manager:

    pip install requests
	
9\. Copy the target CSV to the cloned folder. You can use the graphical interface for this. The folder is probably in /Users/<yourname>/congressional_district_lookup on OSX or C:\Users\<yourname>\congressional_district_lookup on Windows.  
10\. Run the script:

	python lookup.py <FILENAME>
	
where `<FILENAME>` is the name of the .csv file.  
11\. Wait for the script to finish. The output should be in a file called `output.csv`.  

Note that the target CSV must have the following fields on the first line (no caps):

	address, city, county, state, zip
