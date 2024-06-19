import re
from datetime import timedelta

def srt_time_to_ass_time(srt_time):
    hours, minutes, seconds, milliseconds = re.split('[:,]', srt_time)
    return f"{int(hours):01}:{int(minutes):02}:{int(seconds):02}.{int(milliseconds)//10:02}"

def convert_srt_to_ass(srt_filename, ass_filename):
    with open(srt_filename, 'r', encoding='utf-8') as srt_file:
        srt_content = srt_file.read()

    ass_content = [
        "[Script Info]",
        "Title: Converted Subtitle",
        "Original Script: ",
        "ScriptType: v4.00+",
        "Collisions: Normal",
        "PlayDepth: 0",
        "Timer: 100.0000",
        "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
        "Alignment, MarginL, MarginR, MarginV, Encoding",
        "Style: Default,Arial,20,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0.00,0.00,1,1.00,0.00,2,10,10,10,1",
        "",
        "[Events]",
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"
    ]

    srt_blocks = srt_content.split('\n\n')
    
    for block in srt_blocks:
        lines = block.split('\n')
        if len(lines) >= 3:
            index = lines[0].strip()
            times = lines[1].strip()
            text = lines[2:]

            start_time, end_time = times.split(' --> ')
            ass_start_time = srt_time_to_ass_time(start_time)
            ass_end_time = srt_time_to_ass_time(end_time)
            ass_text = "\\N".join(text).replace('{', '\\{').replace('}', '\\}')

            dialogue_line = f"Dialogue: 0,{ass_start_time},{ass_end_time},Default,,0,0,0,,{ass_text}"
            ass_content.append(dialogue_line)

    with open(ass_filename, 'w', encoding='utf-8') as ass_file:
        ass_file.write('\n'.join(ass_content))

# Example usage
convert_srt_to_ass('/Users/kan/Documents/GitHub/karaoke_studio/assets/abhi_na_jao_rocky_aur_rani_dharmendra/vocals.srt', '/Users/kan/Documents/GitHub/karaoke_studio/assets/abhi_na_jao_rocky_aur_rani_dharmendra/vocals.ass')
