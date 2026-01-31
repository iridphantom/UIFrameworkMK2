"""
    浏览器配置封装类
"""

from selenium import webdriver

# options封装示例
# 需要什么设置项，就取消注释
def options():
    option = webdriver.ChromeOptions()

    # 页面加载策略
    # option.page_load_strategy = 'normal'

    # 设置各类内容，只会调用两个方法：
    # option.add_argument()  # 设置常规项，用于定义已经稳定的普通的设置项
    # option.add_experimental_option()   # 试验性质的设置项，设置的内容可能存在有不稳定的状态。

    # 页面最大化.在浏览器启动时就会最大化
    option.add_argument('start-maximized')

    # # 以下两项无法与页面最大化一同使用
    # # 设置窗体在指定坐标启动
    # option.add_argument('window-position=500,500')
    #
    # # 设置窗体的初始尺寸
    # option.add_argument('window-size=1000,500')

    # 去掉“Chrome正受到自动测试软件的控制”
    # option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # # option.add_experimental_option('disable-infobars') # 无效方案，如果看到网上有这个代码，直接关掉网站即可。

    # 无头模式：浏览器不以界面形态启动，而是在后台静默运行。节省硬件资源损耗。但是依旧可以正常执行所有的操作内容。
    # 某些情况下可能会报错（例如Jenkins持续集成的时候）
    # option.add_argument('--headless')

    # 屏蔽弹窗（例如是否要保存账号密码）
    # prefs = {
    #     'credentials_enable_service': False,
    #     'profile.password_manager_enable': False
    # }
    # option.add_experimental_option('prefs', prefs)

    # 加载本地缓存
    """
        selenium默认启动的浏览器是无缓存浏览器，与常规手动启动的浏览器有很大区别。
            webdriver启动的浏览器默认不会加载本地的任何数据。默认为一个全新的浏览器。
        首先，Selenium不处理任何的验证码。所以一旦自动化中遇到验证码一定记得交由开发协助处理。不要去考虑如何破译验证码的问题。
        加载本地缓存可以作为处理验证码的手段之一，本质解决方法就是通过加载缓存，绕过登录，从而实现对验证码的处理。
        如果要加载本地缓存，记得程序执行前先关闭所有的浏览器，否则会启动失败。
    """
    # option.add_argument(r'--user-data-dir=C:\Users\1\AppData\Local\Google\Chrome\User Data')

    # # 去除控制台的多余日志信息。
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    # 如果常规日志去除无效果，则可以调用以下方法
    option.add_argument('--log_level=3')
    option.add_argument('--disable-gpu')
    option.add_argument('--ignore-certificate-errors')

    return option   # 封装成函数后，一定要记得添加return


def firefox_options():
    option = webdriver.FirefoxOptions()
    # Firefox个人资料路径
    profile_path = r"C:\Users\1\AppData\Roaming\Mozilla\Firefox\Profiles\vby4egfz.default-release"
    option.add_argument('start-maximized')
    option.add_argument("-profile")
    option.add_argument(profile_path)

    return option   # 封装成函数后，一定要记得添加return