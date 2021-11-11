from google.cloud import texttospeech

def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Wavenet-D",
    ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    )
    audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
    request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )
    # The response's audio_content is binary.
    with open(file_full, "wb") as out:
        out.write(response.audio_content)
        print(f"Audio content written to file {file_full}")

file_name = input("File Name (without .mp3 extension): ")
text = input("Text: ")
file_full = f"audio/{file_name}.mp3"

synthesize_text(text)