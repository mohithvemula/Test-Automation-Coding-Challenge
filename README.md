## Prerequisites & Setup Instructions
* Python installed (3.8+)
* pip (package installer, which should be installed by default with a python installation)
* Selenium for Python
    * `pip install selenium`
    * preferably version 4.0.0+
* ChromeDriver
    * https://developer.chrome.com/docs/chromedriver/downloads
    * Visit the above website and download the latest version available
    * Move the extracted zip file to a convenient location and add to PATH
    * If the above doesn't work, please look at the local chromedriver.exe included with the project folder under `/driver`
    * If necessary, overwrite this `.exe` file as the local path resolution has already been setup through the line of code 
        `service = Service(executable_path="driver\chromedriver.exe")`
        in `main.py`
* Chromium based browser
    * Google Chrome should work
    * Default installation of Edge that comes with Windows 11 (chromium based) should also work
* I ran all tests and the script using VSCode, but it should work on any other IDE or just using the terminal like `python ./main.py` in the current directory

## Assumptions made
* Assuming that when the tests are being run, the first card clicked after the 'Next To Jump' text are live and bets can be placed
* Assuming user does not have to be logged in (although bets can't be placed without user login, only used for verification purposes)

## Problems encountered
* Initially, I was using inpect element in full-screen mode to select various elements, however, I noticed that these change based on screen size (as we need 420px width). Then, I updated my workflow to use the screen at that size, to select the elements.
* data/test-automation-id is sometimes duplicated over multiple elements and divs. To get over this, I used raw XPATH of these elements

## Problems I may encounter as test suite grows
* As I'm using raw XPATH locators, this may become irrelevant as the website grows or if any component layout changes. To fix this, I could try and implement GREP based XPATH locators, or sub-locating using the data/test-automation-id attribute for elements

## Improvement areas
* Using a specific user-flow like Cucumber, (WHEN, THEN, GIVEN) could consolidate the above issues by sticking to a guideline