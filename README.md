# GUI Automation Framework - Fedex
Automation Framework for testing the GUI for Fedex

The repo contains the basic framework for the automation of the GUI test cases for the [Fedex Page](https://www.fedex.com/en-gb/home.html) along with few critical test cases automated.
**Pytest framework** has been used here for the automation and execution of the test cases.

## Framework Architecture
I have followed the Page Object Model(POM) for designing the GUI Automation Framework. [Reference here.](https://selenium-python.readthedocs.io/page-objects.html)
### Below are the major components of the Framework
* **pages**: All the POM classes are in this package
* **base**: Contains a basepage and a helper file modules.\
        - *basepage*: A base POM class which will be inherited by all the other POM classes.\
        - *helper.py*: Contains few generic functions.
* **reports**: The reports of the tests execution is saved here. The below two files are of impoartance:\
        - *pytest_report.html*: The HTML file with the test execution report. Recommended to open in a browser.\
        - *output.xml*: The xml file with the test execution report.
* **testcases**: This contains the test file and the conftest.py file\
        - *test_cases.py*: The test file containing 11 priority test cases\
        - *conftest*: Contains the setup_teardown fixture and the pytest hook implementation.
* **screenshots**: This contains the screenshots of the failed test cases. For any failed TC, the screenshot is captured before quitting the browser session. The name of the screenshot would be the test method name and in png format.
* **configfiles**: Has the test_data file containing the variables data needed for the test cases.

## How to run the tests 
### Pre-requisites

1. Clone the repository
2. Download and install the chromedriver (geckodriver would be needed to run the tests on firefox)
    - The path of the geckodriver is appended to the system path.
3. Create a Virtual environment (Though this is optional, its highly recommended) and activate it.
4. Install the required Python packages mentioned in the requirements.txt file.
    - pip install -r requirements.txt
    
*Assumed*: We already have Python 3.x installed.


### Run via terminal locally
1. In your terminal of choice navigate to the repository root (GuiAutomationFrameworkFedex directory/folder)
2. Run the below pytest command:
    - *pytest --capture=sys -rP .\testcases\test_cases.py --junitxml=.\reports\output.xml --html=.\reports\pytest_report.html*
    
    The test report files will be saved in the reports directory and the screenshots of the failed TCs will be saved in the screenshot directory with appropriate test method name.
    
### Run via Jenkins:
1. Assuming Jenkins is installed with the Pipeline plugin, create a pipeline project.
2. Create the Pipeline script as per the platform Jenkins is installed on.
     - I have added my jenkinsfile to the repo. I have my windows batch file in the build stage in the pipeline script. The root of the repository may need to be modified as per the path where the repo has been cloned.
     
## Few important points/observations from testing/automation:
- For few critical test cases like shipping, tracking of items - Proper positive scenarios could not be tested as we do not have a real tracking/shipping item(s).
- The UI was found to be unstable and inconsistent at times.
- The login consistently failed through automation. After entering the user credentials and submit, always got the message "We are having trouble establishinh a connection." message. Can refer to the screenshot test_login.png.
    - This prevented from automating many features which needed a login.
- During manual testing, after logging in, when I try to navigate to Shipping --> Returns --> Create a Return label.
    - It says, you need to login for this, despite I already being logged in and it auto logs out after this.
- Most of the times, during manual testing, when I click Ship button(With Ship icon) from the home page, it used to log me out automatically. Few times, it said, "Register to Ship" and on clicking register, it used to throw the error with message, "An error has occurredb and we are unable to process your request. Please try again."
- Through automation the navigation to the Tracking page (Page which displays the tracking information of the items) was not happening and when it did the page was different from what was seen manually. The Menu bar containing the "Track another page" doesn't show up.
- Sometimes the tracking service itself was down (Noticed both via manual testing and automated exeution). Keep getting the message, "Keep getting this message, "Unfortunately we are unable to retrieve your tracking results at this time. Please try again later."
