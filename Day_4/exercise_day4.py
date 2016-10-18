## Assigment 4

## import os and webbrowser:
import os
import webbrowser

## open file:
file_name = "lulu_mix_16.csv"
my_path = os.environ["HOME"]
file_path = os.path.join(my_path,file_name)
file = open(file_path,"r")

## Defining the youtube url
url = "https://www.youtube.com/results?search_query="

## making the Song class:
class Song(object):
	"""A song class"""
	def __init__(self, title, artist, duration):
		self.title = title
		self.artist = artist
		try:
			self.duration = int(duration)
		except ValueError:
			self.duration = 0
		if self.duration < 0: raise Exception("duration is negative!")
	def pretty_duration(self):
		""" Print the duration in a nice way """
		h = int(self.duration)/3600
		rest = int(self.duration)%3600
		m = rest/60
		s = rest%60
		print h, "hours", m, "minutes", s, "seconds"
	def play(self):
		mew_url = url + self.title
		webbrowser.open_new(mew_url)
		

## Testing the Song class:
song_a = Song("Barbra Streisand","Duck Sauce","300")
song_a.pretty_duration()
song_a.play()
print song_a.duration
print song_a.artist
print song_a.title
print song_a.duration


## open file (the file without the negative duration):
file_name = "lulu_mix_16_2.csv"
my_path = os.environ["HOME"]
file_path = os.path.join(my_path,file_name)
file = open(file_path,"r")

## make a generator with the lines fo the file: 
file2 = [l.strip("\n\r").split(",") for l in open(file_path)]

## Defining songs
songs = []

for line in file2[2:]:
	my_song = Song(line[0],line[1],line[2])
	songs.append(my_song)


## Testing the codes:
for s in songs: print s.artist
for s in songs: print s.pretty_duration()
print sum(s.duration for s in songs), "seconds in total"
songs[6].play()








































