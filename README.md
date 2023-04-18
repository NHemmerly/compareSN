# compareSN
A command line program that takes two CSV files as input, and outputs items from the second file that exist in the first file

This very simple program operates on the command line, and I made it to help process through scrap material at my current place of work.

The git repository includes two files useful for testing. The listSN CSV file represents a master list of serial numbers that need to be removed from physical inventory. The scanSN CSV file represents physical material serial numbers that are scanned into a CSV file (or spreadsheet that is converted into a CSV file). My code will look at each line in the scanSN file and check if the value exists in the listSN file, if it does it will be printed to the terminal. 

## Usage

Using my program is very simple if you are comfortable with the command line. 

    python3 compareSN.py masterList.csv scannedList.csv
    
The first file 'masterList.csv' should always be the file of 'scrap' serial numbers, or serial numbers that need to be removed from physical inventory. The second file 'scannedList.csv' should always be the physical material that is scanned into a computer and converted into a CSV. 
