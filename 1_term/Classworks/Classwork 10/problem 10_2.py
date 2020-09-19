# 4842
a = list(map(str, input().split()))
b = list(map(str, input().split()))


form = []
for i in range(len(a)):
    form.append([a[i], b[i]])

english_to_russian = dict(form)
print(english_to_russian)

morf = []
for i in range(len(a)):
    morf.append([b[i], a[i]])

russian_to_english = dict(morf)
print(russian_to_english)

