from lxml import etree
import codecs
import webbrowser
import requests

BAIDU_BASE = 'http://www.baidu.com/s'
BING_BASE = 'http://cn.bing.com/'


def open_browser(url):
    webbrowser.open(url)


def get_lines(keywordlist):
    lines = ''
    for key in keywordlist:
        lines = lines + key + ' '
    return lines


def get_baidu_header(keywordlist):
    return BAIDU_BASE, {'wd': get_lines(keywordlist)}


def get_bing_header(keywordlist):
    return BING_BASE, {'q': get_lines(keywordlist)}


def request_keywords(keywordlist, engine):
    if engine == 'baidu':
        url, params = get_baidu_header(keywordlist)
    elif engine == 'bing':
        url, params = get_bing_header(keywordlist)
    else:
        url, params = get_baidu_header(keywordlist)
    req = requests.get(url=url, params=params)
    body = req.text
    return body


def segment_html(html_text):
    # f = codecs.open("./test_data/index.html", "r", "utf-8")
    # content = f.read()
    # f.close()
    # print(content)
    tree = etree.HTML(html_text)
    nodes = tree.xpath(
        "/html/body/div[@id='wrapper']/div[@id='wrapper_wrapper']/div[@id='container']/div[@id='content_left']/div[@id<100]")
    return nodes
