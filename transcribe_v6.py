"""
Transcribe 2.2.mp3 and 5.5.mp3 from V5_Turniti folder using OpenAI Whisper.
Saves results as 2.2.txt and 5.5.txt in the same folder.
"""

import sys
import os

AUDIO_DIR = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Paper\V5_Turniti"
FILES = ["2.2.mp3", "5.5.mp3"]

def transcribe_with_whisper(audio_path, output_path):
    try:
        import whisper
        print(f"[Whisper] Loading model...")
        model = whisper.load_model("base")
        print(f"[Whisper] Transcribing: {audio_path}")
        result = model.transcribe(audio_path, language="es")
        text = result["text"].strip()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"[OK] Saved: {output_path}")
        print(f"--- PREVIEW ---\n{text[:300]}\n---")
        return True
    except ImportError:
        return False

def transcribe_with_faster_whisper(audio_path, output_path):
    try:
        from faster_whisper import WhisperModel
        print(f"[faster-whisper] Loading model...")
        model = WhisperModel("base", device="cpu", compute_type="int8")
        print(f"[faster-whisper] Transcribing: {audio_path}")
        segments, info = model.transcribe(audio_path, language="es")
        text = " ".join([seg.text for seg in segments]).strip()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"[OK] Saved: {output_path}")
        print(f"--- PREVIEW ---\n{text[:300]}\n---")
        return True
    except ImportError:
        return False

def transcribe_with_speech_recognition(audio_path, output_path):
    """Fallback: use SpeechRecognition + pydub for mp3"""
    try:
        import speech_recognition as sr
        from pydub import AudioSegment
        
        # Convert mp3 to wav for SpeechRecognition
        wav_path = audio_path.replace(".mp3", "_tmp.wav")
        audio = AudioSegment.from_mp3(audio_path)
        audio.export(wav_path, format="wav")
        
        r = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="es-CO")
        
        os.remove(wav_path)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"[OK] Saved: {output_path}")
        print(f"--- PREVIEW ---\n{text[:300]}\n---")
        return True
    except Exception as e:
        print(f"[SpeechRecognition] Failed: {e}")
        return False

for fname in FILES:
    audio_path = os.path.join(AUDIO_DIR, fname)
    output_path = os.path.join(AUDIO_DIR, fname.replace(".mp3", ".txt"))
    
    if not os.path.exists(audio_path):
        print(f"[ERROR] File not found: {audio_path}")
        continue
    
    print(f"\n{'='*50}")
    print(f"Processing: {fname}")
    print(f"{'='*50}")
    
    if os.path.exists(output_path):
        print(f"[SKIP] Already transcribed: {output_path}")
        with open(output_path, encoding="utf-8") as f:
            print(f.read())
        continue
    
    success = transcribe_with_whisper(audio_path, output_path)
    if not success:
        success = transcribe_with_faster_whisper(audio_path, output_path)
    if not success:
        success = transcribe_with_speech_recognition(audio_path, output_path)
    if not success:
        print(f"[ERROR] No transcription engine available. Install: pip install openai-whisper OR faster-whisper")
        print(f"        Or manually paste the audio content as {fname.replace('.mp3', '.txt')}")

print("\nDone.")
