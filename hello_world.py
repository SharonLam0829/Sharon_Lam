def hello(to):
    return f"Hello{to}!"

def goodbye(to):
    return f"Good Bye {to}!"

def main():
    user = input("Name:")
    print(hello(user))
    print(goodbye(user))

if __name__== '__main__':
    main()