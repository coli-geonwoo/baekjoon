from collections import defaultdict


def find_parent(a):
    if(a!= friendship[a]):
        friendship[a]= find_parent(friendship[a])
    return friendship[a]

def union_parent(a,b):
    a= find_parent(a)
    b= find_parent(b)

    if(a<b):
        group_size[a] +=group_size[b]
        friendship[b]=a
        return group_size[a]
    else:
        group_size[b]+=group_size[a]
        friendship[a]=b
        return group_size[b]



n = int(input())

for _ in range(n):
    m= int(input())
    friendship = defaultdict(str)
    group_size = defaultdict(int)

    result=0
    for _ in range(m):
        a,b = input().split()
        if(friendship[a]==""):
            friendship[a]=a
        if(friendship[b]==""):
            friendship[b]=b
        if(group_size[a]==0):
            group_size[a]=1
        if(group_size[b]==0):
            group_size[b]=1

        pa = find_parent(a)
        pb = find_parent(b)
        # print(a,b, pa, pb)
        # print(group_size)
        # print(friendship)
        # print()

        if(pa==pb):
            print(group_size[pa])
            continue
        print(union_parent(a,b))


    #print(result)
