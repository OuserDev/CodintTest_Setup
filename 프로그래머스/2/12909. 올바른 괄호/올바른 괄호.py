
def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        if i == ')':
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0