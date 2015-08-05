"""Implements the xonsh history object"""
import os
import sys
import json
import time
import uuid
import builtins
from collections import OrderedDict

from xonsh import lazyjson


class History(object):

    ordered_history = []

    def __init__(self, hid=None):
        #env = builtins.__xonsh_env__
        #self.hf = env.get('XONSH_HISTORY_FILE',
        #        os.path.expanduser('~/.xonsh_history.json'))
        self.hf = '~/.xonsh-history-{0}.json'.format(uuid.uuid4())

    def open_history(self):
        """Loads previous history from ~/.xonsh_history.json or
        location specified in .xonshrc if it exists.
        """
        if os.path.exists(self.hf):
            self.ordered_history = lazyjson.LazyJSON(self.hf).load()
        else:
            sys.stdout.write("No history\n")


    def close_history(self):
        with open(self.hf, 'w+') as fp:
            lazyjson.dump(self.ordered_history, fp) 


    def add(self, cmd):
        """Adds command with current timestamp to ordered history.

        Parameters
        ----------
        cmd: dict 
            Command dictionary that should be added to the ordered history.
        """
        #self.ordered_history[time.time()] = {'cmd': cmd}
        cmd['timestamp'] = time.time()
        self.ordered_history.append(cmd)
