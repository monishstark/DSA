def func(pos,cards,t,te):
    if pos>len(cards):
        return
    if pos==len(cards):
    
        if eval(te[:len(te)-1])==24:
            print(te[:len(te)-1])
        if t==24:
            print(t)
        return
    func(pos+1,cards,t+cards[pos],te+str(cards[pos])+"+")
    func(pos+1,cards,t-cards[pos],te+str(cards[pos])+"-")
    func(pos+1,cards,t*cards[pos],te+str(cards[pos])+"*")
    func(pos+1,cards,t/cards[pos],te+str(cards[pos])+"/")
    

cards = [4,1,8,7]
func(0,cards,0,"")