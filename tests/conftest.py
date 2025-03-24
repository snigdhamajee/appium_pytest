import pytest
from appium import webdriver


@pytest.fixture(scope="function")
def appium_driver(request):
    # Define desired capabilities
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",  # Replace with your device/emulator version
        "deviceName": "Android Emulator",  # Replace with your device name
        "appPackage": "com.testdroid.sample.android",  # Replace with your app package
        "appActivity": "com.testdroid.sample.android.MM_MainMenu",  # MainActivity
        "automationName": "UiAutomator2",  # Recommended automation name for Android
        "noReset": True,
        "udid": "emulator-5554",
        "app": "/Users/snigdha/Downloads/testdroid-sample-app.apk"
    }

    # Connect to the Appium server
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    # request.cls.driver = driver

    yield driver  # Provide the driver to the test case

    # Teardown after test
    driver.quit()
