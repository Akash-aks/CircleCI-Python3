def to_upper(name):
    return name.upper()

def say_hello(name):
    print("Hello,",name)

if __name__ == '__main__':
    name="Akash"
    say_hello(name)
    up = to_upper(name)
    print(up)