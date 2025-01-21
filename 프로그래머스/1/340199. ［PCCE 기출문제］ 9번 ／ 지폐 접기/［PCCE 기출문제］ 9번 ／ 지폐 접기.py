def solution(wallet, bill):
    answer = 0
    wallet.sort()
    bill.sort()
    while wallet[0] < bill[0] or wallet[1] < bill[1] :
        if bill[0] > bill[1] :
            bill[0] = int(bill[0]/2)
            pass
        else :
            bill[1] = int(bill[1]/2)
            pass
        answer +=1
        wallet.sort()
        bill.sort()
    return answer