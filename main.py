#!/usr/bin/env python

# ^^^ That's how the shebang should be written. See:
# http://stackoverflow.com/questions/2429511/why-do-people-write-usr-bin-env-python-on-the-first-line-of-a-python-script

# WARNING
# I haven't been able to test any of this yet,
# but you get the gist of it :)

import sfml as sf

versiontext = "Intonarumori - Massive refactoring - untested"


if __name__ == '__main__':
    window = sf.RenderWindow(sf.VideoMode(640, 480), versiontext)
    j = sf.Text(versiontext, sf.Font.from_file("libmono.ttf"))
    j.move(sf.Vector2(320-250, 240))


    # Here we will load all the sounds/samples.
    # We're using sf.Sound rather than sf.Music, so expect that.
    # Also, we're using FLAC as the audio format, because WAV sucks and fuck OGG.
    
    # Alternative way of creating the same list - a horrible one liner:
    # This way is fine, but I'm not using it because the one below is
    # slightly more readable.
    # sounds = dict((chr(ord('a') + i), '%02d.flac' % (i+1)) for i in range(0, 10))

    # Actually, this isn't that pretty either..
    # sounds = dict(zip(
    #     (chr(i) for i in range(ord('a'), ord('i')+1)),   # Zip a list from 'a' to 'i' together
    #     ('%02d.flac' % i for i in range(1, 10))          # with one from '01.flac' to '09.flac'.
    # ))
    
    # Now we're talking!
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
