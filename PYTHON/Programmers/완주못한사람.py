participant = ["mislav", "stanko", "mislav", "ana","cho"]
completion = ["stanko", "ana", "mislav","cho"] 

completion.sort()
participant.sort()
for c, p in zip(completion, participant):
    if c !=  p:
        answer = p
        answer
        break
    else :
        answer =  participant[-1]

print(answer)