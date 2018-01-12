from lxml import etree
import codecs

f = codecs.open("./test_data/index.html", "r", "utf-8")
content = f.read()
f.close()
# print(content)
tree = etree.HTML(content)
nodes = tree.xpath(
    "/html/body/div[@id='wrapper']/div[@id='wrapper_wrapper']/div[@id='container']/div[@id='content_left']/div[@id<100]")
for node in nodes:
    print(etree.tostring(node))

