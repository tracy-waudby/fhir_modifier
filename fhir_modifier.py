#!/user/bin/env python3

import argparse
import csv
import json
import os


def find_key(obj, key):
    if isinstance(obj, dict):
        yield from iter_dict(obj, key, [])
    elif isinstance(obj, list):
        yield from iter_list(obj, key, [])

def iter_dict(d, key, indices):
    for k, v in d.items():
        if k == key:
            yield indices + [k], v
        if isinstance(v, dict):
            yield from iter_dict(v, key, indices + [k])
        elif isinstance(v, list):
            yield from iter_list(v, key, indices + [k])

def iter_list(seq, key, indices):
    for k, v in enumerate(seq):
        if isinstance(v, dict):
            yield from iter_dict(v, key, indices + [k])
        elif isinstance(v, list):
            yield from iter_list(v, key, indices + [k])


def main(filename):
	with open(filename) as json_file:
		data = json.load(json_file)
		for t in find_key(data, 'subject'):
			seq, val = t
			obj = data
			for k in seq:
				obj = obj[k]
			obj['patientId'] = obj['reference'].strip('Patient/') 

	outfile = 'processed/{}'.format(filename)
	with open(outfile, 'w') as output:
		json_out = json.dumps(data)
		output.write(json_out)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('file', nargs='+', help='path to file')
	args_namespace = parser.parse_args()
	args = vars(args_namespace)['file'][0]
	if not os.path.exists('processed'):
		os.makedirs('processed')
	main(args)
