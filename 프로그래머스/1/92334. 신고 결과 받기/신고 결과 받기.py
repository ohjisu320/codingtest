def solution(id_list, report, k):
    report = set(report)
    reported_ids = dict()
    stop_ids = set()

    answer = [0] * len(id_list)

    for r in report:
        _, to_id = r.split(" ")  # 신고 당한 사람 횟수 세기
        reported_ids[to_id] = reported_ids.get(to_id, 0) + 1  # 신고 수 누적하기
        if reported_ids.get(to_id, 0) >= k:  # 딕셔너리에 신고당한 사람의 신고 수가 k개 이상이면
            stop_ids.add(to_id)  # 정지 아이디 리스트에 넣기
    for r in report:
        from_id, to_id = r.split(" ")  # 신고 한 사람의 결과 메일 개수 세보기
        if to_id in stop_ids:  # from이 신고한 to가 정지된 아이디 리스트에 있다면
            index = id_list.index(from_id)  # 신고자의 리스트 자리에
            answer[index] += 1  # 결과메일 + 1

    return answer