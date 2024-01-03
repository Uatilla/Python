#print("Hello," + name, sep=" | ")
#print("Hello,",name, sep=" | ")
#print(name)
#print("Hello, {}!". format(name))

#print(f"Hello, {name}!")

def main():
    name = input("What's your name? ").strip().title()
    hello(name)
    
def hello(nm):
    print(f"Hello, nice to meet you! {nm}")

main()