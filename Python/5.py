def x3(N,Z): #function to do the assigned task
    fin=[] #final list that'll contain only the max elements of each list
    temp=[] #temporary list that'll hold the i-th list for processing
    for i in range(0,N):
        print("Length of the ",i+1,"th list please?")
        M=int(input()) #length of list to be entered
        print("Enter the elements one by one. \n") 
        for j in range(M):
            temp.append(int(input())) #accepts elements in the list
        #print(str(max(temp))+"\n") #this was just to verify whether the program works upto this point
        fin.append(max(temp))
        S1=0
        for i in range(len(fin)):
            S1+=(fin[i]**3) #f(X)=X^3
    #print(fin) #this was just to verify whether the program works upto this point
    S=S1%Z #modulo of cubes of max numbers
    return S #returns final value

def main():
    print("Enter the number of lists and the modulo value.\n")
    N=int(input())
    Z=int(input())
    print(x3(N,Z))

main()




