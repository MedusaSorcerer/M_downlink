#!/usr/bin/env python
# _*_ Coding: UTF-8 _*_
import os
import shutil
import sys
import time
from _thread import start_new_thread

import pyautogui
import pyperclip
from bs4 import BeautifulSoup
from pynput.keyboard import Listener
from selenium import webdriver

try:
    from .config import *
except ImportError:
    from config import *

F = False
N = NUMBER
THREAD = True
pyautogui.FAILSAFE = True


def write_html():
    paths = list()
    for root, dirs, files in os.walk(DOWNLOAD):
        for i in dirs:
            for _root, _dirs, _files in os.walk(os.path.join(root, i)):
                if _files:
                    try:
                        _files.remove('m_index.html')
                    except ValueError:
                        ...
                    try:
                        paths.append([i, _files[0]])
                    except IndexError:
                        print(i)
                        return
                break
        break
    a = ''
    for i in paths:
        title = i[1][:-5]
        a += fr"""<div class="link"><a href="{i[0]}/m_index.html" target="_blank" onmousemove="goin(this)" onmouseout="gout()">{i[0]} {title}</a></div>"""
        a += '\n'
    with open(os.path.join(DOWNLOAD, 'links.html'), 'w', encoding='UTF-8') as f:
        f.write(header() + a + finish())
        f.close()


def download():
    def _press(key):
        try:
            if key.char == '1':
                listener.stop()
        except AttributeError:
            ...

    global N, driver
    driver = webdriver.Chrome('chromedriver.exe', options=ops)
    for i in links:
        if not i: continue
        driver.get(i)
        time.sleep(1)
        scroll_height = None
        move = 0
        while 1:
            driver.execute_script(f"window.scrollBy (0,{SCROLL_MOVE});")
            _scroll_height = driver.execute_script('return document.documentElement.scrollTop || document.body.scrollTop;')
            time.sleep(.5)
            move += 1
            if _scroll_height == scroll_height: break
            if move >= SCROLL_MAX:
                with Listener(on_press=_press) as listener:
                    listener.join()
                break
            scroll_height = _scroll_height
        time.sleep(1)
        driver.execute_script('var q=document.documentElement.scrollTop=0')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(.5)
        if os.path.isdir(os.path.join(DOWNLOAD, str(N).zfill(4))): shutil.rmtree(os.path.join(DOWNLOAD, str(N).zfill(4)), ignore_errors=True)
        os.mkdir(os.path.join(DOWNLOAD, str(N).zfill(4)))
        time.sleep(1)
        pyperclip.copy(DOWNLOAD)
        pyautogui.typewrite([*(['shiftleft'] if SHIFT else []), 'home'])
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(.1)
        pyautogui.typewrite(['\\', *(i for i in str(N).zfill(4)), '\\'])
        N += 1
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.1)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(.1)
        pyautogui.typewrite(['enter'])
        time.sleep(2)
        thread(pyperclip.paste())
    driver.minimize_window()


def thread(download_file):
    def _():
        if os.path.isfile(download_file):
            hf = open(download_file, 'r', encoding='UTF-8')
            html = BeautifulSoup(hf.read(), 'html.parser')
            hf.close()
            for img in html.find_all('img'):
                if img.get('crossOrigin'): del img['crossOrigin']
                if img.get('crossorigin'): del img['crossorigin']
            for js in html.find_all('link') + html.find_all('script'):
                if js.get('href', '').endswith('.js.下载') or js.get('src', '').endswith('.js.下载'): js.extract()
            index = open(os.path.join(download_file, '..', 'm_index.html'), 'w', encoding='UTF-8')
            index.write(str(html))
            index.close()
        time.sleep(1)

    start_new_thread(_, ())


