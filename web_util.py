from lxml import etree
import codecs
import re
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


def segment_html(html_text, engine):
    # f = codecs.open("./test_data/index.html", "r", "utf-8")
    # html_text = f.read()
    # f.close()
    def get_string_from_node(node):
        node = etree.tostring(node, encoding="UTF-8", xml_declaration=False)
        node = str(node, encoding='utf-8')
        dr = re.compile(r'<[^>]+>', re.S)
        node = dr.sub('', node)
        return node

    n = []
    tree = etree.HTML(html_text)
    if engine == 'baidu':
        nodes = tree.xpath(
            "/html/body/div[@id='wrapper']/div[@id='wrapper_wrapper']/div[@id='container']/div[@id='content_left']/div[@id<100]/div[@class='c-abstract']")
        for node in nodes:
            # node = node.xpath("//div[@class='c-abstract']")
            node = get_string_from_node(node)
            n.append(node)
    else:
        path = "/html/body/div[@id='b_content']/ol[@id='b_results']/li"
        nodes = tree.xpath(path)
        for node in nodes:
            headers = node.xpath("./h2/a")
            contents = node.xpath("./div[@class='b_caption']/p")
            line = ""
            for h in headers:
                line = line + get_string_from_node(h)
            for c in contents:
                line = line + get_string_from_node(c)
            n.append(line)
    return n


if __name__ == '__main__':
    segment_html("")
