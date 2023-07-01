def add(fn : list , ln: str | None = None):
    # ln = ln.capitalize()
    for i in fn:
        print(i)
    return ln


fn = [1,2,'jin']
ln = "gates is here"

print(add(fn))