from ArrayStack import ArrayStack

def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        print(S.show_stack())
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

print(is_matched("({[])}"))
print(is_matched("[()[(())]]"))