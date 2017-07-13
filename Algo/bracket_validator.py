
def validate(s):
    """
    Naive solution.
    O(n) for the loop looking at each character
    O(1) for each set lookup in first conditional of the loop
    O(1) for equality checking
    O(1) for each dict lookup
    O(1) for each append
    O(1) for each pop

    Final time complexity: O(n)
    Final space complexity: O(n) as a very worst-case scenario to hold the list
    """
    looking_for_match = []
    matches = {"{":"}", "[":"]", "(":")"}
    match = None
    for c in s:
        if c in {"{", "[", "("}:
            if match:
                looking_for_match.append(match)
            match = c

        elif match:
            if c == matches[match]:
                if looking_for_match:
                    match = looking_for_match.pop()
                else:
                    match = None
        else:
            continue ## is this best practice/a good idea?? or better to imply?

    return not match


assert(validate("{ [ ] ( ) }") == True)
assert(validate("{ [ ( ] ) }") == False)
assert(validate("{ [ }") == False)

"""
The IC solution, below, was slightly simpler; factored out match variable. DUH.
Same time/space complexity.
But might be better performance because of the early exit/short circuiting.
Similar but imptoved use of a stack to manage seen opening characters.
"""

def is_valid(code):
    openers_to_closers = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    openers = frozenset(openers_to_closers.keys())
    closers = frozenset(openers_to_closers.values())

    openers_stack = []

    for char in code:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            if not openers_stack:
                return False
            else:
                last_unclosed_opener = openers_stack.pop()

                # if this closer doesn't correspond to the most recently
                # seen unclosed opener, short-circuit, returning false
                if not openers_to_closers[last_unclosed_opener] == char:
                    return False

    return openers_stack == []
