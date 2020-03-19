def formatter(expr):
    for c in expr:
        if c == "+" or c == "-" or c == "/" or c == "*":
            print(f" {c} ", end="")
        else:
            print(c, end="")

expr = input()
formatter(expr)