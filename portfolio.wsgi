#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/portfolio/")
sys.path.insert(0,"/var/www/portfolio/portfolio/")

import logging
logging.basicConfig(stream=sys.stderr)

from portfolio import app as application
