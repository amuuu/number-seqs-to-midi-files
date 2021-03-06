import math
from midiutil import MIDIFile


seq_type = 1 # 1=fibonacci, 2=prime
index = 200 # number of notes in the file and sequences
duration = 0.5 # of each note in a half bar
tempo =  120

octave_numbers = 7
base_note = 36 # C2=36, C3=48, C4=60, C5=72


total_notes_number = octave_numbers * 12

def fibonacci_seq(index):
    ans = []
    ans.append(1)
    ans.append(1)
    for i in range(0, index):
        ans.append(ans[len(ans)-1] + ans[len(ans)-2])
    return ans

def prime_seq(index):
    ans = []
    for i in range(2, index+1):
        if check_prime(i):
            ans.append(i)
    return ans

def check_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number%i==0:
            return False
    return True

def generate_notes_list(math_sequence):
    notes = []
    for number in math_sequence:
        notes.append(number % total_notes_number + base_note)
    return notes

def write_to_midi_file(notes_list, file_name):    
    volume = 100
    track = 0
    channel = 0
    time = 0 # In beats

    MyMIDI = MIDIFile(1) 
    MyMIDI.addTempo(track, time, tempo)

    for i, pitch in enumerate(notes_list):
        MyMIDI.addNote(track, channel, pitch, (time + i)*duration, duration, volume)

    with open("results/{}.mid".format(file_name), "wb") as output_file:
        MyMIDI.writeFile(output_file)

if __name__ == "__main__":
    print("Writing...")
    
    math_seq = []
    if seq_type == 1:
        math_seq = fibonacci_seq(index)
        file_name = "fibonacci_midi_{}_{}".format(octave_numbers, index)
    if seq_type == 2:
        math_seq = prime_seq(index)
        file_name = "prime_midi_{}_{}".format(octave_numbers, index)

    
    notes = generate_notes_list(math_seq)
    
    write_to_midi_file(notes, file_name)    
    print("Successfully created the midi file...")
