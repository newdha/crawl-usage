# -*- coding: utf-8 -*-

'''
Created on 2018年6月27日

@author: dha
'''

import argparse
import csv

import jieba

import utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='按idf之和重新排序')
    parser.add_argument('input_file', help='Input file', metavar='<inputfile>')
    parser.add_argument('output_file', help='Output file', metavar='<outputfile>')
    parser.add_argument('-sw', '--stopwords', dest='stop_words_file', help='Stop words file', metavar='<file>')
    parser.add_argument('-idf', '--idffile', dest='idf_file', help='IDF file', metavar='<file>')
    args = parser.parse_args()
     
    input_file = args.input_file
    output_file = args.output_file
    
    stop_words_file = args.stop_words_file
    stop_words = []
    if stop_words_file:
        stop_words = utils.read_lines(stop_words_file)
    
    idf_file = args.idf_file    
    idfs = {}
    if idf_file:
        idfs = utils.read_pairs(idf_file, float)
    
    scored_rows = []
    field_names = []
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        field_names = reader.fieldnames
        for row in reader:
            content = row['content']
            if 'after_user_comment' in row and len(row['after_user_comment']) > 0:
                content = content + '。' + row['after_user_comment']
            if 'answer_content' in row and len(row['answer_content']) > 0:
                content = content + '。' + row['answer_content']
            
            words = jieba.cut(content)
            words_set = set()
            for word in words:
                word = word.strip()
                if word not in stop_words:  
                    if word != '\t':  
                        words_set.add(word)
            scores = [idfs[word] for word in words_set]
            scored_rows.append((row, sum(scores)))
            
    sorted_rows = sorted(scored_rows, key=lambda d: d[1], reverse=True)
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, field_names, delimiter=',')
        writer.writeheader()
        for row in sorted_rows:
            writer.writerow(row[0])
