# -*- coding: utf-8 -*-
import datetime
import time
from apscheduler.scheduler import Scheduler
import subprocess

# target URL
URL = 'https://www.youtube.com/watch?v=K-F4CeVsWHA'

# Start the scheduler
sched = Scheduler()
sched.daemonic = False
sched.start()

# define Job
def job_function():
    now = datetime.datetime.now()
    ### CHANGE THE URL HERE ####
    command='streamlink ' + URL + ' 720p --hls-start-offset 01:00:00 --hls-duration 01:00:00 -o "'+str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'-'+str(now.hour)+str(now.minute)+'-jackson.ts"'
    subprocess.call(command,shell=True)
    time.sleep(20)

# Schedules job_function to be run once each hour
sched.add_cron_job(job_function, hour='0-23')
