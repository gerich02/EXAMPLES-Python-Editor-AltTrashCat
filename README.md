# Standalone Build with Python Tests

This repository shows a few Python tests that use the page object model and AltTester Unity SDK to test the Unity endless runner sample:

https://assetstore.unity.com/packages/essentials/tutorial-projects/endless-runner-sample-game-87901

### Running the tests on Windows or MacOS
The tests are meant to be run on an Windows or MacOS device. Create a folder `App` under project.
To start the tests, depending of your OS run:

❗ Starting with version 2.0.0, the AltTester Desktop must be running on your PC while the tests are running.

- MacOS/Linux:
    1. Install the [AltTesterDesktop](https://alttester.com/app/uploads/AltTester/desktop/AltTesterDesktopPackageMac__v2.0.1.zip), then open it.
    2. Create a folder `TrashCatMac` under `App`. The app is provided at https://alttester.com/app/uploads/AltTester/TrashCat/TrashCat.app.zip and needs to be included unzipped under the App/TrashCatMac/ folder.
    3. run `./start_tests_Mac.sh` in your terminal

- Windows
    1. Install the [AltTesterDesktop](https://alttester.com/app/uploads/AltTester/desktop/AltTesterDesktopPackageWindows__v2.0.1.zip), then open it. 
    2. Create a folder `TrashCatWindows` under `App`. The app is provided at https://alttester.com/app/uploads/AltTester/TrashCat/TrashCatStandAlone2_0_1.zip and needs to be included unzipped under the App/TrashCatWindows/ folder.
    3. run `./start_tests_Windows.sh` in your terminal

This script will:

- start the app on your device
- run the tests
- stop the app after the test are done

## Allure
### Run the tests:
The same setup as in the case of Windows/MaOS, but in the third step, use the following command  `start_tests_Windows_with_Allure.sh` / `start_tests_Mac_with_Allure.sh` instead of `start_tests_Windows.sh` / `start_tests_Mac.sh`

The `start_tests_Windows_with_Allure.sh`/ `start_tests_Mac_with_Allure.sh` script will:
- start the app on your device
- create an `allure-report` folder
- run the tests
- generate the allure report
- combine the allure report in a single html file
- stop the app after the test are done