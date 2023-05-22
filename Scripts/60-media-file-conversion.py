from pydub import AudioSegment
import os

def convert_audio(input_path, output_path, output_format):
    # Load the audio file
    audio = AudioSegment.from_file(input_path)

    # Set the output format
    output_format = output_format.lower()

    # Convert the audio file
    converted_audio = audio.export(output_path, format=output_format)

    # Print success message
    print(f"File converted successfully to {output_format} format!")

# Provide the paths and format for conversion
input_file = "path/to/input/file.mp3"
output_file = "path/to/output/file.wav"
output_format = "wav"

# Call the convert_audio function
convert_audio(input_file, output_file, output_format)
