# coding=utf-8
import os
import pandas as pd
import requests
import json

# 添加请求头伪装成浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
    "referer": ""   # 这里输入网站链接
}
# 步骤：从excel表格中将要爬的内容读取为列表-》根据列表制作文件夹
# 读取列表中的两列，一列英文用于存入指定文件夹，一列中文用于检索

#  读取一列列名
def excel_one_list():
    df = pd.read_excel("h.xls", usecols=[1],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    return result

#  读取两列
def excel_two_list():
    df = pd.read_excel("herb.xls", usecols=[0, 1],
                       names=None)  # 读取项目名称和行业领域两列，并不要列名
    df_li = df.values.tolist()
    return df_li

#  根据keyword创建一批文件夹，英文路径是为了方便制作标签
def input_and_output(keyword):
    last_dir = "D://images3//"
    dir = "D://images3//" + keyword
    # 判断images3文件夹是否存在
    if os.path.exists(last_dir):
        if os.path.exists(dir):
            print("文件夹已经存在")
        else:
            os.mkdir(dir)
            print(dir + "已经创建成功")
    else:
        os.mkdir(last_dir)
        if os.path.exists(dir):
            print("文件夹已经存在")
        else:
            os.mkdir(dir)
            print(dir + "已经创建成功")


def getPages(keyword, pages):
    keyword = keyword+'中药'
    params = []
    for i in range(30, 30 * pages + 30, 30):
        params.append({
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': 201326592,
            'is': '',
            'fp': 'result',
            'queryWord': keyword,
            'cl': 2,
            'lm': -1,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': -1,
            'z': '',
            'ic': 0,
            'word': keyword,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': 2,
            'qc': '',
            'nc': 1,
            'fr': '',
            'pn': i,
            'rn': 30,
            'gsm': '1e',
            '1488942260214': ''
        })
    url = '输入网站链接/search/acjson'
    urls = []
    s = requests.session()
    s.headers = headers
    a = ''
    for i in params:
        try:
            a = s.get(url, params=i).json(strict=False).get('data')
        except:
            pass
        urls.append(a)
    return urls



# keyword用于写入指定路径
def get_herb(keyword, dataList):
    try:
        x = 0
        for lists in dataList:
            for i in lists:
                if i.get('thumbURL') is not None:
                    print('正在下载：%s' % i.get('thumbURL'))
                    ir = requests.get(i.get('thumbURL'))
                    open('/图片路径/images3/' + keyword + '/%d.jpg' % x, 'wb').write(ir.content)
                    x += 1
        print('图片下载完成')
    except Exception as e:
        print("图片下载失败", e)


# 对指定路径的图片打标签
def labels(file_dir):
    json_text = {'labels': []}
    for files in os.listdir(file_dir):
        json_text['labels'].append({'name': files})
        json_data = json.dumps(json_text)
        print(json_data)
        for fileses in os.listdir(file_dir + "/" + files + "/"):
            s = fileses[:-4]
            f = open(file_dir + "/" + files + "/" + s + ".json", 'w')
            f.write(json_data)
            f.close()
        json_text['labels'].remove({'name': files})

# 新建一批文件夹
# result_b = excel_one_list()
# for i in result_b:
#     input_and_output(i)


# 读取中文列和英文列用于爬虫
result_a = excel_two_list()
print(result_a)
r = 0
for i in result_a:
    r = r + 1
    if r == 10:     # 设置起点
        s = getPages(i[0], 3)
        get_herb(i[1], s)
        print('第', a, '种图片'+i[1]+'下载完毕')
    if r == 15:     # 设置终点
        break
