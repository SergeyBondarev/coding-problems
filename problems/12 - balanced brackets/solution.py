def is_balances(s):
    current = 0
    for ch in s:
        if ch == '(':
            current += 1
        if ch == ')':
            current -= 1
        if current < 0:
            return False
    return current == 0
