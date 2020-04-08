class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxlen = 0
        pathlen = {0: 0}
        
        # splitlines: split '/n' from a string
        for line in input.splitlines():
            
            # lstrip() method removes any leading characters
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                # pathlen for the next name
                # 1 represent a '/' token
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
                
        return maxlen
