import problem, web, algo

def main():
  problem,  = problem.get_chongding_by_api()
  web.open_browser(web.BAIDU_BASE + '?wd=' + problem)
  tags = algo.extract_tags(problem)
  context = web.request_keywords(tags, 'baidu')
  respones = web.segment_html(context)
  

if __name__ == '__main__':
  main()