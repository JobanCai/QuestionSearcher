import jieba
import jieba.analyse

jieba.initialize()

def cut_word(sentence):
  result = jieba.cut(sentence)
  return result

def extract_tags(sentence):
  result = jieba.analyse.extract_tags(sentence, topK=5, withWeight=True, allowPOS=())
  return result



def test():
  question = '扑克牌中黑桃Q的人物原型是谁？'
  result = extract_tags(question)
  keywords = []
  for r in result:
    keywords.append(r[0])
  return keywords

if __name__ == '__main__':
  test()