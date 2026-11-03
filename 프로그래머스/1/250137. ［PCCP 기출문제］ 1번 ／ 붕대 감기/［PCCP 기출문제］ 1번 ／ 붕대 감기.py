def solution(bandage, health, attacks):  # 최대체력
    t, x, y = bandage

    now_health = health  # health의 초기값
    nt = 0  # 시간 초기값
    for attack in attacks:
        at, ahp = attack  # 공격시간, 피해량

        if at - nt - 1 == 0: pass #  연속공격이면 붕대 못감음
        else:
            if now_health < health:  # health의 최대치를 넘지 않을 때만 now_health가 증가 가능
                # 초당 붕대감기 시작
                now_health = min(now_health + (at - nt - 1) * x, health)

                # 연속 추가 회복량 검사
                if (at - nt - 1) // t > 0:
                    now_health = min(now_health + y * ((at - nt - 1) // t), health)

        now_health -= ahp
        nt = at
        if now_health <= 0:
            return -1

    return now_health