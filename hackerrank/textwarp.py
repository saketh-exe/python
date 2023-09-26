import textwrap

def wrap(string, max_width):
    q = " "
    d = 0
    for i in range(len(string)):
        c = i*max_width
        v = (string[d:c]+"\n")
        q = q + v
        d = c
        
    q = q.strip()    
    return  q

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)