#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import json

import pygal


filename = None
data = None

if len(sys.argv) < 2:
    print "No thread ID passed"
    print "Usage: make_graph.py thread_id"
    exit()
else:
    filename = "{}{}".format(sys.argv[1],
                             "" if sys.argv[1].endswith('.json') else '.json')
    print "Making graph for thread ID: {}".format(sys.argv[1])


def load(load_file=filename):
    with open(load_file, 'r') as in_file:
        return json.load(in_file)


if not os.path.exists(filename):
    print "File {}.json not found".format(filename)
    exit()
else:
    data = load()

line_chart = pygal.Line()
line_chart.show_dots = False
line_chart.title = 'Thread: "{}"'.format(data['title'])
try:
    del data['title']  # remove title key/value pair
except:
    pass
line_chart.x_title = "Time (UTC)"
line_chart.x_labels = sorted(data)
line_chart.y_label = "Value"
line_chart.add('Upvotes', [data[i]['ups'] for i in sorted(data)])
line_chart.add('Downvotes', [data[i]['downs'] for i in sorted(data)])
line_chart.add('Score', [data[i]['score'] for i in sorted(data)])
line_chart.add('Comments', [data[i]['comments'] for i in sorted(data)])
line_chart.render_to_file("{}.svg".format(sys.argv[1]))