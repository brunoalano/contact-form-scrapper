"""
scrapper - Heuristic-based contact form scrapper and submitter

Usage:
  python cli.py scrapper -c keyword_1 -c keyword 2

"""

__author__ = 'Bruno Medina <bruno@monoscope.io>'
from .__version__ import __version__

# Logging
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())