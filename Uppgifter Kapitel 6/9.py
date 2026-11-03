from sys import exit
from time import sleep

queue = ["Adam", "Eva", "Kerstin", "Gertrud", "Tobias"]

while queue:
    print(f"Nu betjänas {queue[0]}")
    print(f"I kön: {", ".join(queue[1:])}")
    input()
    queue.pop(0)

print("Alla kunder betjänade")
sleep(1)
exit()