#!/usr/bin/python3
import sys
import os
import datetime

def print_expected_args():
    script_name = os.path.basename(__file__)
    print(f'syntax: {script_name} <output_nt_file> <size_1>')

if len(sys.argv) < 3:
    print_expected_args()
    exit(1)
    
output_filename = sys.argv[1]
size_1 = int(sys.argv[2])

print(f'size_1: {size_1}')

def generate_file(output_file, size_1):
    var_1_value_fun = lambda num: f'<var_1_value_{num}>'
    # var_5_value_fun = lambda num: f'<var_5_value_{num}>' no data with ?var5
    var_4_value_fun = lambda num: f'<var_4_value_{num}>'
    var_3_value_fun = lambda num: f'<var_3_value_{num}>'
    
    dt = '<http://www.w3.org/2001/XMLSchema#dateTime>'
    now = datetime.datetime.utcnow()
    thirty_five_days_ago = now - datetime.timedelta(days=35)
    days_ago_literal = f'"{thirty_five_days_ago.isoformat()}"^^{dt}'

    birth_date = f'"{datetime.datetime(year=1960, month=1, day=1).isoformat()}"^^{dt}'

    statements = '<http://wikiba.se/ontology#statements>'
    sitelinks = '<http://wikiba.se/ontology#sitelinks>'

    p569 = '<http://www.wikidata.org/prop/direct/P569>'
    p570 = '<http://www.wikidata.org/prop/direct/P570>'
    p31 = '<http://www.wikidata.org/prop/direct/P31>'
    # p1196 = '<http://www.wikidata.org/prop/direct/P1196>' used for ?var5
    q5 = '<http://www.wikidata.org/entity/Q5>'

    def add_without_v5(num):
        var1_value = var_1_value_fun(num)
        output_file.write(f'{var1_value} {p570} {days_ago_literal} .\n')
        output_file.write(f'{var1_value} {p31} {q5} .\n')
        output_file.write(f'{var1_value} {p569} {birth_date} .\n')
        output_file.write(f'{var1_value} {statements} {var_3_value_fun(num)} .\n')
        output_file.write(f'{var1_value} {sitelinks} {var_4_value_fun(num)} .\n')


    for i in range(0, size_1):
        add_without_v5(i)

    
        
with open(output_filename, 'w') as f:
    generate_file(f, size_1)
