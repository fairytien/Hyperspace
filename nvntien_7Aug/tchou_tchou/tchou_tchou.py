size = int(input("What is the size of your train? "))

a = " ______________________>__"
b = "|]||[]_[]_[]|||[]_[]_[]||[|"
c = r"\==o-o======o-o======o-o==/"

d = " _________________________"
e = "|]||[]_[]_[]|||[]_[]_[]||[|"
f = r"\==o-o======o-o======o-o==/"


if size > 0:
    print((d + '  ') * (size - 1) + a)
    print((e + ' ') * (size - 1) + b)
    print((f + '_') * (size - 1) + c)
elif size < 0:
    print("Don't be so negative.")
