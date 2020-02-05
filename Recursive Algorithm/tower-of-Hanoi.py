
def solution(n, sourceTower, destinationTower, tempTower):
    global counter
    if n == 0:
        return "if you have 0 disks then there is a no tower of disks"
    if n == 1:
        counter+=1
        print(counter,"Move disk 1 Source Tower",sourceTower,"Desination Tower",destinationTower)
    else:
        solution(n-1,sourceTower,tempTower,destinationTower)
        counter+=1
        print (counter,"Move disk",n,"Source Tower",sourceTower,"Desination Tower",destinationTower)
        solution(n-1,tempTower, destinationTower, sourceTower)

counter = 0
Number_of_Disks = 5
solution(Number_of_Disks,"A","B","C")

print("Number of move Required:", pow(2,Number_of_Disks)-1)