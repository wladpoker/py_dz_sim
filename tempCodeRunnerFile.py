old_name = "Петров,Петр,222,описание Петрова"

new_name = "Васичкина,Василиса,333,описание Васичкиной"

with open("phon.txt", "rt", encoding='utf-8') as f:
    lines = f.readlines()
with open("phon.txt", "wt", encoding="utf-8") as f:
    for line in lines:
        f.write(line.replace(old_name, new_name))
    