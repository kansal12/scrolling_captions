import re

def convert_vtt_to_ass(vtt_file, ass_file):
    try:
        with open(vtt_file, 'r', encoding='utf-8') as vtt:
            vtt_content = vtt.read()
        
        # Regular expression to match timestamps and text blocks in VTT format
        pattern = r'(\d{2}):(\d{2}):(\d{2})\.(\d{3}) --> (\d{2}):(\d{2}):(\d{2})\.(\d{3})\n(.*?)\n\n'
        subtitle_lines = re.findall(pattern, vtt_content, re.DOTALL)
        
        # Open the ASS file for writing
        with open(ass_file, 'w', encoding='utf-8') as ass:
            # Write ASS header
            ass.write('[Script Info]\n')
            ass.write('Title: Converted from VTT\n')
            ass.write('Original Script: Unknown\n')
            ass.write('ScriptType: v4.00\n')
            ass.write('Collisions: Normal\n')
            ass.write('\n')
            ass.write('[V4+ Styles]\n')
            ass.write('Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, TertiaryColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, AlphaLevel, Encoding\n')
            ass.write('Style: Default,Arial,20,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,-1,0,1,1,0,2,10,10,10,0,0\n')
            ass.write('\n')
            ass.write('[Events]\n')
            ass.write('Format: Marked, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n')
            
            # Write subtitle lines in ASS format
            for line in subtitle_lines:
                start_hour, start_min, start_sec, start_ms, end_hour, end_min, end_sec, end_ms, text = line
                start_time = f'{start_hour}:{start_min}:{start_sec}.{start_ms}'
                end_time = f'{end_hour}:{end_min}:{end_sec}.{end_ms}'
                ass.write(f'Dialogue: Marked=0,{start_time},{end_time},Default,,0,0,0,,{text}\n')
        
        print(f'Conversion successful. ASS file saved as "{ass_file}".')

    except FileNotFoundError:
        print(f'Error: File "{vtt_file}" not found.')

# Example usage:
convert_vtt_to_ass('subtitles.vtt', 'subtitles.ass')
