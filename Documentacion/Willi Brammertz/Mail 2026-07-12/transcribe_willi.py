import sys
import os

AUDIO_PATH = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Willi Brammertz\Mail 2026-07-12\RG2Willi.mp3"
OUTPUT_PATH = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\Willi Brammertz\Mail 2026-07-12\RG2Willi.txt"

def transcribe():
    try:
        import whisper
        print("[Whisper] Loading model...")
        model = whisper.load_model("base")
        print(f"[Whisper] Transcribing: {AUDIO_PATH}")
        # Not specifying language so Whisper auto-detects it
        result = model.transcribe(AUDIO_PATH)
        text = result["text"].strip()
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"[OK] Saved: {OUTPUT_PATH}")
        print(f"--- PREVIEW ---\n{text[:300]}\n---")
        return True
    except ImportError:
        print("[ERROR] whisper library not found.")
        return False
    except Exception as e:
        print(f"[ERROR] {e}")
        return False

if __name__ == "__main__":
    if not os.path.exists(AUDIO_PATH):
        print(f"[ERROR] Audio file not found: {AUDIO_PATH}")
        sys.exit(1)
    transcribe()
