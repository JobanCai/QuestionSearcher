import jieba
import jieba.analyse
import numpy as np

jieba.initialize()

K = 5

def cut_word(sentence):
    words = jieba.cut(sentence)
    result = []
    for w in words:
        result.append(w)
    return result


def extract_tags(sentence):
    result = jieba.analyse.extract_tags(sentence, topK=K, withWeight=True, allowPOS=())
    keywords = []
    for r in result:
        keywords.append(r[0])
    return keywords


def get_weight(option, page_rank, segments):
    count = 0.0
    for i, seg in enumerate(segments):
        for j, s in enumerate(seg):
            if option in s:
                count = count + page_rank[i]
    return count

def get_weight_list(options, page_rank, segments):
    weights = []
    for i, opt in enumerate(options):
        w = get_weight(opt, page_rank, segments)
        weights.append(w)
    return weights

def get_weight_list_by_n_gram(options, page_rank, segments):
    pass

def get_answer(options, respones):
    page_rank = []
    segments = []
    score = 0.5
    min_score = 0.00001
    for i, res in enumerate(respones):
        page_rank.append(score)
        score = score / 2.0
        if score < min_score:
            score = 1.0 - np.sum(page_rank)
        words = cut_word(res)
        segments.append(words)

    weights = get_weight_list(options, page_rank, segments)

    result = []
    s = np.sum(weights)
    for i, w in enumerate(weights):
        n_w = 0.0
        if s > 0.0:
            n_w = w / s
        result.append((options[i], n_w))

    result.sort(key=lambda x: x[1], reverse=True)
    return result


def test():
    pass


if __name__ == '__main__':
    test()
