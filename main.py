file = None
with open('activity.csv') as data:
    file = data.read()


def resultDict(file):
    result = {}

    for i in range(1, len(file.split('\n'))):  # iterate thorugh line number
        # create list of data of each line
        data = file.split("\n")[i].split(",")
        if len(data) < 3:  # skip if entry is less than 3
            continue
        if data[1] in result:
            if data[0] != 'NA':
                result[data[1]][0] += int(data[0])
            else:
                result[data[1]][1] += 1
                result[data[1]][2][data[2]] = 0
        else:
            if data[0] != 'NA':
                result[data[1]] = [int(data[0]), 0, {data[2]: data[0]}]
            else:
                result[data[1]] = [0, 0, {data[2]: 0}]
    return result, data


def findMean(result, data):
    mean = result[data[1]][0] / len(data[2].keys)
    return mean


def findMedian(result, data):
    sorted_dict = result[data[1]][2]
    length = 0
    for value in sorted_dict.values():
        length += value
    half = length / 2
    sum_var = 0
    # finds the index of the middle of the dataset
    for val in sorted_dict.values():
        if half - sum_var > 0:
            sum_var += val
        else:
            break
    index = (list(sorted_dict.values()).index(val))
    # returns the median based off some characteristics of the dataset
    if sum(list(sorted_dict.values())[index:]) != sum(list(sorted_dict.values())[:index]):
        if sum(list(sorted_dict.values())[index:]) > sum(list(sorted_dict.values())[:index]):
            median = list(sorted_dict.keys())[index]
        else:
            median = list(sorted_dict.keys())[index - 1]
    else:
        median = (list(sorted_dict.keys())[
                  index - 1] + list(sorted_dict.keys())[index]) / 2
    return median


print(resultDict(file))

# return(median)
# list per line

# data[1] --> date
# data[0] --> steps
# data[2] --> interval


# mean = totalSteps/len(data[2].keys)
# median = data[2][len(data[2].keys) + 1/2] if data[2].keys % 2 != 0 else
# median = None
# if len(data.keys) % 2 == 0:
#     median = len(data.keys) / 2 + len
