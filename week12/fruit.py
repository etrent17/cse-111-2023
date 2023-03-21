def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")
        print(f"reversed: {fruit_list.reverse()}")
        fruit_list.append("orange")
        print(f"append orange: {fruit_list}")
        fruit_list.insert(1, "cherry")
        print(f"insert cherry: {fruit_list}")
        fruit_list.remove("banana")
        print(f"remove banana: {fruit_list}")
        fruit_list.pop(-1)
        print(f"pop orange: {fruit_list}")
        fruit_list.sort()
        print(f"sorted: {fruit_list}")
        fruit_list.clear()
        print(f"clear: {fruit_list}")
    except TypeError as e:
        print(f"You suck, {e}")
                   
# Copy code to the clipboar\
if __name__ == "__main__":
    main()