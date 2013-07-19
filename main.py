#!/usr/bin/python2 -B

import sfml as sf

#### ABANDON ALL HOPE YE WHO ENTER HERE ####

window = sf.RenderWindow(sf.VideoMode(640, 480), "Intonarumori - Development Build")

# Here we will load all the sounds/samples.
# We're using sf.Sound rather than sf.Music, so expect that.
# Also, we're using FLAC as the audio format, because WAV sucks and fuck OGG.
a = sf.Sound(sf.SoundBuffer.from_file("01.flac"))
b = sf.Sound(sf.SoundBuffer.from_file("02.flac"))
c = sf.Sound(sf.SoundBuffer.from_file("03.flac"))
d = sf.Sound(sf.SoundBuffer.from_file("04.flac"))
e = sf.Sound(sf.SoundBuffer.from_file("05.flac"))
f = sf.Sound(sf.SoundBuffer.from_file("06.flac"))
g = sf.Sound(sf.SoundBuffer.from_file("07.flac"))
h = sf.Sound(sf.SoundBuffer.from_file("08.flac"))
i = sf.Sound(sf.SoundBuffer.from_file("09.flac"))

while window.is_open:
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()
        if type(event) is sf.KeyEvent:
            if event.code is sf.Keyboard.A:
                if not a.status is sf.SoundSource.PLAYING:
                    a.play()
                else:
                    a.stop() # HAMMER TIME!
            elif event.code is sf.Keyboard.S:
                if not b.status is sf.SoundSource.PLAYING:
                    b.play()
                else:
                    b.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.D:
                if not c.status is sf.SoundSource.PLAYING:
                    c.play()
                else:
                    c.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.F:
                if not d.status is sf.SoundSource.PLAYING:
                    d.play()
                else:
                    d.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.G:
                if not e.status is sf.SoundSource.PLAYING:
                    e.play()
                else:
                    e.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.H:
                if not f.status is sf.SoundSource.PLAYING:
                    f.play()
                else:
                    f.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.J:
                if not a.status is sf.SoundSource.PLAYING:
                    g.play()
                else:
                    g.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.K:
                if not h.status is sf.SoundSource.PLAYING:
                    h.play()
                else:
                    h.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.L:
                if not i.status is sf.SoundSource.PLAYING:
                    i.play()
                else:
                    i.stop() # HAMMER TIME!
	window.clear()
	window.display()
