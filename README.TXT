When you first open it their will be an error message, "Can't find /tmp/vis.txt", that is normal, just continue

This is a music visualizer widget for Übersicht.
To be able to use it you have to have python installed.
if you don't have python installed then open up a terminal and

1. Install x-code if you don't have it, run: 
"xcode-select --install" 

2. Install homebrew if you don't have it, run: 
"/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)""

3. Install python! run:
"brew install python"


you will also need the following python libraries:

1. scipy
2. pyaudio 
3. wave

run "pip install" with them. i.e.
"pip install scipy"
"pip install pyaudio"
"pip install wave"


Finaly, navigate to the widget and run in your terminal 
"python vis.py"

the preloaded song is java jive sung by the inkspots.
if you want to load your own song open up the python file and change the first line of code from

fileName='java.wav'

to 

fileName='whateverYourFileIs.wav'

IT HAS TO BE A WAV FILE IN THE WIDGET'S FOLDER.


anyway, thanks for viewing i guess.




