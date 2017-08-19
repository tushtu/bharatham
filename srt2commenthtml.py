#!/usr/bin/env python

# For loading the SRT
import pysrt
# For generating the HTML file
from yattag import Doc
# For mkdir
import os

srt = 'Bharatham.srt'
comments = 'comments/'
site = '../site/'

os.mkdir(comments)

subs = pysrt.open(srt)
# We do not want the first subtitle
for idx,sub in enumerate(subs[1:]):
  subtitle_id = str(2+idx)
  doc, tag, text = Doc().tagtext()
  doc.asis('<!DOCTYPE html>')
  with tag('html'):
      with tag('body'):
          text(subtitle_id+'. '+sub.text)
          doc.stag('br')
          with tag('audio',controls="",preload="none"):
              doc.stag('source',src=site+subtitle_id+'.ogg',type="audio/ogg")
          doc.stag('br')
          with tag('script'):
              text("var idcomments_acct = '7720157ebbf514bb31abf7430d18bb2c';")
              text("var idcomments_post_id;")
              text("var idcomments_post_url;")
          with tag('span',id="IDCommentsPostTitle",style="display:none"):
              pass
          with tag('script',type="text/javascript",src="https://www.intensedebate.com/js/genericCommentWrapperV2.js"):
              pass

  with open(comments + subtitle_id + '.html','w') as f:
      f.write(doc.getvalue())
