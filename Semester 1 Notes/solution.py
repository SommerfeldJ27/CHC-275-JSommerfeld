import math

def sol(arr):
    total_cost = 0
    while len(arr) > 1:
        sum = arr[0] + arr[-1]
        cost = math.ceil((arr[0] + arr[-1])/(arr[-1] - arr[0] + 1)) 
        arr.pop(0)
        arr.pop(-1)
        arr.append(sum)
        total_cost += cost
        
    return total_cost

def main():
    data = [3,4,8,1,5,4]
    print(sol(data))
    
if __name__ == "__main__":
    main()
    
    