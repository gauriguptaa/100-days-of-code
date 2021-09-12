#  You are going to use Dictionary Comprehension to create a dictionary called result that takes
#  each word in the given sentence and calculates the number of letters in each word.
if __name__ == '__main__':
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    results = {word: len(word) for word in sentence.strip('", ?').split(" ")}
    print(results)
