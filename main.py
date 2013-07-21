#!/usr/bin/python

# WARNING
# I haven't been able to test any of this yet,
# but you get the gist of it :)

import sfml as sf

versiontext="Intonarumori - Massive refactoring - untested"

window = sf.RenderWindow(sf.VideoMode(640, 480), versiontext)
j = sf.Text(versiontext, sf.Font.from_file("libmono.ttf"))
j.move(sf.Vector2(320-250, 240))


# Here we will load all the sounds/samples.
# We're using sf.Sound rather than sf.Music, so expect that.
# Also, we're using FLAC as the audio format, because WAV sucks and fuck OGG.
sounds = {
  "a": sf.Sound(sf.SoundBuffer.from_file("01.flac")),
  "b": sf.Sound(sf.SoundBuffer.from_file("02.flac")),
  "c": sf.Sound(sf.SoundBuffer.from_file("03.flac")),
  "d": sf.Sound(sf.SoundBuffer.from_file("04.flac")),
  "e": sf.Sound(sf.SoundBuffer.from_file("05.flac")),
  "f": sf.Sound(sf.SoundBuffer.from_file("06.flac")),
  "g": sf.Sound(sf.SoundBuffer.from_file("07.flac")),
  "h": sf.Sound(sf.SoundBuffer.from_file("08.flac")),
  "i": sf.Sound(sf.SoundBuffer.from_file("09.flac"))
}

for sound in sounds.itervalues():
  sound.volume = 60.0




playkeys = {
  sf.Keyboard.A: "a",
  sf.Keyboard.S: "b",
  sf.Keyboard.D: "c",
  sf.Keyboard.F: "d",
  sf.Keyboard.G: "e",
  sf.Keyboard.H: "f",
  sf.Keyboard.J: "g",
  sf.Keyboard.K: "h",
  sf.Keyboard.L: "i",
}

loopkeys = {
  sf.Keyboard.Q: "a",
  sf.Keyboard.W: "b",
  sf.Keyboard.E: "c",
  sf.Keyboard.R: "d",
  sf.Keyboard.T: "e",
  sf.Keyboard.Y: "f",
  sf.Keyboard.U: "g",
  sf.Keyboard.I: "h",
  sf.Keyboard.O: "i",
}

pitchkeys = {
  sf.Keyboard.Z: "a",
  sf.Keyboard.X: "b",
  sf.Keyboard.C: "c",
  sf.Keyboard.V: "d",
  sf.Keyboard.B: "e",
  sf.Keyboard.N: "f",
  sf.Keyboard.M: "g",
  sf.Keyboard.PERIOD: "h",
  sf.Keyboard.COMMA: "i",
}


running = True

while running:
  for event in window.events:
    if type(event) is sf.CloseEvent:
      running = False
      
    elif type(event) is sf.KeyEvent and event.pressed:
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

window.close
  