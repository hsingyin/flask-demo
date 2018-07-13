# coding: utf-8
from flask import render_template, flash, redirect,request,url_for,current_app
import os 
# os.chdir(r'D:\作业\小学期Python\nlp\NLP\resource\learning_nlp\chapter-8\classification')

import numpy as np
from sklearn.cross_validation import train_test_split
import numpy as np
import jieba
from app import app
from .normalization import normalize_corpus
from sklearn.externals import joblib
# from feature_extractors import bow_extractor, tfidf_extractor
from collections import Counter

def get_data(uploadpath):
    '''
    获取数据
    :return: 文本数据，对应的labels
    '''
    # ../static/lib/normal.txt
#    d:\Data\py\flask\app\../uploads/files\normal.txt
    with open(uploadpath, encoding="utf8") as ham_f:
        ham_data = ham_f.readlines()
    return ham_data

def remove_empty_docs(corpus):
    filtered_corpus = []
    for doc in corpus:
        if doc.strip():
            filtered_corpus.append(doc)
    return filtered_corpus

def mainAnalysis(uploadpath):
    
    
    # mlp = joblib.load( 'app/static/lib/tdidf_mlp.model')
    mlp = joblib.load( 'app/static/lib/name.model')
    # tfidf_vectorizer = joblib.load( 'app/static/lib/tfidf_vectorizer_mlp.model')
    tfidf_vectorizer = joblib.load( 'app/static/lib/vectorizer_name.model')
    corpus = get_data(uploadpath)
    #print("total datasets:", len(corpus))
    corpus = remove_empty_docs(corpus)
    #print("corpus 0 is ", corpus[0])

    #print (len(corpus))
    norm_train_corpus = normalize_corpus(corpus)

    train_messages = []
    for i in range(len(norm_train_corpus)):
        seg_list = jieba.cut(norm_train_corpus[i], cut_all=False)
        train_messages.append(','.join(seg_list))
    #print (len(train_messages))

    
    tfidf_train_features = tfidf_vectorizer.transform(train_messages)

    #print(tfidf_train_features[0])
    

    predictions = mlp.predict(tfidf_train_features)

    # c = Counter(predictions)
    # for word_freq in c.most_common(2):
    #     word, freq = word_freq
    #     if word == 1:
    #         print (freq /  len(corpus))
    # #     print (word,freq)    
    
    print(predictions.tolist())
    return predictions.tolist()
    
# if __name__ == "__main__":
#     mainAnalysis(uploadpath)
   

