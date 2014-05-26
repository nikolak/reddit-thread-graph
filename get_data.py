#!/usr/bin/env python
# encoding: utf-8
import os
import json
import datetime
import sys
from time import sleep
import traceback

import praw


r = praw.Reddit("/u/wub_wub's thread score stats script")

filename = None

if len(sys.argv) < 2:
    print "No thread ID passed"
    print "Usage: get_data.py thread_id"
    exit()
else:
    filename = "{}.json".format(sys.argv[1])
    print "Gathering data for submission ID: {}".format(sys.argv[1])


def save(data, save_file=filename):
    with open(save_file, 'w') as out_file:
        json.dump(data, out_file, indent=4)


def load(load_file=filename):
    with open(load_file, 'r') as in_file:
        return json.load(in_file)


if not os.path.exists(filename):
    data = {}
    save(data)
else:
    data = load()

while True:
    try:
        title = data.get("title")
        thread = r.get_submission(submission_id=sys.argv[1])
        date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        data[date] = {"ups": thread.ups,
                      "downs": thread.downs,
                      "score": thread.score,
                      "comments": thread.num_comments}

        if not title:
            data['title'] = thread.title

        save(data)
        print "Saved data on {}".format(date)
    except Exception, e:
        print "Exception:\n\n"
        print traceback.format_exc()
    sleep(60)
