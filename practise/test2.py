#Maximise profits
import sys
def find_maxm_profit(arr):
    buy=0
    sell=0
    profit=0
    maxm=-sys.maxsize+1
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            profit=arr[j]-arr[i]
            if profit>maxm:
                maxm=profit
                buy=arr[i]
                sell=arr[j]
    return buy,sell,maxm

#Find maximum profit
def find_max_profit_stock(arr):
    minm=sys.maxsize-1
    buy=0
    sell=0
    mprofit=0
    for i in range(len(arr)):
        if minm>arr[i]:
            minm=arr[i] 
            print(minm)
        profit=arr[i]-minm
        if profit>mprofit:
            mprofit=profit
            buy=minm
            sell=arr[i]
    return buy,sell,mprofit

if __name__=="__main__":
    arr=[3,1,4,8,7,2,5]
    buy,sell,maxm=find_maxm_profit(arr)
    print("The buying price is:")
    print(buy)
    print("The sellling price is:")
    print(sell)
    print("The maximum profit is:")
    print(maxm)
    print("=============================================")
    arr=[3,1,4,8,7,2,5]
    buy,sell,profit=find_max_profit_stock(arr)
    print("The buying price is")
    print(buy)
    print("The selling price is:")
    print(sell)
    print("The profit is:")
    print(profit)
                
                
        