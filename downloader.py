# -*- coding: utf-8 -*-
import datetime
import time
from apscheduler.scheduler import Scheduler
import subprocess

### CHANGE THE URL HERE ####
URL = 'https://www.youtube.com/watch?v=K-F4CeVsWHA'
quality = 'best' # can choose from 720p, 480p, 240p 


# Start the scheduler
sched = Scheduler()
sched.daemonic = False
sched.start()

# define Job
def job_function():
    now = datetime.datetime.now()
    outputfile = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'-'+str(now.hour)+str(now.minute)+'.ts'
    
    command='streamlink ' + URL + ' '+ quality + ' --hls-start-offset 01:00:00 --hls-duration 01:00:00 -o ' + outputfile
    subprocess.call(command, shell=True)
    time.sleep(20)

# Schedules job_function to be run once each hour
sched.add_cron_job(job_function, hour='0-23')
