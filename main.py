import problem_util, web_util, algo_util


def show_problem(problem, options):
    print('Prob:%s' % problem)
    count = 1
    for opt in options:
        print('%d:%s' % (count, opt))
        count = count + 1


def show_anwser(result):
    print('Recommend:%s' % result[0][0])
    print('Answer\t--\tWeight')
    for i, r in enumerate(result):
        print('%s\t--\t%.6f' % (r[0], r[1]))


def main():
    problem, options = problem_util.get_chongding_by_api()
    show_problem(problem, options)
    web_util.open_browser(web_util.BAIDU_BASE + '?wd=' + problem)
    tags = algo_util.extract_tags(problem)
    context = web_util.request_keywords(tags, 'baidu')
    respones = web_util.segment_html(context)
    result = algo_util.get_answer(options, respones)
    show_anwser(result)


if __name__ == '__main__':
    main()
