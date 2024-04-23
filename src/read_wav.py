import wave
import struct

def read_wav_file(filename):
    with wave.open(filename, 'rb') as wav_file:
        # Read WAV file header
        num_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        frame_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()
        
        # Print header information
        print("Number of channels:", num_channels)
        print("Sample width (bytes per sample):", sample_width)
        print("Frame rate (samples per second):", frame_rate)
        print("Total number of frames:", num_frames)

        # Read audio data
        audio_data = wav_file.readframes(num_frames)

        # Parse audio data into frames
        frames = []
        for i in range(num_frames):
            frame = audio_data[i * num_channels * sample_width : (i + 1) * num_channels * sample_width]
            frames.append(frame)

        return frames

def main():
    filename = "../wav/example.wav"
    frames = read_wav_file(filename)
    
    # Display properties of each frame
    for i, frame in enumerate(frames):
        print("Frame", i + 1)
        print("Data:", frame)
        print("Size:", len(frame), "bytes")
        print("Channel 1 sample:", struct.unpack('<h', frame[:2])[0])  # Assuming 16-bit PCM
        print("Channel 2 sample:", struct.unpack('<h', frame[2:])[0])  # Assuming stereo
        print()

if __name__ == "__main__":
    main()
