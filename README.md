# !请勿外传

## 简介
HITWH抢课。只能解决手速问题，不能解决网速问题，不排除失败可能。
本脚本不对抢课结果负责，use at your own risk.

## 逆向相关信息
新教务系统含一个frame，该frame展示导航栏内容。在选课节目的frame上，有一个saveXsxk方法，接受课程代码并提交选课表单。虽然课程代码只有在选课时会暴露在选课button上，但是选科人数也是通过课程代码查询的，从选科人数的input中可以得到课程代码。

## 环境配置
1. 安装[python解释器](https://www.python.org)，本脚本开发时使用3.10版本。
2. 以管理员身份打开终端，安装selenium包及其依赖 `$ pip install selenium`。
3. 下载chrome driver并将其添加到环境变量，安装chrome浏览器。
4. 运行get\_class.py脚本

## 下载链接
1. chrome浏览器: https://www.google.cn/intl/zh-CN/chrome/
2. chromedriver(windows): https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.52/
3. chromedriver(macOS apple silicon): https://chromedriver.storage.googleapis.com/105.0.5195.52/chromedriver\_mac64\_m1.zip
4. chromedriver(全部版本): https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.52/
5. 环境变量配置:
	- windows: https://ceshiren.com/t/topic/21687
	- macOS: https://www.cnblogs.com/CMbenten/p/16550193.html
	- linux: 同mac，但是真的有linux用户不会处理环境变量?
