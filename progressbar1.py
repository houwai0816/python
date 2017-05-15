#!/usr/bin/python
from progressbar import *
import time

pbar=ProgressBar()
pbar.start()
for i in pbar(range(100)):
	time.sleep(0.5)
