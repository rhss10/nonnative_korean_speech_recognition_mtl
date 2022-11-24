import librosa
import glob
import soundfile
import re
import random
#from g2pk import G2p
#g2p=G2p()

with open('4.csv', 'r', encoding='utf-8') as f: lines = f.readlines()


random.shuffle(lines)
print(lines)

new_lines = []

seconds = 0
f_idx = 0
for line in lines:
	path = line.split(',')[0]
	#path = '/data/lsnoo/KsponSpeech_audio/' + path
	print(path)
	script = line.split(',')[1]
	print(script)

	num_frame = soundfile.info(path).frames
	if num_frame <= 272000:
		f_dur = librosa.get_duration(filename = path)
		seconds += f_dur
		#if seconds >= 180000: break

		file_index = 'valid_4_' + str(f_idx).zfill(6)
		f_idx += 1

		category = line.split(',')[-1][0]
		new_line = file_index + ',' + path + ',' + category + ',' + script + ',' + 'valid' + '\n'
		
		new_lines.append(new_line)

with open('./less_17/4_valid.csv', 'w') as f: f.writelines(new_lines)

hours = round(seconds//3600)
mins = round((seconds%3600)//60)
secs = round(seconds%60)

duration_hms = str(hours) + ':' + str(mins) + ':' + str(secs)

print('number of files: ' + str(len(new_lines)))
print('total_seconds: ' + str(round(seconds)))
print('H:M:S = ' + duration_hms)

#characters = []
#for p in phn:
#	chars = p.split()
#	new_chars = []
#	for i in chars:
#		i += '1\n'
#		new_chars.append(i)
#	characters += new_chars

#characters = list(set(characters))
#characters.sort()
#print(characters)

#with open('dict.ltr.txt', 'w') as f: f.writelines(characters)

