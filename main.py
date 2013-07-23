#!/usr/bin/python2 -B

import sfml as sf

#### ABANDON ALL HOPE YE WHO ENTER HERE ####

window = sf.RenderWindow(sf.VideoMode(640, 480), "Intonarumori - Development Build")

# Here we will load all the sounds/samples.
# We're using sf.Sound rather than sf.Music, so expect that.
# Also, we're using FLAC as the audio format, because WAV sucks and fuck OGG.
a = sf.Sound(sf.SoundBuffer.from_file("01.flac"))
a.volume = 60.0
b = sf.Sound(sf.SoundBuffer.from_file("02.flac"))
c = sf.Sound(sf.SoundBuffer.from_file("03.flac"))
d = sf.Sound(sf.SoundBuffer.from_file("04.flac"))
e = sf.Sound(sf.SoundBuffer.from_file("05.flac"))
f = sf.Sound(sf.SoundBuffer.from_file("06.flac"))
g = sf.Sound(sf.SoundBuffer.from_file("07.flac"))
h = sf.Sound(sf.SoundBuffer.from_file("08.flac"))
i = sf.Sound(sf.SoundBuffer.from_file("09.flac"))

j = sf.Text("Intonarumori - Dev Build 0.2a", sf.Font.from_file("libmono.ttf"))
j.move(sf.Vector2(320-250, 240))

while window.is_open:
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()
        if type(event) is sf.KeyEvent:
            if event.code is sf.Keyboard.A and event.pressed:
                if not a.status is sf.SoundSource.PLAYING:
                    a.play()
                else:
                    a.stop() # HAMMER TIME!
            elif event.code is sf.Keyboard.ESCAPE:
                window.close()
            elif event.code is sf.Keyboard.S and event.pressed:
                if not b.status is sf.SoundSource.PLAYING:
                    b.play()
                else:
                    b.stop() # HAMMER TIME!
            elif event.code is sf.Keyboard.D and event.pressed:
                if not c.status is sf.SoundSource.PLAYING:
                    c.play()
                else:
                    c.stop() # HAMMER TIME!
            elif event.code is sf.Keyboard.F and event.pressed:
                if not d.status is sf.SoundSource.PLAYING:
                    d.play()
                else:
                    d.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.G and event.pressed:
                if not e.status is sf.SoundSource.PLAYING:
                    e.play()
                else:
                    e.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.H and event.pressed:
                if not f.status is sf.SoundSource.PLAYING:
                    f.play()
                else:
                    f.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.J and event.pressed:
                if not g.status is sf.SoundSource.PLAYING:
                    g.play()
                else:
                    g.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.K and event.pressed:
                if not h.status is sf.SoundSource.PLAYING:
                    h.play()
                else:
                    h.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.L and event.pressed:
                if not i.status is sf.SoundSource.PLAYING:
                    i.play()
                else:
                    i.stop() # HAMMER TIME!
            if event.code is sf.Keyboard.Q and event.pressed:
                if not a.loop:
                    a.loop = True
                else:
                    a.loop = False
            elif event.code is sf.Keyboard.W and event.pressed:
                if not b.loop:
                    b.loop = True
                else:
                    b.loop = False
            elif event.code is sf.Keyboard.E and event.pressed:
                if not c.loop:
                    c.loop = True
                else:
                    c.loop = False
            elif event.code is sf.Keyboard.R and event.pressed:
                if not d.loop:
                    d.loop = True
                else:
                    d.loop = False
            if event.code is sf.Keyboard.T and event.pressed:
                if not e.loop:
                    e.loop = True
                else:
                    e.loop = False
            if event.code is sf.Keyboard.Y and event.pressed:
                if not f.loop:
                    f.loop = True
                else:
                    f.loop = False
            if event.code is sf.Keyboard.U and event.pressed:
                if not g.loop:
                    g.loop = True
                else:
                    g.loop = False
            if event.code is sf.Keyboard.I and event.pressed:
                if not h.loop:
                    h.loop = True
                else:
                    h.loop = False
            if event.code is sf.Keyboard.O and event.pressed:
                if not i.loop:
                    i.loop = True
                else:
                    i.loop = False
            if event.code is sf.Keyboard.Z and event.pressed:
                 if a.pitch == 1:
                    a.pitch = .5
                 else:
                    a.pitch = 1
            elif event.code is sf.Keyboard.X and event.pressed:
                if b.pitch == 1:
                    b.pitch = .5
                else:
                    b.pitch = 1
            elif event.code is sf.Keyboard.C and event.pressed:
                if c.pitch == 1:
                    c.pitch = .5
                else:
                    c.pitch = 1
            elif event.code is sf.Keyboard.V and event.pressed:
                if d.pitch == 1:
                    d.pitch = .5
                else:
                    d.pitch = 1
            if event.code is sf.Keyboard.B and event.pressed:
                if e.pitch == 1:
                    e.pitch = .5
                else:
                    e.pitch = 1
            if event.code is sf.Keyboard.N and event.pressed:
                if f.pitch == 1:
                    f.pitch = .5
                else:
                    f.pitch = 1
            if event.code is sf.Keyboard.M and event.pressed:
                if g.pitch == 1:
                    g.pitch = .5
                else:
                    g.pitch = 1
            if event.code is sf.Keyboard.COMMA and event.pressed:
                if h.pitch == 1:
                    h.pitch = .5
                else:
                    h.pitch = 1
            if event.code is sf.Keyboard.PERIOD and event.pressed:
                if i.pitch == 1:
                    i.pitch = .5
                else:
                    i.pitch = 1
    window.clear()
    window.draw(j)
    window.display()
