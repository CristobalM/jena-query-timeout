#!/usr/bin/python3
import sys
import os

def print_expected_args():
    script_name = os.path.basename(__file__)
    print(f'syntax: {script_name} <output_nt_file> <left_size> <right_size>')

if len(sys.argv) < 4:
    print_expected_args()
    exit(1)
    
output_filename = sys.argv[1]
left_size = int(sys.argv[2])
right_size = int(sys.argv[3])

def generate_file(output_file, left_size, right_size):
    var_1_value_fun = lambda num: f'<var_1_value_{num}>'
    var_2_value_fun = lambda num: f'<var_2_value_{num}>'    
    
    p1889 = '<http://www.wikidata.org/prop/direct/P1889>'
    type_pred = '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>'
    property_pred = '<http://wikiba.se/ontology#Property>'

    for i in range(0, left_size):
        output_file.write(f'{var_1_value_fun(i)} {p1889} {var_2_value_fun(i)} .\n')
    
    for i in range(0, right_size):
        output_file.write(f'{var_1_value_fun(i)} {type_pred} {property_pred} .\n')
        
        
with open(output_filename, 'w') as f:
    generate_file(f, left_size, right_size)
