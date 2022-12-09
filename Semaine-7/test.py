def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

def foo(name, /, **kwds):
    for key, value in kwds.items():
        print(f"{key} - {value}")

foo(1, **{'name': 2, 'data' : [1,2,3]})
foo(1, name = 2, data = [2, 3, 4])


def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")