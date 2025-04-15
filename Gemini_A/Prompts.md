# Prompts

### Gemini 2.0 Flash
- Can you generate python code?
  - Yes, it can generate code
- Can you accept a file for inputs to python code?
  - Created code to read a file and process it
  - But it didn't really answer my question
- Can I upload a data file that you can process?
  - Answer was an indirect no.
  - Provided work around answers for accessing data from a file
    - Copy and paste into chat session
    - Provide File Contents as a String
    - Describe File Structure and provide samples

### First try
- Here is the sample data in csv format
  - Data provided - first 6 rows
  - Then it created some code to use the data, but I wasn't interested in it.
- Using the data, generate a PDF file using python that prints the Topic at the top and in the lower left corner, separate by the number of pages in the Pages as blank pages, and put lines in all pages for someone to take notes.
  - Kept version in reportlab.py, but it doesn't run. 
    - ModuleNotFoundError: No module named 'reportlab.lib'; 'reportlab' is not a package
    - Problem was that reportlab.py as a file name was interferring. 
  - Renamed version to reportlab_main.py
    - Runs now, but does not produce desired output
  - Good explanation of code and imports
- Use fpdf
  - Kept version as usefpdf_main.py.
  - Worked, but needs tweaking instructions
    - Lines per page is off
    - Initial page is blank, just header and footer
- Emulate reading the data as a csv file
  - Kept version as emulatecsv_main.py
  - Worked about the same as usefpdf_main.py
- Read the csv data into a pandas and process
  - Kept version as pandasfpdf_main.py
  - Worked about the same a emulatecsv_main.py
- Put lines on blank pages. Move header to left and footer to right.
  - Starting to work with main.py as final version
  - Moved header and footer, but still has blank pages
- Still has blank pages where the first header is. Put lines on those pages.
  - Did the task, but lines are still not over the whole page
- Fill the entire pages with lines
  - Lines fill the page, but header is repeated on each page
- Only put the header on the first page of each set of topics.
  - Code works, but too many extra pages.
- The number of pages is one more than it should be for all topics.
  - Still to many extra pages
- Still too many pages
  - Still to many extra pages
  - Decided to stop here

