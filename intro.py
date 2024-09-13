
# console.log("Hello from python")
print("hello from python")


# let variable = 1;
variable = 1
variable = True
variable = "hello"

# known as list here 
array = [1,2,3,4,5] 

print(array[0])

array.append((6))

print(array)
array.pop()

print(array)


dict = {
    "name": "kevin",
    "last_name": "reyes"
}

print(dict['name'])

# for(i=0; i<size; i++){
  # let temp = array[1]}

for elements in dict:
        print ("kevin")

# use inditation to set start and end 
for i in dict:
        print(dict[i])


# functions


def print1():
    print("hello from python")

# excute function 

print1()


def sayGoodbye(name, last_name):
       print(f"Goodbye {name} {last_name}")


sayGoodbye('reyes', 'kevin')