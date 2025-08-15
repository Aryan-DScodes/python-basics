#MY CODE
# import os
# os.chdir("C:/Users/aryan/trial_files")
# print(os.listdir(),"\n")

# i=1
# for filename in os.listdir():
#     if filename.endswith(".mp3"):
#         os.rename(filename,f"{i}.mp3")
#         i=i+1

# print(os.listdir(),"\n")

#efficient code by gpt
import os

os.chdir("C:/Users/aryan/trial_files")
mp3_files = [f for f in listdir() if f.endswith(".mp3")]

for i, filename in enumerate(mp3_files, start=1):
    rename(filename, f"{i}.mp3")

print(os.listdir())
