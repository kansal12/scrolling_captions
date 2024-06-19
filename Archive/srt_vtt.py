def srt_to_vtt(srt_content):
    vtt_content = "WEBVTT\n\n"
    vtt_content += srt_content.replace(",", ".")
    return vtt_content

srt_file = "/Users/kan/Documents/GitHub/scrolling_caption_archive/HTML Route/vocals.srt"
vtt_file = "/Users/kan/Documents/GitHub/scrolling_caption_archive/HTML Route/vocals.vtt"

with open(srt_file, "r", encoding="utf-8") as file:
    srt_content = file.read()

vtt_content = srt_to_vtt(srt_content)

with open(vtt_file, "w", encoding="utf-8") as file:
    file.write(vtt_content)
