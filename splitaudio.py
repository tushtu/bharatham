#!/usr/bin/env python
# Adapted from https://stackoverflow.com/questions/25120363/python-multiprocessing-execute-external-command-and-wait-before-proceeding
from multiprocessing import Pool
import subprocess
import shlex
import pysrt

video = 'Bharatham.mp4'
srt   = 'Bharatham.srt'

def split(cmd):
    p = subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err=p.communicate()
    return (out,err)
    

# Default to number of cores
pool = Pool()
results = []
subs = pysrt.open(srt)
# We don't want the first sub
for idx,sub in enumerate(subs[1:]):
    subtitle_id = idx+2
    start = '%02d:%02d:%02d.%03d' % (sub.start.hours,sub.start.minutes,sub.start.seconds,sub.start.milliseconds)
    end  = '%02d:%02d:%02d.%03d' % (sub.end.hours,sub.end.minutes,sub.end.seconds,sub.end.milliseconds)
    output = 'site/%d.ogg' % (subtitle_id)
    cmd = 'ffmpeg -ss ' + start + ' -to ' + end + ' -vn -ar 44100 -ab 128k -f ogg ' + output + ' -i ' + video
    pool.apply_async(split,(cmd,))

pool.close()
pool.join()
