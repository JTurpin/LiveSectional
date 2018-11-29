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

app = live_sectional.App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
