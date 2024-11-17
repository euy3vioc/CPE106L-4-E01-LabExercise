def main():
	list = [3, 4, 5, 6, 7]
	print("Mean", mean(list))
	print("Median", median(list))
	print("Mode", mode(list))

def mean(list):     
    n = len(list)
    sumlist = sum(list)
    mean = sumlist/n
    return mean

def median(list):
    list.sort()
    n = len(list)
    if(n%2==1):
        return list[len(list)//2]
    else:
        return (list[len(list)//2-1]+list[len(list)//2])/2

def mode(list):
    frequency = {}
    for i in list:
        frequency.setdefault(i,0)
        frequency[i]+=1
    highFrequency = max(frequency.values())
    highFrequencyList = []
    for i, frq in frequency.items():
        if frq == highFrequency:
            highFrequencyList.append(i)
    return highFrequencyList

main()