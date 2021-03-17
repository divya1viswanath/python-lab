d1={"a":100,'b':200}
d2={"x":300,'y':200}
print("Dictionary1=",d1)
print("Dictionary2=",d2)
d=d1.copy()
d.update(d2)
print("Merged dictionary is",d)

