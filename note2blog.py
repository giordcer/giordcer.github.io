from datetime import date
import os

today = date.today().strftime("%Y-%m-%d")
# print(today)
path = input("Path to note: ")
filename = os.path.basename(path)
title = filename[:-3]
filename = today + "-" + filename
frontmatter = f'---\ntitle: "{title}"\ndate: {today}\nlayout: post\n---\n'
with open(path, "r") as fp:
    content = fp.read()
content = frontmatter + content

# Find tags and replace
i = 0
tagvals = []
while i < len(content):
    tag = content[i] == "[" and content[i - 1] == "[" and content[i - 2] == "!"
    tagval = ""
    if tag:
        i += 1
        tagstart = i - 2
        while content[i] != "]":
            tagval += content[i]
            i += 1
        tagval_old = tagval[:]
        tagval = tagval.replace(" ", "_")
        # # print(tagval)
        tagvals.append((tagval_old[:], tagval[:]))
        tagend = i + 1
        newtag = f"![{tagval[:]}](/assets/{tagval[:]})"
        # print("newtag", newtag)
        # input("newtag")
        content = content[: tagstart - 1] + newtag + content[tagend + 1 :]

    i += 1
#   move files to /assets
for tag in tagvals:
    os.system(
        f'cp /home/gc/Documents/main/Images/"{tag[0]}" /home/gc/giordcer.github.io/assets{tag[1]}'
    )

# print(content)
# input("pause")

# os.chdir("/home/gc/giordcer.github.io/")
os.system("git pull")
with open(f"/home/gc/giordcer.github.io/_posts/{filename}", "w") as fp:
    fp.write(content)
os.system("git add --all")
os.system(f"git commit -m 'Add new post: {filename}'")
os.system("git push")
