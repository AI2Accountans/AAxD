import os
import sys
import subprocess

def transcribe_audio():
    audio_path = r"c:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Charles Hoffman\Mail\2026-08-03\Charlie.ogg"
    wav_path = r"c:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Charles Hoffman\Mail\2026-08-03\Charlie.wav"
    output_txt = r"c:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Charles Hoffman\Mail\2026-08-03\charlie_transcription.txt"

    print(f"[*] Processing audio file: {audio_path}")

    # Method 1: Using OpenAI Whisper
    try:
        import whisper
        print("[+] Attempting transcription with whisper...")
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        text = result.get("text", "").strip()
        print("\n--- TRANSCRIPTION (WHISPER) ---")
        print(text)
        with open(output_txt, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[✓] Saved transcription to: {output_txt}")
        return text
    except Exception as e:
        print(f"[-] Whisper failed: {e}")

    # Method 2: Convert OGG to WAV using ffmpeg, then use SpeechRecognition
    try:
        print("[+] Converting OGG to WAV via ffmpeg...")
        subprocess.run(["ffmpeg", "-y", "-i", audio_path, wav_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio = r.record(source)
            print("[+] Transcribing with SpeechRecognition...")
            text = r.recognize_google(audio, language="en-US")
            print("\n--- TRANSCRIPTION (GOOGLE SPEECH RECOGNITION) ---")
            print(text)
            with open(output_txt, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"[✓] Saved transcription to: {output_txt}")
            return text
    except Exception as e:
        print(f"[-] SpeechRecognition/ffmpeg failed: {e}")

if __name__ == "__main__":
    transcribe_audio()
