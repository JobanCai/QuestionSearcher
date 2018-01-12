import requests
import json
import log_utils


def get_chongding_by_api():
    api_url = 'http://htpmsg.jiecaojingxuan.com/msg/current'
    # api_url = 'http://192.168.152.58:8080/1'  
    req = requests.get(url=api_url)
    msg = u''
    while msg != u"成功":
        req = requests.get(url=api_url)
        try:
            msg = json.loads(req.text)['msg']
        except BaseException:
            log_utils.debug("所获取JSON异常%s" % req.text)
            msg = u''
    log_utils.info("获取JSON成功")
    event = json.loads(req.text)['data']['event']
    question = event['desc']
    answerStr = event['options']
    answerStr = answerStr.replace("\"", "")
    answerStr = answerStr.replace("[", "")
    answerStr = answerStr.replace("]", "")
    answer = answerStr.split(",")

    if question[1] == '.':
        question = question[2:]
    else:
        question = question[3:]
    return question, answer


if __name__ == '__main__':
    get_chongding_by_api()
