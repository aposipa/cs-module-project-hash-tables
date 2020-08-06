
def word_count(s):
    # Your code here
    ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    
    count = {}
    s = ' '.join(s.split())
    s = ''.join([c for c in s if c not in ignore]).lower()
    if s == '':
        return {}
    words = s.split(" ")
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))