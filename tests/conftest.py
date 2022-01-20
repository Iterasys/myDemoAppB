import pytest
from appium import webdriver

from . import config, credentials

# definir os valores default / padrão
def pytest_addoption(parser):
    parser.addoption(
        '--baseurl',
        action='store',
        default='@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        help='caminho do Appium no Saucelabs dos EUA'
    )
    parser.addoption(
        '--host',
        action='store',
        default='saucelabs',
        help='provedor do Appium'
    )
    parser.addoption(
        '--platform_name',
        action='store',
        default='Android',
        help='Sistema Operacional do dispositivo ou emulador'
    )
    parser.addoption(
        '--platform_version',
        action='store',
        default='9.0',
        help='Versão do Sistema Operacional do dispositivo ou emulador'
    )

@pytest.fixture
def driver(request):
    # passa os valores do arquivo config.py ou os valores default do pytest_addoption
    config.baseurl = request.config.getoption('--baseurl')
    config.host = request.config.getoption('--host')
    config.platform_name = request.config.getoption('--platform_name')
    config.platform_version= request.config.getoption('--platform_version')

    # direciona para execução do Appium local ou na nuvem
    if config.host == 'saucelabs':
        test_name = request.node.name # nome do teste
        caps = {
            'platformName': 'Android',
            # 'appium:platformVersion': '10.0' # versão do emulador local
            'appium:platformVersion': '9.0',  # versão do emulador no Saucelabs
            'browserName': '',
            # 'appium:appiumVersion': '1.22.0'    # apenas quando local ou próprio (rede)
            # 'appium:deviceName': 'emulator5554' # aparelho ou emulador local
            'appium:deviceName': 'Galaxy S9 FHD GoogleAPI Emulator', # emulador no Saucelabs
            'appium:deviceOrientation': 'portrait',
            'appium:app': 'storage:filename=mda-1.0.10-12.apk',
            'appium:appPackage': 'com.saucelabs.mydemoapp.android',
            'appium:appActivity': 'com.saucelabs.mydemoapp.android.view.activities.SplashActivity',
            'appium:ensureWebviewsHavePages': True,
            'appium:nativeWebScreenshot': True,
            'appium:newCommandTimeout': 3600,
            'appium:connectHardwareKeyboard': True,
            'sauce:options': {
                'name': test_name # enviar o nome do nosso teste para o Saucelabs
            }
        }

        # montar a credencial e a url
        _credentials = credentials.SAUCE_USER_NAME + ':' + credentials.SAUCE_ACCESS_KEY
        _url = 'https://' + _credentials + config.baseurl

        # instanciar o Saucelabs
        driver_ = webdriver.Remote(_url, caps)



