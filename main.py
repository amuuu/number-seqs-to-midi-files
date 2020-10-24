import math
from midiutil import MIDIFile


seq_type = 2 # 1=fibonacci, 2=prime
index = 3000 # number of notes in the file and sequences
duration = 0.5 # of each note in a half bar
tempo =  120

octave_numbers = 2
base_note = 48 # C2=36, C3=48, C4=60, C5=72


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

def write_to_midi_file(notes_list):    
    volume = 100
    track = 0
    channel = 0
    time = 0 # In beats

    MyMIDI = MIDIFile(1) 
    MyMIDI.addTempo(track, time, tempo)

    for i, pitch in enumerate(notes_list):
        MyMIDI.addNote(track, channel, pitch, (time + i)*duration, duration, volume)

    with open("result.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

if __name__ == "__main__":
    print("Writing...")
    math_seq = []
    if seq_type == 1:
        math_seq = fibonacci_seq(index)
    if seq_type == 2:
        math_seq = prime_seq(index)
    
    notes = generate_notes_list(math_seq)
    
    write_to_midi_file(notes)    
    print("Successfully created the midi file...")
