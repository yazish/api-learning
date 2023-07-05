def greet(func):
    def mfx():
        print("Hello world")
        func()
    return mfx

# @greet
def howAreYou():
    print("How are you")


greet(howAreYou)()