def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}

    for calling in callings:
        winning = rank[calling]  # 추월한 선수의 현재 위치
        loser = players[winning - 1]  # 바로 앞 선수의 이름
        losing = winning - 1

        players[losing], players[winning] = players[winning], players[losing]

        rank[calling] -= 1
        rank[loser] += 1

    return players