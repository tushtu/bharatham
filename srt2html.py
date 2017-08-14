#!/usr/bin/env python

# For loading the SRT
import pysrt
# For generating the HTML file
from yattag import Doc
doc, tag, text = Doc().tagtext()

srt = 'Bharatham.srt'
html = 'index.html'

subs = pysrt.open(srt)

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('body'):
        text('Please be patient..')
        doc.stag('hr')
        # We do not want the first subtitle
        for idx,sub in enumerate(subs[1:]):
            subtitle_id = str(2+idx)
            with tag('p'):
                text(subtitle_id+'. '+sub.text)
                doc.stag('br')
                with tag('audio',controls="",preload="none"):
                    doc.stag('source',src='site/'+subtitle_id+'.ogg',type="audio/ogg")
                doc.stag('hr')

with open(html,'w') as f:
    f.write(doc.getvalue())
