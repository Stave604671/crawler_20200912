# crawler_20200912
Go to waterfall flow type sites to get a bunch of pictures
首先，使用这个爬虫你需要能拿到Robots协议的许可。
接下来需要根据这个网站的具体结构来设置爬虫的结构
第一层函数：
    功能：读取你需要爬取的那一批图片的名称，并将这一批名称存储到列表里
    备注：这里需要使用pandas库来处理这种存储到表格里的数据，如果你要爬取的内容是以其他形式存储的，就需要使用类似的方法将这一批名称存储到列表里。
第二层函数：
    功能：根据第一步获取到的列表，遍历这个列表，然后根据列表的内容（你要爬取的内容）在指定路径下创建一批文件夹
    备注：这样做的目的是为了方便给每一张图片制作标签，根据图片的内容来创建了一批文件夹以后，后面制作标签的时候，可以通过读取图片所属的文件夹的形式来制作对应的标签。
第三层函数：
    功能：根据你的需求，需要爬取瀑布流页面里面的几页的图片，需要爬取的图片的关键字是什么，根据这两个需求将图片的下载链接从网页的结构中提取出来。
    备注：这里一般跟网页中的javascript结构有关，需要通过分析内部结构找到图片的存储路径。至于分析结构的方法就需要一部分HTML语言的基础，然后打开浏览器的开发者模式找到你要获取的内容。
第四层函数：
    功能：根据第二层函数创建的文件夹的路径，将第三层函数提取到的图片的内容存储到指定路径里。
第五层函数：
    功能：根据图片的路径（需要带上文件名那种）在指定路径下创建指定的json格式的文件
