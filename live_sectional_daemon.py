#!/usr/bin/python
import urllib2
import xml.etree.ElementTree as ET
import time
from neopixel import *
import sys
import os
import datetime
from daemon import runner

import live_sectional

class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/null'
        self.stderr_path = '/dev/null'
        self.pidfile_path =  '/var/run/livesectional.pid'
        self.pidfile_timeout = 5
    run()

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
