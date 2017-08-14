# The Bharatham Subtitle Project

[Bharatham](https://en.wikipedia.org/wiki/Bharatham) is a 1991 award winning [Malayalam](https://en.wikipedia.org/wiki/Malayalam) film classic. Despite it being widely considered as one of the best Indian movies made to date, subtitles are hard to come by.

Thefore, I decided to rectify this by creating my own. Please note that I am not an expert practitioner of Malayalam and the objective of creating a GitHub project was to encourage more qualified practitioners to improve on my subtitles. 

# Where can I get the subtitles?
[Right here.](https://github.com/tushtu/bharatham/releases)


# Collaboration 
I have generated an [HTML file](https://tushtu.github.io/bharatham/) which contains all audio clips and their corresponding translation. 

If you feel that it can be improved, just edit the appropriate line in [Bharatham.srt](Bharatham.srt) and send me a pull request.

# Tools
The video file was obtained from [YouTube](https://www.youtube.com/watch?v=UisSHGY1emA). I used [Subtitle Editor](https://apps.ubuntu.com/cat/applications/subtitleeditor/) to create the subtitles. 

If you would like to load these subtitles into Subtitle Editor, you must 
* Obtain the video linked above
* Load it and [Bharatham.srt](Bharatham.srt).
* (optional) Generate a waveform which will make it easier to segment the audio.

I used 
* [splitaudio.py](splitaudio.py) to segment the movie audio into an OGG file for each subtitle (stored [here](site)) and 
* [srt2html.py](srt2html.py) to generate the [HTML file](https://tushtu.github.io/bharatham/) file for easier collaboration.
