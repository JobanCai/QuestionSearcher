import web
import codecs
import random

urls = (
    '/(.*)', 'hello'
)

app = web.application(urls, globals())


class hello:
    json_list = {
        1: '1515762118.json',
        2: '1515762154.json',
        3: '1515762168.json',
        4: '1515762221.json',
        5: '1515762269.json',
        6: '1515762320.json',
        8: '1515762395.json',
        9: '1515762406.json',
        10: '1515762432.json',
        11: '1515762537.json',
        12: '1515762559.json',
        13: '1515762614.json',
        14: '1515762673.json',
        15: '1515762765.json',
        7: '1515762471.json'
    }

    def GET(self, name):
        if not name:
            json = 'not JSON!'
        else:
            f = codecs.open("../test_data/json/%s" % self.json_list[random.randint(1, 16)], "r", "utf-8")
            json = f.read()
            f.close()
        return json


if __name__ == "__main__":
    app.run()
