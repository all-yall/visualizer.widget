fileName='java.wav'
import scipy.io.wavfile as wav
from scipy.fftpack import fft
import pyaudio 
import os
import wave
#This function will convert an mp3 to a wav namned temp.wav
def toWav(arr):
  fname = arr
  oname = 'temp.wav'
  cmd = 'lame --decode {0} {1}'.format( fname,oname )
  os.system(cmd)
  data = wav.read(oname)
#toWav('java.mp3')
player = wave.open(fileName)
p = pyaudio.PyAudio()
stream = p.open(format = p.get_format_from_width(player.getsampwidth()),  
                channels = player.getnchannels(),  
                rate = player.getframerate(),  
                output = True)  

def frequencyArray(clip):
  print clip[0]
  b=[((x+y)/2**8.)*2-1 for x,y in clip] # this is 8-bit track, b is now normalized on [-1,1)
  c = fft(b) # calculate fourier transform (complex numbers list)
  return c[0:200]

song = wav.read(fileName)
rate = song[0]
song = song[1]
fps = 30
loc = 1
chunk=1024

def tick():
  arr=[]
  ind=loc*chunk
  array = frequencyArray(song[ind:ind+(chunk)+1])[::2]
  for x in xrange(len(array)):
    arr.append(0)
    string=str(array[x])
    if string=="0j":
      array[x]=0
      continue
    index=string[2:].replace("+","-").find("-")+2
    temp=string[index:].find("e")
    if temp!=-1:
      index+=temp
    else:
      index=-1
    if index==-1:
      index=string[0:string.find("j")].replace("+","-").rfind("-")
    else:
      index=string[0:index].replace("+","-").rfind("-")
    arrs=[string[1:index],string[index:-2]]
    arr[x]=int((((float(arrs[0])**2)  +  (float(arrs[1])**2))**(.5)))/100
  os.system('echo "'+((" "+str(arr)[1:-1]).replace("   "," ").replace("\n",""))+'">"/tmp/vis.txt"')


done=False
while loc*chunk<len(song):
  if loc%4:
    sheets=tick()
  stream.write(player.readframes(chunk))
  loc+=1




