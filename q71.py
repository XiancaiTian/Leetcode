## concept: use prev and stack to save the previous results
class Solution:
    def simplifyPath(self, path: str) -> str:
        prev = ''
        stack = []
        for word in path+'/':
            if prev and word == '/':
                if prev =='..' and stack:
                    stack.pop()
                elif prev != '.' and prev != '..':
                    stack.append(prev)
                prev = ''
            elif word !='/':
                prev += word
        return '/' +'/'.join(stack)
