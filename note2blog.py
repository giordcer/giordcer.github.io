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
print(content)

os.chdir("/home/gc/giordcer.github.io/")
os.system("git pull")
newpath = f"/home/gc/giordcer.github.io/_posts/{filename}"
with open(newpath, "w") as fp:
    fp.write(content)
os.system(f"git add _posts/{filename}")
os.system(f"git commit -m 'Add new post: {filename}'")
os.system("git push")
