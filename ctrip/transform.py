# -*- coding: utf-8 -*-

'''
Created on 2018年6月27日

@author: dha
'''

import argparse
import csv

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='转换csv使价格可读')
    parser.add_argument('input_file', help='Input file', metavar='<inputfile>')
    parser.add_argument('output_file', help='Output file', metavar='<outputfile>')
    args = parser.parse_args()
     
    input_file = args.input_file
    output_file = args.output_file
    
    dates = set()
    rows = {}
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            dates.add(row['date'])
            hotel_id = row['id']
            if hotel_id not in rows:
                rows[hotel_id] = {
                    "city_name":row['city_name'],
                    "name": row['name'],
                    "url":row['url'],
                    "score":row['score'],
                    "dpcount":row['dpcount']
                }
            rows[hotel_id][row['date']] = row['lowest_price']
        
    field_names = ['city_name', 'name', 'url', 'score', 'dpcount'] + sorted(dates)
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, field_names, delimiter=',')
        writer.writeheader()
        for row in rows.values():
            writer.writerow(row)
