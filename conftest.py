import pytest

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',help='type in browser')

@pytest.fixture(scope='class')

def test_setup(request):

    from selenium import webdriver

    browser = request.config.getoption('--browser')

    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C://Users//rakes//PycharmProjects//AutomationFramework//Driver//chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="")

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()
    print("Test Passed")







