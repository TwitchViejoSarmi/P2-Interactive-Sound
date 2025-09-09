# BettingEchoes — A Minimal Audio Visual-Novel (Terminal) using OpenAL

## Developers

- Juan Esteban Becerra Gutiérrez
- Alejandro Sarmiento Rivera

**Language:** Spanish story text (terminal only).  
**Code:** English, object‑oriented Python.  
**Audio:** OpenAL (3D positional effects for each line).

## What this is

A tiny, Zork-like _visual novel by text_ about fictional gambling. The player advances **line by line** and makes a couple of choices leading to **two distinct endings**. There is **no save system**.

This project is designed to satisfy constraints similar to a university assignment:

- Uses **OpenAL** for spatialized audio; every line triggers a suitable effect or musical cue positioned in 3D.
- **Console interface** (no colors).
- **50+ lines** forming a complete narrative (beginning, middle, and end).
- **Object-Oriented** code, simple/clean.
- **Works via .bat scripts** to create/activate a venv and run the game on Windows.

> All characters and situations are fictional. This project **does not promote gambling**.

## Getting started (Windows)

1. Install a recent Python 3.10+.
2. Open **Command Prompt** in this folder.
3. Run:
   ```bat
   scripts\setup_and_run.bat
   ```
   The script will create `.venv`, install dependencies, and launch the game.

Later runs:

```bat
scripts\run_game.bat
```

## Project layout

```
BettingEchoes/
  assets/
    music/         # place BGM tracks here (stereo recommended)
    sfx/           # place SFX here (mono recommended for spatialization)
  scripts/
    setup_and_run.bat
    run_game.bat
  src/
    betting_echoes/
      __init__.py
      main.py
      game.py
      audio_engine.py
      story.py
  requirements.txt
  README.md
```

## Audio recommendations

- **SFX (positional):** use **mono WAV**, 44.1 kHz, 16-bit PCM. Short, dry effects: footsteps, murmurs, dice, chips, doors, crowd, street, etc.
- **BGM (non-positional):** **stereo WAV/OGG**, gentle loops per scene (tension, calm, decision).
- Suggested cues:
  - _ambience_casino.wav_ (loop), _crowd_murmur.wav_, _chips_clatter.wav_, _card_flip.wav_,
    _door_far.wav_, _rain_outside.wav_, _heartbeat_soft.wav_, _coin_spin.wav_, _cash_register.wav_,
    _footsteps_left.wav/right.wav_, _whisper_behind.wav_, _siren_far_right.wav_.
- Loudness: normalize to approximately **-18 LUFS** integrated (or just keep consistent perceived loudness).
- Duration: very short stingers (0.5–2 s) + a few ambiences (15–60 s) set to loop.
- Legal: only use audio you are allowed to distribute (public domain/CC0/your own).

## How OpenAL is used

- We create a `Listener` at (0,0,0).
- Each story line spawns a `Source` from a file and sets its **3D position** (x,y,z) and gain.
- Ambient sources can **loop**; line SFX are one-shots.
- Threads are used so ambience can continue while the player reads/inputs.

## Credits

- Code written for academic demonstration. Replace/credit your own sounds in `assets/`.
