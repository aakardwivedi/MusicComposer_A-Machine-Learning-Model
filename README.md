# Overview

This is an AI composer that creates musical pieces used as soundtracks for film directors, advertising agencies, and even game studios.The project that trains a LSTM recurrent neural network over a dataset of MIDI files.

Dependencies
============

* Numpy (http://www.numpy.org/)
* Tensorflow (https://github.com/tensorflow/tensorflow)
* Python Midi (https://github.com/vishnubob/python-midi.git)
* Mingus (https://github.com/bspaans/python-mingus)

Use [pip](https://pypi.python.org/pypi/pip) to install any missing dependencies

Basic Usage
===========

1. `mkdir data && mkdir models`
2. run 'python main.py'. This will collect the data, create the chord mapping file in data/nottingham.pickle, and train the model
3. Run `python rnn_sample.py --config_file new_config_file.config` to generate a new MIDI song.

We have trained our machine using a combination of 10 bollywood and hollywood songs.

Credits
===========
This project is inspired by [Siraj Raval](https://github.com/llSourcell)'s [Youtube video](https://www.youtube.com/watch?v=S_f2qV2_U00) 
