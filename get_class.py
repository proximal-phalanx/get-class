try:
    from selenium.webdriver import Chrome
    from selenium.webdriver.common.by import By
except:
    print('''请在命令行中输入\n
    pip install selenium\n
    以安装必要的包. ''')
    input()
    exit()
import time
from getpass import getpass

print('请等待窗口打开\n')
try:
    web = Chrome()
except:
    print('''请检查是否已安装Chrome浏览器,\n
    并检查是否已下载chromedriver并已将其添加到环境变量.''')
    print('''
    下载链接:\n
    chrome浏览器: https://www.google.cn/intl/zh-CN/chrome/\n
    chromedriver(windows): https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.52/\n
    chromedriver(macOS apple silicon): https://chromedriver.storage.googleapis.com/105.0.5195.52/chromedriver_mac64_m1.zip
    chromedriver(全部版本): https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.52/\n
    环境变量配置:\n
    windows: https://ceshiren.com/t/topic/21687\n
    macOS: https://www.cnblogs.com/CMbenten/p/16550193.html\n
    linux: 同mac，但是真的有linux用户不会处理环境变量?
    ''')
    input()
    exit()

vpn = True if input("是否使用VPN(y/n): ") == 'y' else False

if(not vpn):
    web.get('http://jwts.hitwh.edu.cn/loginNOCAS')
    print('使用过程中请勿以任何形式操作自动打开的窗口, 包括将鼠标移至网页中的任何内容上. ')
    time.sleep(2)
    web.find_element(By.ID, 'usercode').send_keys(input('请在终端上输入学号\n'))
    print('部分终端无法隐藏密码, 密码将可能被他人看到, 请注意保护隐私.')
    web.find_element(By.ID, 'password').send_keys(getpass('请在终端上输入密码(密码不会以任何方式保存或上传至教务系统外的其它地址)\n'))

    web.find_element(By.ID, 'code').send_keys(input('请在终端上输入验证码\n'))

    web.find_element(By.CLASS_NAME, 'login_but').click()
    time.sleep(1)
else:
    web.get('http://authserver-hitwh-edu-cn.ivpn.hitwh.edu.cn:8118/authserver/login?service=https%3A%2F%2Fivpn.hitwh.edu.cn%2Fauth%2Fcas_validate%3Fentry_id%3D1')
    print('使用过程中请勿以任何形式操作自动打开的窗口, 包括将鼠标移至网页中的任何内容上. ')
    time.sleep(2)
    web.find_element(By.ID, 'username').send_keys(input('请在终端上输入学号\n'))
    print('部分终端无法隐藏密码, 密码将可能被他人看到, 请注意保护隐私.')
    web.find_element(By.ID, 'password').send_keys(getpass('请在终端上输入密码(密码不会以任何方式保存或上传至教务系统外的其它地址)\n'))
    web.find_element(By.XPATH, '//*[@id="casLoginForm"]/p[5]/button').click()
    input("通过浏览器安全检查后, 请在终端上按回车键继续\n")
    web.get('http://172-26-64-16.ivpn.hitwh.edu.cn:8118/loginCAS')
    time.sleep(1)

tabsCount = int(input('请在终端上输入tab数\n'))

class TabConfig:

    def __init__(self, shiftPage, classXPath, pageXPath, handle) -> None:
        self.shiftPage = shiftPage
        self.classXPath = classXPath
        self.pageXPath = pageXPath
        self.handle = handle

tabConfigs = []

for i in range(tabsCount):
    web.execute_script('window.open("http://jwts.hitwh.edu.cn/loginNOCAS");' if not vpn else 'window.open("http://172-26-64-16.ivpn.hitwh.edu.cn:8118/loginCAS");')
    if i == 0:
        web.close()
    web.switch_to.window(web.window_handles[i])
    time.sleep(1)
    targetClassType = input("输入数字编号：\n[2]英语\n[3]体育\n[4]文化素质核心\n[5]创新研修\n[6]创新实验\n[7]创新创业\n[8]未来技术学院课程\n")
    web.find_elements(By.CLASS_NAME, 'navi_title')[4].click()
    time.sleep(1)

    web.find_element(By.XPATH, '//*[@id="tabs_container"]/div/span[5]/p[' + targetClassType + ']').click()
    time.sleep(1)
    web.switch_to.frame(0)
    web.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/form/ul/li[5]/div').click()
    time.sleep(1)
    classNum = int(input('目标课序号\n'))
    page = int((classNum - classNum % 20) / 20 + 1)
    shiftPage = page != 1
    pageXPath = '/html/body/div[7]/div/div[7]/ul/li[' + str(int(page + 2)) + ']'
    classXPath = '/html/body/div[7]/div/div[6]/table/tbody/tr[' + str(int(classNum % 20 + 1)) + ']/td[1]/div'
    tabConfigs.append(TabConfig(shiftPage, classXPath, pageXPath, web.window_handles[i]))

print("自动抢课已开始，如需停止，请关闭窗口，或者杀死此进程")
print("请在自行打开另一个窗口检查是否抢课成功")
print("请勿在自动打开的窗口中进行任何操作")
print("本程序不保证抢课成功，如需保证，请同时自行手动抢课")

excepted = False
while True:
    try:
        for each in tabConfigs:
            web.switch_to.window(each.handle)
            web.switch_to.frame(0)
            web.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/form/ul/li[5]/div').click()
            time.sleep(0.01)
            if each.shiftPage:
                web.find_element(By.XPATH, each.pageXPath).click()
            web.find_element(By.XPATH, each.classXPath).click()
            web.find_element(By.XPATH, each.classXPath).click()
            web.find_element(By.XPATH, each.classXPath).click()
    except:
        if not excepted:
            print("出错了，可能是网络问题，也可能是抢课成功了，或者是其他原因，但程序不会停止，继续抢课")
            excepted = True
