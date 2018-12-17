f1 = open('textfile1.txt', 'r', encoding="utf-8")
txt1 = f1.read()
words = txt1.split()
inversed = [w[::-1] for w in words]
txt2 = ' '.join(inversed)
f2 = open('textfile2.txt', 'w', encoding="utf-8")
f2.write(txt2)
f1.close()
f2.close()
