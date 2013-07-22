#!/usr/bin/env python

# WARNING
# I haven't been able to test any of this yet,
# but you get the gist of it :)

import sfml as sf

versiontext = "Intonarumori - Massive refactoring - untested"


if __name__ == '__main__':
    window = sf.RenderWindow(sf.VideoMode(640, 480), versiontext)
    j = sf.Text(versiontext, sf.Font.from_file("libmono.ttf"))
    j.move(sf.Vector2(320-250, 240))

    # Some magic to create the sounds list. See my previous commit.
    keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    sounds = dict((v, '%02d.flac' % (i+1)) for i, v in enumerate(keys))

    for k, v in sounds.iteritems():
        sounds[k] = sf.Sound(sf.SoundBuffer.from_file(sounds[k]))
        v.volume = 60.0

    sk = sf.Keyboard
    playkeys = dict(zip([sk.A, sk.S, sk.D, sk.F, sk.G, sk.H, sk.J, sk.K, sk.L], keys))
    loopkeys = dict(zip([sk.Q, sk.W, sk.E, sk.R, sk.T, sk.Y, sk.U, sk.I, sk.O], keys))
    pitchkeys = dict(zip([sk.Z, sk.X, sk.C, sk.V, sk.B, sk.N, sk.M, sk.PERIOD, sk.COMMA], keys))

    running = True

    while running:
        for event in window.events:
            if event.type == sf.CloseEvent:
                running = False

            elif event.type == sf.KeyEvent and event.pressed:
                if event.code is sf.Keyboard.ESCAPE:
                    running = False

                elif event.code in playkeys:
                    sound = sounds[playkeys[event.code]]
                    sound.play() if sound.status is not sf.SoundSource.PLAYING else sound.stop()

                elif event.code in loopkeys:
                    sound = sounds[loopkeys[event.code]]
                    sound.loop = not sound.loop

                elif event.code in pitchkeys:
                    sound = sounds[pitchkeys[event.code]]
                    sound.pitch = 0.5 if sound.pitch == 1 else 1

        window.clear()
        window.draw(j)
        window.display()

    window.close()
