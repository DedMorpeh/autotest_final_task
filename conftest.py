import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_options(lang):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    return options


def get_firefox_profile(lang):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", lang)
    return fp


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: en, ru, uk, etc...')


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=get_chrome_options(language))
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=get_firefox_profile(language))
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
