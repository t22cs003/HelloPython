def quick_sort(data):
    
    if len(data) <=1:
        return data
    
    pivot = data.pop(0)
    
    left = [i for i in data if i <= pivot]
    
    right = [i for i in data if i > pivot]
    
    left = quick_sort(left)
    right = quick_sort(right)
    
    return left + [pivot] + right

if __name__ == '__main__':
    DATA = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

    print(f"{DATA} → {quick_sort(DATA)}")