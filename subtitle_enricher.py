import ass, re, numpy

with open("vocals.ass", encoding='utf_8_sig') as f:
    doc = ass.parse(f)

print (len(doc.events))
print (doc.events[0].text)

def check_event_ends_with_brace(doc, i):
    if 0 <= i < len(doc.events):
        return doc.events[i].text.endswith('}')
    else:
        raise IndexError("Index out of range")

result=check_event_ends_with_brace(doc,10)
print(result)


'''
for i in range(1, len(doc.events)):
            j=0
            if (doc.events[i].text)
            previous_text = doc.events[i-1].text            
            current_text = doc.events[i].text

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
    a. No previous line ending with }- concat (/n, current line)
    b. Previous lines ends with }, then concat(previous line, /n, current line)  

'''