def header():
    return r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Links</title>
    <script>
        function goin(x) {
            let ts = document.getElementById("ts")
            ts.innerHTML = x.innerText;
            ts.style.backgroundColor = "rgba(167,167,167,.9)"
        }

        function gout() {
            let ts = document.getElementById("ts")
            ts.style.backgroundColor = "rgba(0,0,0,0)"
            ts.innerHTML = "";
        }
    </script>
    <style>
        body {
            background: url("https://i.ibb.co/XZ9zt3p/593918ed85e56.png");
            background-size: cover;
        }

        body > div {
            width: 40%;
            background: #e5e5e5;
            margin: 5px 30% 0 30%;
            border-radius: 20px;
            background: -ms-linear-gradient(top, #cacaca, #a2b2ff);
            background: -moz-linear-gradient(top, #cacaca, #a2b2ff);
            background: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#cacaca), to(#a2b2ff));
            background: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#cacaca), to(#a2b2ff));
            background: -webkit-linear-gradient(top, #cacaca, #a2b2ff);
            background: -o-linear-gradient(top, #cacaca, #a2b2ff);
        }

        h1 {
            margin-top: 80px;
        }

        .link {
            padding: 2px 0 2px 10px;
        }

        .link:nth-child(1) {
            padding: 20px 0 2px 10px;
        }

        .link:nth-last-child(1) {
            padding: 2px 0 20px 10px;
        }

        a {
            font-size: 16px;
            display: block;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        a:link {
            color: #005400;
            text-decoration: none;
        }

        a:active {
            color: #005400;
            text-decoration: none;
        }

        a:visited {
            color: #005400;
            text-decoration: none;
        }

        a:hover {
            color: white;
            text-decoration: none;
        }

        #ts {
            height: 40px;
            z-index: 9999;
            position: fixed ! important;
            right: 0;
            top: 0;
            width: 100%;
            margin: 0;
            text-align: center;
            padding-top: 16px;
            font-size: 18px;
            letter-spacing: 2px;
        }

        ::-webkit-scrollbar {
            width: 10px;
            height: 1px;
        }

        ::-webkit-scrollbar-thumb {
            border-radius: 10px;
            background-color: #00b1ff;
            background-image: -webkit-linear-gradient(
                    45deg,
                    rgba(255, 255, 255, 0.5) 25%,
                    transparent 25%,
                    transparent 50%,
                    rgba(255, 255, 255, 0.5) 50%,
                    rgba(255, 255, 255, 0.5) 75%,
                    transparent 75%,
                    transparent
            );
        }

        ::-webkit-scrollbar-track {
            box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
            background: #ededed;
            border-radius: 10px;
        }
    </style>
</head>
<body>
<h1 align="center">保存的链接地址目录</h1>
<div>

    """


def finish():
    return r"""
</div>
<p id="ts">
</p>
<br>
<br>
<br>
<br>
<br>
</body>
</html>    
    """


if __name__ == '__main__':
    """
    help:
        -t 测试组件运行是否正常
        -d 下载指定 LINK_FILE 中的链接保存到 DOWNLOAD 目录下
        -w 将 DOWNLOAD 目录下的文件生成文件静态目录文件 links.html
        -f 查找指定索引位置的链接数据，或者将数据作为下载输入内容
        -n 指定下载目录名称的起始数字
    """
    ops = webdriver.ChromeOptions()
    ops.add_argument('--ignore-certificate-errors')
    argv = sys.argv
    if '-t' in argv[1:]:
        t_driver = webdriver.Chrome('chromedriver.exe', options=ops)
        t_driver.maximize_window()
        t_driver.get('https://www.baidu.com')
        time.sleep(2)
        t_driver.close()
        sys.exit()
    if not os.path.isdir(DOWNLOAD):
        if input(f'没有发现配置的 {DOWNLOAD} 文件夹路径，是否自动创建？ [Y/y]创建 or [other]退出：').upper() == 'Y':
            os.makedirs(DOWNLOAD)
            if not os.path.isdir(DOWNLOAD):
                print(f'创建未成功，请使用手动创建文件夹 {DOWNLOAD}')
                sys.exit()
        else:
            sys.exit()
    if not os.path.isfile(LINK_FILE):
        print(f'未发现网络地址文件：{LINK_FILE}')
        sys.exit()
    with open(LINK_FILE, 'r', encoding='UTF-8') as lf:
        links = lf.readlines()
        lf.close()
    if '-f' in argv[1:]:
        try:
            nu = argv[argv.index('-f') + 1]
            links, N = (links[int(nu.split(':')[0]) - 1:int(nu.split(':')[1])], int(nu.split(':')[0])) if ':' in nu else ([links[int(nu) - 1]], int(nu))
        except (Exception,):
            print('-f 后面你需要接一个数字，或者是用 ":" 连接的两个数字，来指定你的范围')
            sys.exit()
    if '-n' in argv[1:]:
        try:
            N = int(argv[argv.index('-f') + 1])
        except (Exception,):
            print('-n 后面你需要跟随一个数字来指定创建文件夹的名称')
            sys.exit()
    if '-d' in argv[1:] or ('-d' not in argv[1:] and '-w' not in argv[1:]):
        download()
        print('窗口已经最小化，下载任务已全部创建成功 ！')
    if '-w' in argv[1:] or ('-d' not in argv[1:] and '-w' not in argv[1:]):
        if '-d' in argv[1:] or ('-d' not in argv[1:] and '-w' not in argv[1:]):
            input('确认所有下载任务都已完成后，按任意键写入目录文件：')
        write_html()
        print('目录文件写入任务已完成 ！')
    if 'driver' in globals(): driver.close()
    input('确认所有任务进度完成后，按任意键退出程序：')
    sys.exit()
