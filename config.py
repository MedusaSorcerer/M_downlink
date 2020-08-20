#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

# 配置下载的文件保存的文件夹位置, 需要注意：需要写入绝对的文件路径
DOWNLOAD = r'F:\downblog\blog'

# 保存了你需要下载到本地的地址, 如 https://juejin.im/user/2805609406139950
# 一行是一个地址, 可配置多行地址, 并忽觉空行
LINK_FILE = r'./m_links.txt'

# 如你的默认输入法是中文, 需要指定 True 来切换输入法, 如果是英文, 则使用 False
SHIFT = True

# 启动服务的 Debug 模式, True 和 False 任选
DEBUG = False

# 启动服务的绑定地址, 如使用 "127.0.0.1" 仅当前主机访问, "0.0.0.0" 当前局域网内可访问
HOST = '0.0.0.0'

# 启动服务的绑定端口号
PORT = 8009

# 下载目录的首个命名数字, 往后依次 +1
NUMBER = 1

# 操作滚动条的最大次数
SCROLL_MAX = 5

# 单次操作滚动条的距离, 单位 px(像素)
SCROLL_MOVE = 700
