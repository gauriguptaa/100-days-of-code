import pandas as pd
if __name__ == '__main__':
    name = input("Enter your name? ").upper()
    nato_alphabet_file = pd.read_csv("nato_phonetic_alphabet.csv")
    df = pd.DataFrame(nato_alphabet_file)
    nato_list = [row.code for letter in name for(index, row) in df.iterrows() if row.letter == letter]
    print(nato_list)

