'''
Created on 2018年6月28日

@author: dha
'''
import math

import jieba


def docs(w, D):
    '''
    计算词引用数
    '''
    c = 0
    for d in D:
        if w in d:
            c = c + 1;
    return c


def seg(content, stopwords):
    '''
    分词并去除停用词
    '''
    segs = jieba.cut(content)
    segs = [w for w in list(segs)]  # 特别注意此处转换
 
    seg_set = set(set(segs) - set(stopwords))
    return seg_set


def compute_idf(contents, stopwords):
    '''
    计算内容列表的idf
    '''
    # 所有分词后文档
    D = []
    # 所有词的set
    W = set()
    for i in range(len(contents)):
        # 新闻原始数据
        d = seg(contents[i], stopwords)
        D.append(d)
        W = W | d
    # 计算idf
    idf_dict = {}
    n = len(W)
    # idf = log(n / docs(w, D))
    for w in list(W):
        if len(w.strip()) > 0:
            idf = math.log(n * 1.0 / docs(w, D))
            idf_dict[w] = idf
    return idf_dict


def save(idf_dict, path):
    '''
    保存udf文件
    '''
    
    sorted_idfs = sorted(idf_dict.items(), key=lambda d: d[1])
    f = open(path, "a+", encoding='utf-8')
    f.truncate()
    # write_list = []
    for idf in sorted_idfs:
        f.write(str(idf[0]) + " " + str(idf[1]) + "\n")
    f.close()
