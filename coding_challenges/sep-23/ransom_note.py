# test file
import time, re, sys
from os import path

match_string = "Hello, world" if len(sys.argv) == 1 else sys.argv[1]
text_path = "Hamlet.txt" if len(sys.argv) < 3 else sys.argv[2]

print(f"I have a message to send. I want to say '{match_string}', " +
      f"but I don't want to type it out.")
time.sleep(3)
print(f"To have a bit of fun, I'll cut each letter out of " + 
      f"{path.splitext(path.split(text_path)[1])[0]}, my favourite piece of writing.\n")
time.sleep(3)

with open(text_path, "r") as f:
    text = f.read()

text = re.sub(r"\r?\n+", " / ", text)
text = re.sub(r"\s+", " ", text)

missing = re.sub(" ", "", match_string)
ransom = ""
sticky = "".join([" " *len(missing)*3])

print("\r" + sticky + "> " + text[0:98-len(sticky)], end = "\r")
time.sleep(3)
for i in range(len(text)):
    end_pos = len(text) if len(text) < i + 100 else i + 100
    end_char = "\r" if end_pos - i == 100 else (100-(end_pos-i))*" "+"\r"
    print("\r" + sticky + "> " + text[i:end_pos-len(sticky)-2], end = end_char)
    time.sleep(0.05)
    if len(missing) == 0: 
        time.sleep(.8)
        break
    if text[i] in missing:
        time.sleep(0.5)
        print("\r" + sticky + "> " + text[i] + "|" + text[i+1:end_pos-len(sticky)-3], end = end_char)    
        time.sleep(0.3)
        print("\r" + sticky + "> " + "|" + text[i] + "|" + text[i+1:end_pos-len(sticky)-4], end = end_char)    
        ransom += text[i]
        missing = re.sub(re.escape(text[i]), "", missing, count = 1)
        sticky = "".join(["[","][".join([*ransom]), "]", " "*len(missing)*3, ])
        time.sleep(0.5)
        print("\r" + sticky + "> |▓|" + text[i+1:end_pos-len(sticky)-4], end = end_char)    
        time.sleep(1)
print(f"\r{' '*101}\r{sticky}", end = "\r")

if len(missing) == 0:
    sorted = ""
    for char in match_string:
        if char != ransom[0]: time.sleep(1)
        ransom = re.sub(re.escape(char), "", ransom, count = 1) if char != " " else ransom
        sorted += char
        out = sorted + ransom
        sticky = "".join(f"[{c}]" if c != " " else f"{c}" for c in out) 
        print("\r" + sticky, end = "\r")
    print(f"\n\nPerfect! Now I just need some glue and glitter...")
else:
    print(f"\n\nDarn, I guess I need to find some more letters somewhere...")
