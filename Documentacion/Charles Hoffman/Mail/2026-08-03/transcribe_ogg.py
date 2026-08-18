import sys
import os

def main():
    audio_path = r"c:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Charles Hoffman\Mail\2026-08-03\Charlie.ogg"
    output_path = r"c:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Charles Hoffman\Mail\2026-08-03\charlie_transcription.txt"
    
    print("Testing audio transcription...")
    
    # Try openai-whisper / whisper
    try:
        import whisper
        print("Loading whisper model...")
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        text = result.get("text", "")
        print("Whisper Transcription:")
        print(text)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        return
    except Exception as e:
        print("Whisper error:", e)

    # Try speech_recognition with ffmpeg conversion if needed
    try:
        import speech_recognition as sr
        import subprocess
        
        wav_path = r"c:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Charles Hoffman\Mail\2026-08-03\Charlie.wav"
        subprocess.run(["ffmpeg", "-y", "-i", audio_path, wav_path], check=True)
        
        r = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio = r.record(source)
            text = r.recognize_google(audio, language="en-US")
            print("Google Speech Recognition:")
            print(text)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            return
    except Exception as e:
        print("SpeechRecognition error:", e)

if __name__ == "__main__":
    main()
