import requests
import json


def get_chongding_by_api():
    # api_url = 'http://localhost/test.php'
    api_url = 'http://htpmsg.jiecaojingxuan.com/msg/current'
    req = requests.get(url=api_url)
    while (json.loads(req.text)['msg'] != u"成功"):
        req = requests.get(url=api_url)
    event = json.loads(req.text)['data']['event']
    question = event['desc'];
    answerStr = event['options']
    answerStr = answerStr.replace("\\\"", "")
    answerStr = answerStr.replace("[", "")
    answerStr = answerStr.replace("]", "")
    answer = answerStr.split(",")

    result = []
    result.append(question)
    result.append(answer)
    return result


if __name__ == '__main__':
    get_chongding_by_api()
