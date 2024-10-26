import os

file_eng = open("./data_eng.txt").read()
file_is = open("./data_is.txt").read()
out = ""

paragraphs_eng = file_eng.split("\n\n")
paragraphs_is = file_is.split("\n\n")

for each_paragraph in paragraphs_eng:
    leading_nr = float(each_paragraph[0:2])
    if leading_nr < 10:
        each_paragraph = each_paragraph[3:]
    else:
        each_paragraph = each_paragraph[4:]
    
    out += each_paragraph + "\n\n"
    

open("./data_eng_clean.txt", "w").write(out)

out = ""
for each_paragraph in paragraphs_is:
    leading_nr = float(each_paragraph[0:2])
    if leading_nr < 10:
        each_paragraph = each_paragraph[3:]
    else:
        each_paragraph = each_paragraph[4:]
    
    out += each_paragraph + "\n\n"
    

open("./data_is_clean.txt", "w").write(out)

