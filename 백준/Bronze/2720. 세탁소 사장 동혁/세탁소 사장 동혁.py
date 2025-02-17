
N = int(input())

Quarter = 25
Dime= 10
Nickel= 5
Penny = 1
Q_cnt,D_cnt,N_cnt,P_cnt = 0,0,0,0

answer_list = []
for _ in range(N) :
      pay = int(input())
      Q_cnt,D_cnt,N_cnt,P_cnt = 0,0,0,0
      while pay-Quarter >= 0 :
            pay -= Quarter
            Q_cnt+= 1

      while pay-Dime >= 0 :
            pay -= Dime
            D_cnt += 1

      while pay-Nickel >= 0 :
            pay -= Nickel 
            N_cnt += 1

      while pay-Penny >= 0 :
            pay-=Penny 
            P_cnt += 1

      print(str(Q_cnt)+" "+str(D_cnt)+" "+ str(N_cnt)+" "+ str(P_cnt))