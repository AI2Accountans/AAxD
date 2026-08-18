import os
import sys

# Ruta del archivo MP3 y de salida MD
audio_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\GSKM_FON\Documentacion\flujo.mp3"
output_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\GSKM_FON\Documentacion\flujo_transcripcion.md"

print(f"--- INICIANDO TRANSCRIPCIÓN DE AUDIO ---")
print(f"Archivo de entrada: {audio_path}")

# Opción 1: Probar con OpenAI Whisper (Recomendado)
try:
    import whisper
    print("Cargando modelo OpenAI Whisper ('base')...")
    model = whisper.load_model("base")
    print("Transcribiendo audio en español...")
    result = model.transcribe(audio_path, language="es")
    texto = result.get("text", "").strip()
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Transcripción Oficial del Audio: flujo.mp3\n\n")
        f.write(f"**Ubicación original**: `{audio_path}`\n\n")
        f.write("## Contenido Transcrito\n\n")
        f.write(texto)
        f.write("\n")
        
    print(f"\n✅ TRANSCRIPCIÓN COMPLETADA EXITOSAMENTE CON WHISPER.")
    print(f"Archivo guardado en: {output_path}")
    sys.exit(0)
except ImportError:
    print("⚠️ El paquete 'whisper' no está instalado. Instalando 'openai-whisper'...")
    os.system("pip install openai-whisper")
    try:
        import whisper
        model = whisper.load_model("base")
        result = model.transcribe(audio_path, language="es")
        texto = result.get("text", "").strip()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("# Transcripción Oficial del Audio: flujo.mp3\n\n")
            f.write(texto)
        print(f"\n✅ TRANSCRIPCIÓN COMPLETADA EXITOSAMENTE CON WHISPER.")
        sys.exit(0)
    except Exception as e:
        print(f"Error ejecutando Whisper: {e}")
except Exception as e:
    print(f"Error procesando con Whisper: {e}")

# Opción 2: Fallback con SpeechRecognition si Whisper falla
try:
    import speech_recognition as sr
    import subprocess
    print("Probando alternativa con SpeechRecognition...")
    wav_path = r"C:\Users\IPHIX\Documents\Projects\DFRNT\GSKM_FON\Documentacion\flujo.wav"
    subprocess.run(["ffmpeg", "-y", "-i", audio_path, wav_path], check=True)
    
    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)
    texto = r.recognize_google(audio, language="es-ES")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Transcripción Oficial del Audio: flujo.mp3\n\n")
        f.write(texto)
    print(f"\n✅ TRANSCRIPCIÓN COMPLETADA EXITOSAMENTE CON SPEECH RECOGNITION.")
    print(f"Archivo guardado en: {output_path}")
except Exception as e:
    print(f"\n❌ Error final en la transcripción: {e}")
    print("Asegúrate de instalar whisper con: pip install openai-whisper ffmpeg-python")
