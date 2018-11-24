
import importlib

from .pyopengv import *


globals().update(importlib.import_module('pyopengv.pyopengv').__dict__)
