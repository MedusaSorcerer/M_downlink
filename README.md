# M_downlink

```text
 ____    ____                __                              __    _            __       
|_   \  /   _|              |  ]                            [  |  (_)          [  |  _   
  |   \/   |            .--.| |  .--.   _   _   __  _ .--.   | |  __   _ .--.   | | / ]  
  | |\  /| |          / /'`\' |/ .'`\ \[ \ [ \ [  ][ `.-. |  | | [  | [ `.-. |  | '' <   
 _| |_\/_| |_  _______| \__/  || \__. | \ \/\ \/ /  | | | |  | |  | |  | | | |  | |`\ \  
|_____||_____||_______|'.__.;__]'.__.'   \__/\__/  [___||__][___][___][___||__][__|  \_] 
                                                                                         
```

![](https://img.shields.io/badge/python-3.8.2-red?style=for-the-badge&logo=python)
![](https://img.shields.io/badge/flask-1.1.2-red?style=for-the-badge&logo=flask)

[juejin](https://juejin.im/post/6863063060387463175/)

<span style="font-size: 30px; padding: 0 5px 0 30px">起</span>初写的是一个脚本,
是为了将收藏的博客文章等下载到本地收藏,
制定了一个目录文件便于查阅,
后来就优化了相关内容后,
就发布到 Github 给大家使用了,
当然,
依赖的语言是 `Python` 脚本,
为了方便,
我也会打包成一个 `exe` 可执行文件,
方便那些没有环境的使用者来使用。

而下载到本地的一些博客大多是自己觉得值得收藏的干货,
或者是一些写的好的文章等等,
而收藏链接的好处是空间节约以及方便,
而坏处就是某一天访问的时候出现了 `404` 或者 `该内容不存在` 等字样,
就说明这个文章可能被作者删除了。

成品示例：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24708d164cbf43c989ad1cc59c31394c~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfab2f239ba4440788991f5fde495690~tplv-k3u1fbpfcp-zoom-1.image)

## 项目文件说明
基本构造由下面几个文件组成：

* `m_downlink.py` 下载网页的主要运行文件, 你也可以指定相关参数
* `config.py` 配置一些参数的配置文件
* `m_service.py` 将下载目录文件所谓服务器进行访问的服务启动文件
* `chromedriver.exe` selenium 调用的 Chrome 插件

### config.py
优先介绍一下配置的内容,
打开配置文件 `config.py` 后有这几个配置参数：
```python
# 配置下载的文件保存的文件夹位置, 需要注意：需要写入绝对的文件路径
DOWNLOAD = r'C:\Users\Administrator\Desktop\xxx'

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
```
注意 `DOWNLOAD` 参数需要的是绝对路径,
并不是相对路径。

### m_downlink.py
这是主要的运行文件,
功能是：

* 下载路径的网页内容
* 优化图片展示问题
* 写入目录文件

原理是使用 selenium 操作 chromedriver 使用键盘操作的方式进行下载,
并写入以数字命名的文件夹中,
并对图片展示进行优先缓存,
再对所有下载任务完成后写入路径到目录文件 `links.html` 中。

基本的使用是,
在配置文件完善的情况下直接运行：
```shell
python3 m_downlink.py
```
当然了,
对于特殊需求的情况下,
利用 `python` 的逻辑判断,
写了以下几个参数：
```text
-t 测试组件运行是否正常
-d 下载指定 LINK_FILE 中的链接保存到 DOWNLOAD 目录下
-w 将 DOWNLOAD 目录下的文件生成文件静态目录文件 links.html
-f [number or number:bumber] 查找指定索引位置的链接数据，或者将数据作为下载输入内容
-n [number] 指定下载目录名称的起始数字
```
如测试 chromedriver 是否运行正常：
```shell
python3 m_downlink.py -t
```
只需要下载即可,
暂不生成目录文件：
```shell
python3 m_downlink.py -d
```
对已经下载好的链接文件生成目录：
```shell
python3 m_downlink.py -w
```
配置文件的 `NUMBER` 和 `-n` 参数都是一样的,
后者的优先级高于前者,
如果想把文件夹命名从 `100` 开始,
即可使用 `-n 100` 参数, 文件夹名即 `0100`：
```shell
python3 m_downlink.py -n 100
```
如果是在配置的 `LINK_FILE` 文件中有 100 个链接地址,
此时我不需要全部下载,
仅需要下载一部分,
你可以使用 `-f xx` 来指定范围：
```shell
# 只下载第四个链接
python3 m_downlink.py -f 4 -d

# 下载第五至第五十五个链接
python3 m_downlink.py -f 5:55 -d

# 下载从第五十五个开始的链接
python3 m_downlink.py -f 5:999 -d
```
<span style="color: red">
  注意：脚本启动后不要操作鼠标,
  使其失去光标,
  否则下载可能会遇到错误,
  下载时默认会操作滚动条移动最大 <code>SCROLL_MAX 乘 SCROLL_MOVE</code> 个像素,
  若在最大值之后还未移动至底部：<br>
  ① 如果图片加载对于你并不重要,
  可以直接按 <code>1</code> 来继续进行操作<br>
  ② 如果你需要图片加载,
  你可以手动操作鼠标来滚动至需要的高度后按 <code>1</code> 继续工作
</span>

这里使用了手动操作的方式是为了解决如掘金文章,
你所查阅的文章底部再往下滑动,
会出现很多推荐内容,
并且是局部刷新的,
可以滑动很多内容,
这儿并不能对文字做精确的预判,
并且推荐的也不是我想保存的,
所以采用了人为客观的做一次判断处理。

运行时完成后有以下字样,
按照提示操作即可：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fce358fa8954443b85415936465656f6~tplv-k3u1fbpfcp-zoom-1.image)

### m_service.py
这个文件主要是使用 `flask` 来提供 web 服务的,
寥寥几行代码,
直接运行即可,
不需要配置参数：
```shell
python3 m_service.py
```
启动完成后,
你可以使用 `127.0.0.1` 加上你的端口来访问,
就像这样：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a22252cd3cfb44aea33ce96087b11a14~tplv-k3u1fbpfcp-zoom-1.image)

### m_links.txt
这个文件是在配置文件中 `LINK_FILE` 指定的文件,
内容是你需要下载的链接地址,
譬如：
```url
https://juejin.im/post/6859632848761651213
https://juejin.im/post/6859625125365415949
...
```
你可以任意命名该文件,
只需要在 `config.py` 的 `LINK_FILE` 指定它就可以。

## 无 Python 环境运行
项目还包含有打包 windows 可执行文件 `.exe` 运行文件,
所以这意味着你可以没有 `Python` 运行环境就可以使用这个项目,
项目的打包文件就在 `lib` 文件夹中,
你可以在这个里面找到
<img style="overflow:hidden; margin: 0px 0 -6px 0;" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24bc577e790e43308eff23c59116505c~tplv-k3u1fbpfcp-zoom-1.image">
和
<img style="overflow:hidden; margin: 0px 0 -6px 0;" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ef02429f3cc4fdda285a67525f49c13~tplv-k3u1fbpfcp-zoom-1.image">
两个文件,
运行方法和 `.py` 大致一样,
你可以使用参数,
不同的是,
在不使用参数的情况下,
你可以直接双击 `.exe` 文件开始使用,
如果在使用的时候想指定参数,
你需要在你的 `bin` 文件目录下,
点击目录窗口,
键入 `cmd` 并 回车(Enter),
打开终端黑窗口：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69e35cc18aa04c3a8d0e7c22bdc5dcbb~tplv-k3u1fbpfcp-zoom-1.image)

在使用：
```shell
downlink.exe -t
downlink.exe -n 100 -d
```
相同的 `service.exe` 也可以使用终端启动：
```shell
service.exe
```

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/708c9af6d711423c9851e229a8a716e6~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae0272c2c05a4e01809805ddddd86e9d~tplv-k3u1fbpfcp-zoom-1.image)

允许访问即可。

## 下载
如果你是一个拥有 `python` 环境的使用者,
建议你直接下载 `m_downlink.zip` 文件,
其中仅包含 `lib` 以外的文件,
因为打包文件大小约 `88MB`,
下载速度较慢,
也对你的使用没有任何作用,
如果你没有环境的支持,
建议你下载项目 `.zip`。

## 本地文件说明
你的网页下载到本地后将会有两个 `.html` 文件,

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94fc3919d6c040be982a3da5b8a4c75c~tplv-k3u1fbpfcp-zoom-1.image)

文件夹是网页的一些依赖静态资源,
红色的 `.html` 是下载的界面原网页,
绿色的 `M_index.html` 是优化后的界面网页。