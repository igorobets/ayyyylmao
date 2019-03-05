import random
number = random.choice([i for i in range(1, 101)])
start = 0
end = 101
i=0
while True:
    i+=1
    guess = int((start+end)/2)
    if guess==number:
        break
    elif guess < number:
        start = guess
    elif guess > number:
        end = guess
print(number,  guess, i)

