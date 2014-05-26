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

line_chart = pygal.Line(x_label_rotation=20,
                        show_only_major_dots=True,
                        show_minor_x_labels=False,
                        title='Thread: "{}"'.format(data['title'])
)
try:
    del data['title']  # remove title key/value pair
except:
    pass

sorted_keys = sorted(data)
step = len(sorted_keys) / 10

line_chart.x_title = "Date/Time (UTC)"
line_chart.x_labels = sorted_keys
line_chart.x_labels_major = [sorted_keys[i] for i in
                             range(0, len(sorted_keys), step)] + sorted_keys[-1:]

line_chart.y_label = "Value"

line_chart.add('Upvotes', [data[i]['ups'] for i in sorted_keys])
line_chart.add('Downvotes', [data[i]['downs'] for i in sorted_keys])
line_chart.add('Score', [data[i]['score'] for i in sorted_keys])
line_chart.add('Comments', [data[i]['comments'] for i in sorted_keys])
line_chart.render_to_file("{}.svg".format(sys.argv[1]))