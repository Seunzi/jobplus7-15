# encoding: utf-8

import multiprocessing

bind = 'unix:/run/gunicorn/jobplus.socket'
pid = '/run/gunicorn/jobplus.pid'
workers = multiprocessing.cpu_count() * 2 + 1
