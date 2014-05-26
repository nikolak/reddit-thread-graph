reddit-thread-graph
===================

Scripts to gather data, ups, downs, score, and comment count from reddit thread and create a graph with the data over time. Licensed under MIT license.

Example
=======

Example graph (requires browser that supports svg format):

![Example Graph](https://rawgit.com/Nikola-K/reddit-thread-graph/master/example_graph.svg)

Installation/Setup
==================

This assumes you already have `git`, `pip` and python 2.7+ installed (Not tested/working on 3.x)

    $ git clone https://github.com/Nikola-K/reddit-thread-graph.git
    $ cd reddit-thread-graph
    $ pip install -r requirements.txt

Usage of virtualenvironment is recommended but not required.

Dependencies:

    praw==2.1.16
    pygal==1.4.6


Homepages:

http://pygal.org/

http://praw.readthedocs.org/en/latest/

Usage
=====

Thread ID is used to specify from which thread to gather data, and raw data is saved under that name with `.json` extension.

The graph is saved under same name but with `.svg` file extension.

The thread ID is in url of reddit threads, example:

http://www.reddit.com/r/IAmA/comments/**26gtvt**/i_am_actor_pedro_pascal_i_play_oberyn_in_game_of/

The ID in this case is: `26gtvt`

**Gathering data**

    python get_data.py 26gtvt

A file named `26gtvt.json` will be created in the same folder and it will be updated every minute. The times used are in UTC.

Json file structure is like this:

    {
        "title":"String, title of the thread as it's on reddit.",
        "String, ISO 8601 date format of the data timestamp": {
            "downs": integer current number of downvotes ,
            "score": integer current score returned from API,
            "ups": integer current number of downvotes,
            "comments": integer current number of comments
        }, [next time dict]
    }


Example:

    {
        "title":"I am actor Pedro Pascal. I play Oberyn in Game of Thrones, Ask me anything.",
        "2014-05-26T00:25:17.374758": {
            "downs": 11925,
            "score": 3744,
            "ups": 15669,
            "comments": 3859
        }, [etc]

    }

**Creating a graph**

    python make_graph.py 26gtvt.json

This will produce file named `26gtvt.json.svg` in the same folder as the data file.

The `.json` part can be omitted upon input but will still appear on output file.

License
=======

The MIT License (MIT)

Copyright (c) 2014 Nikola Kovacevic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.