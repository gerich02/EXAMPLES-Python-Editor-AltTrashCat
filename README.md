# Standalone Build with Python Tests

This repository shows a few Python tests that use the page object model and AltTester® Unity SDK to test the Unity Endless Runner sample:

https://assetstore.unity.com/packages/essentials/tutorial-projects/endless-runner-sample-game-87901

### Running the tests on Windows or MacOS
The tests are meant to be run on a Windows or MacOS device.
Create a folder `App` under the project.

To start the tests, depending on your OS run:

❗ Starting with version 2.0.0, the AltTester® Desktop must be running on your PC while the tests are running.

- **MacOS/Linux**:
    1. Download and install the AltTester® Desktop for MacOS from [here](https://alttester.com/downloads/), then open it.
    2. Instrument the TrashCat application using the latest version of AltTester® Unity SDK - for additional information you can follow [this tutorial](https://alttester.com/walkthrough-tutorial-upgrading-trashcat-to-2-0-x/#Instrument%20TrashCat%20with%20AltTester%20Unity%20SDK%20v.2.0.x)
    3. Create a folder `TrashCatMac` under `App` and include the instrumented app under the App/TrashCatMac/ folder.
    4. Run `./start_tests_Mac.sh` in your terminal.

- **Windows**:
    1. Download and install the AltTester® Desktop for Windows from [here](https://alttester.com/downloads/), then open it.
    2. Instrument the TrashCat application using the latest version of AltTester® Unity SDK - for additional information you can follow [this tutorial](https://alttester.com/walkthrough-tutorial-upgrading-trashcat-to-2-0-x/#Instrument%20TrashCat%20with%20AltTester%20Unity%20SDK%20v.2.0.x)
    3. Create a folder `TrashCatWindows` under `App` and include the instrumented app under the App/TrashCatWindows/ folder.
    4. Run `./start_tests_Windows.sh` in your terminal.

This script will:

- start the app on your device
- run the tests
- stop the app after the tests are done

## Allure
As an option, to run and process the test report you will need to install Allure beforehand. You can do that by using npm and the following command `npm install -g allure-commandline --save-dev` or check the Allure official page for more installation options.

To run the tests, you can use the same setup as in the case of Windows/MacOS, but in the third step, use the following command  `start_tests_Windows_with_Allure.sh` / `start_tests_Mac_with_Allure.sh` instead of `start_tests_Windows.sh` / `start_tests_Mac.sh`.


The `start_tests_Windows_with_Allure.sh`/ `start_tests_Mac_with_Allure.sh` script will:
- start the app on your device
- create an `allure-report` folder
- run the tests
- generate the Allure report
- combine the Allure report in a single HTML file
- stop the app after the tests are done
