import subprocess
from midi2audio import FluidSynth
import os

def generate_music_file():
    # Step 1: Generate .mid file using Magenta
    subprocess.run([
        "melody_rnn_generate",
        "--config=basic_rnn",
        "--bundle_file=magenta_models/basic_rnn/basic_rnn.mag",
        "--output_dir=static/music/",
        "--num_outputs=1",
        "--num_steps=128",
        "--primer_melody=[60]",
        "--output_file=generated.mid"
    ])

    # Step 2: Convert .mid to .mp3 using FluidSynth
    midi_path = "static/music/generated.mid"
    mp3_path = "static/music/generated.mp3"

    fs = FluidSynth(sound_font="soundfonts/FluidR3_GM.sf2")
    fs.midi_to_audio(midi_path, mp3_path)
