import web
import codecs

urls = (
    '/(.*)', 'hello'
)

app = web.application(urls, globals())


class hello:
    json_list = {
        '1': '1515761747.json',
        '2': '1515761761.json',
        '3': '1515762118.json',
        '4': '1515762154.json',
        '5': '1515762168.json',
        '6': '1515762210.json'
    }

    def GET(self, name):
        if not name:
            json = 'not JSON!'
        else:
            f = codecs.open("../test_data/json/%s" % self.json_list[name], "r", "utf-8")
            json = f.read()
            f.close()
        print(json)

        return json


if __name__ == "__main__":
    app.run()
