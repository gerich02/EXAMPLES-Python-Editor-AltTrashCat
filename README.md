# Standalone Build with Python Tests

This repository shows a few Python tests that use the page object model and AltTester® Unity SDK to test the Unity Endless Runner sample:

https://assetstore.unity.com/packages/essentials/tutorial-projects/endless-runner-sample-game-87901

### Running the tests on Windows or MacOS
The tests are meant to be run on a Windows or MacOS device.

To start the tests, depending on your OS run:

❗ Starting with version 2.0.0, the AltTester® Desktop must be running on your PC while the tests are running.

1. Install and open AltTester® Desktop:
   - **MacOS/Linux**: Download and install the AltTester® Desktop for MacOS from [here](https://alttester.com/downloads/)
   - **Windows**: Download and install the AltTester® Desktop for Windows from [here](https://alttester.com/downloads/)
2. Instrument the TrashCat application using the latest version of AltTester® Unity SDK - for additional information you can follow [this tutorial](https://alttester.com/walkthrough-tutorial-upgrading-trashcat-to-2-0-x/#Instrument%20TrashCat%20with%20AltTester%20Unity%20SDK%20v.2.0.x)
3. Launch example project game:
   1. Run AltTester® editor in Unity project.
   2. Select platform Editor.
   3. Click Play in Editor.
4. Run `./start_tests.sh` in your terminal:
   - **MacOS/Linux**: Use Terminal
   - **Windows**: Use Git Bash or other unix terminal emulator

This script will:

- start the app on your device
- run the tests
- stop the app after the tests are done
