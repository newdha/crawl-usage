# -*- coding: utf-8 -*-

'''
Created on 2018年6月27日

@author: dha
'''

import argparse
import csv

import utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='生成idf文件')
    parser.add_argument('input_file', help='Input file', metavar='<inputfile>')
    parser.add_argument('output_file', help='Output file', metavar='<outputfile>')
    parser.add_argument('-sw', '--stopwords', dest='stop_words_file', help='Stop words file', metavar='<file>')
    args = parser.parse_args()
     
    input_file = args.input_file
    output_file = args.output_file
    stop_words_file = args.stop_words_file
    stop_words = {}
      
    if stop_words_file:
        stop_words = stop_words.fromkeys([ line.rstrip() for line in open(stop_words_file, encoding='utf-8') ])
      
    contents = []
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            comment = row['content'] + '。' + row['after_user_comment']
            contents.append(comment)
    idf = utils.compute_idf(contents, stop_words)
    utils.save(idf, output_file)
