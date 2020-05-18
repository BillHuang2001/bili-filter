from tkinter import messagebox
import random

with open("comments.txt","r",encoding="utf-8") as fin:
    comments = fin.read()

comments = comments.split()
random.shuffle(comments)

new_comments = []
new_targets = []

try:
    for comment in comments:
        choice = messagebox.askokcancel("choice if ok or not", comment )
        if choice == True:
            new_targets.append('1')
        else:
            new_targets.append('0')

        new_comments.append(comment)
finally:
    with open("comments_clip.txt","a",encoding="utf-8") as fout1:
        with open("target_clip.txt","a",encoding='utf-8') as fout2:
            fout1.write("\n".join(new_comments))
            fout2.write("\n".join(new_targets))

    print("end")