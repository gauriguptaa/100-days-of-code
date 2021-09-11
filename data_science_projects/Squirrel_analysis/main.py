import pandas
if __name__ == '__main__':
    data_dict = {"Fur Color": [], "Count": []}
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    for color in ["Gray", "Cinnamon", "Black"]:
        data_dict["Fur Color"].append(color)
        data_dict["Count"].append(sum(data["Primary Fur Color"] == color))
    squirrel_data_dict = pandas.DataFrame(data_dict)
    squirrel_data_dict.to_csv("squirrel_count.csv")
