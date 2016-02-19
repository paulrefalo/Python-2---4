"""
Filter file contents using a sequence of generators.
"""
def nocomment(f):
    "Gen the non-comment lines of a file"
    for line in f:
        if not line.startswith('#'):
            yield line
            
def nospaces(f):
    "Gen the lines of a file without leading or trailing spaces"
    for line in f:
        yield line.strip()
        
def noblanks(f):
    "Gen the non-blank lines of a file"
    for line in f:
        if line:
            yield line
            
if __name__ == "__main__":
    for line in nocomment(noblanks(nospaces(open("py08-01.txt")))):
        print(line)
