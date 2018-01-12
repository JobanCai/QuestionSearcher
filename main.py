import time
import problem_util, web_util, algo_util


def show_problem(problem, options):
    print('Prob:%s' % problem)
    count = 1
    for opt in options:
        print('%d:%s' % (count, opt))
        count = count + 1


def show_anwser(result, engine):
    print('Search Engine:%s\tRecommend:%s' % (engine, result[0][0]))
    print('Answer\t--\tWeight')
    for i, r in enumerate(result):
        print('%s\t--\t%.6f' % (r[0], r[1]))


def main():
    engines = ['baidu', 'bing'] 

    problem, options = problem_util.get_chongding_by_api()
    last = time.time()
    show_problem(problem, options)

    url = web_util.BAIDU_BASE + '?wd=%s' % problem
    web_util.open_browser(url)
    
    tags = algo_util.extract_tags(problem)
    keys = ''
    for t in tags:
        keys = keys + t + ' '
    print(keys)

    for e in engines:
        context = web_util.request_keywords(tags, e)
        
        respones = web_util.segment_html(context, e)
        result = algo_util.get_answer(options, respones)
        show_anwser(result, e)
    print('cost:%fs' % (time.time() - last))

if __name__ == '__main__':
    main()
