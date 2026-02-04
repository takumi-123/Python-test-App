print("hello world")

#greet関数
def greet():
    print("こんにちは")
greet()

#print_name関数
def print_name(name):
    print(f"私の名前は{name}です")
print_name("佐藤")

#get_greet関数
def get_greet():
    return "おはようございます"
mog = get_greet()
print(mog)

#add関数
def add(a, b):
    return a + b
result = add(4, 4)
print(result)