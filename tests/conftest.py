import os.path
import subprocess
import time

import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


@pytest.fixture(scope="function")
def appium_driver():
    # Define desired capabilities
    subprocess.run("pkill -f appium", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Start Appium server:")
    appium_process = subprocess.Popen("appium --chromedriver-executable "
                                      "/Users/snigdha/PycharmProjects/pytestAppiumDemo/chromedriver",
                                      shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(3)
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "Android Emulator",
        "appPackage": "com.saucelabs.mydemoapp.android",
        # "appActivity": "com.testdroid.sample.android.MM_MainMenu",  # MainActivity
        "appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity",
        "automationName": "UiAutomator2",  # Recommended automation name for Android
        "noReset": True,
        # "chromedriverAutodownload": True,
        "chromedriverExecutable": "/Users/snigdha/PycharmProjects/pytestAppiumDemo/chromedriver",
        "udid": "emulator-5554",
        "app": os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "mda-2.2.0-25.apk")
    }
    print(os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "mda-2.2.0-25.apk"))
    # Connect to the Appium server
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    driver.implicitly_wait(20)

    yield driver  # Provide the driver to the test case

    # Teardown after test
    # driver.quit()

    # Teardown - quit the driver and stop the Appium server after the test run
    driver.quit()
    print("\ndriver is quit.")
    appium_process.terminate()
    print("appium server is terminated.")
    # Stop the Appium server process
