# coding=utf-8
import time

from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'ec80ffe5',
    'platformVersion': '11',
    # 'appPackage': 'com.tencent.mm',
    # 'appActivity': 'com.tencent.mm.ui.LauncherUI',
    'appPackage': 'com.android.settings',
    'appActivity': '.MainSetting',
    'ignoreHiddenApiPolicyError': True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
driver.quit()


# UnknownError: An unknown server-side error occurred while processing the command. Original error: Appium Settings app is not running after 5000ms
#     at getResponseForW3CError (C:\Users\think\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\protocol\errors.js:804:9)
#     at asyncHandler (C:\Users\think\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\protocol\protocol.js:380:37)

