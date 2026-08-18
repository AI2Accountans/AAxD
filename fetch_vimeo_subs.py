import yt_dlp
import urllib.request
import urllib.parse
import sys

def download_vimeo_subs(url, output_file="vimeo2.vtt"):
    print(f"Extracting info for {url}")
    ydl_opts = {'skip_download': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    
    print(f"Title: {info.get('title', 'Unknown Title')}")
    
    subs = info.get('subtitles', {})
    if 'en-x-autogen' not in subs and 'en' not in subs:
        print("No english subtitles found.")
        print("Available:", list(subs.keys()))
        return
        
    sub_key = 'en-x-autogen' if 'en-x-autogen' in subs else 'en'
    sub_list = subs[sub_key]
    
    m3u8_url = None
    vtt_url = None
    
    for s in sub_list:
        if s.get('protocol') == 'm3u8_native':
            m3u8_url = s.get('url')
            
    if m3u8_url:
        print(f"Fetching m3u8: {m3u8_url}")
        m3u8_text = urllib.request.urlopen(m3u8_url).read().decode('utf-8')
        rel_path = [l for l in m3u8_text.split('\n') if not l.startswith('#') and l.strip()][0]
        vtt_url = urllib.parse.urljoin(m3u8_url, rel_path)
        
    if vtt_url:
        print(f"Fetching VTT: {vtt_url}")
        vtt = urllib.request.urlopen(vtt_url).read().decode('utf-8')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(vtt)
        print("Successfully saved subtitles.")
    else:
        print("Could not find a valid VTT URL.")

if __name__ == "__main__":
    download_vimeo_subs('https://vimeo.com/1159682963/cce8d17d78?fl=pl&fe=vl')
