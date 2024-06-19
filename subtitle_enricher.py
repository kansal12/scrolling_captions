import ass, re, numpy

with open("vocals.ass", encoding='utf_8_sig') as f:
    doc = ass.parse(f)

print (len(doc.events))

#print(re.sub(r'\{[^}]*\}', '', doc.events[1].text))




def find_closest_brace(lines):
    brace_line = -1
    closest_brace_lines = []

    for i in range(len(lines)):
        # Check if the current line ends with '}'
        if lines[i].strip().endswith('}'):
            brace_line = i

        # Add the line number of the closest brace above
        closest_brace_lines.append(brace_line)

    return closest_brace_lines

1. check previous line, if it ends with }
    a. No previous line- concat (/n, current line)If there is no prevous line, 
    b. Previous lines does not end with }, then  


