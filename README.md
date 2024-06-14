# karaoke_video

This is a HTML based media player.

**Input**: mp4 video, WebVTT (subtitles), Subtitle Formatting Details. See *video.mp4*, *subtitles.vtt* and *format.json*
**Output**: mp4 video, with background greyed out, and with subtitles scrolling from bottom to top. The currently active line will be in the centre of the screen (historical lines will be above, and future lines will be below). At any point in time, max of laast three and future three lines will be shown on the screen. See *format.json* for all formatting details.

[
background:{
"colour": "#848884",
"opacity":"30%"
}

frame: {
"aspect_ration":"same as video"
left_cushion=10%
right_cushion=10%
top_cushion: 10%
botton_cushion: 10%
}

historical: {
"name":"historical"
"font":"calibri",
"size":"12"
"colour":"#C0C0C0"
"number":"3" # max number of lines that will be shown on screen 
}

current: {
"name":"historical"
"font":"calibri",
"size":"15"
"colour":"#FFFFFF"
"number":"1" # max number of lines that will be shown on screen 
}

Future: {
"name":"historical"
"font":"calibri",
"size":"14"
"colour":"#B2BEB5"
"number":"3" # max number of lines that will be shown on screen 
}

frame: {
"aspect_ration":"same as video"
left_cushion=10%
right_cushion=10%
top_cushion: 10%
botton_cushion: 10%
}
]
