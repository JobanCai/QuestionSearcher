import problem, web_util, algo

def main():
  problem,  = problem.get_chongding_by_api()
  web_util.open_browser(web_util.BAIDU_BASE + '?wd=' + problem)
  tags = algo.extract_tags(problem)
  context = web_util.request_keywords(tags, 'baidu')
  respones = web_util.segment_html(context)
  

if __name__ == '__main__':
  main()