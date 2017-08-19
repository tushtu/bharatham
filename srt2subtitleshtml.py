#!/usr/bin/env python

# For loading the SRT
import pysrt
# For generating the HTML file
from yattag import Doc
doc, tag, text = Doc().tagtext()

srt = 'Bharatham.srt'
html = 'subtitles.html'
site = 'site/'
comments = 'comments/'

subs = pysrt.open(srt)

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('body'):
        text('Help improve the subtitles for the 1991 Malayalam classic ')
        with tag('a',target="_blank",href="https://en.wikipedia.org/wiki/Bharatham"):
            text('Bharatham')
        doc.stag('hr')
        # We do not want the first subtitle
        for idx,sub in enumerate(subs[1:]):
            subtitle_id = str(2+idx)
            with tag('p'):
                with tag('a',name=subtitle_id):
                    text(subtitle_id+'. '+sub.text)
                doc.stag('br')
                with tag('audio',controls="",preload="none"):
                    doc.stag('source',src=site+subtitle_id+'.ogg',type="audio/ogg")
                    doc.stag('source',src=site+subtitle_id+'.mp3',type="audio/mpeg")
                doc.stag('br')
                with tag('a',href="subtitles.html#"+subtitle_id,onclick="parent.comments.location.href = '"+comments+subtitle_id + ".html'"):
                    text('Comments')
                doc.stag('hr')

with open(html,'w') as f:
    f.write(doc.getvalue())
