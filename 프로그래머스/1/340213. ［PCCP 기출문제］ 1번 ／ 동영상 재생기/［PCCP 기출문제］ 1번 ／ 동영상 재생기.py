def solution(video_len, pos, op_start, op_end, commands):
    video_s = trans_to_seconds(video_len)
    pos_s = trans_to_seconds(pos)
    op_start_s = trans_to_seconds(op_start)
    op_end_s = trans_to_seconds(op_end)
    
    for command in commands:
        if op_start_s <= pos_s <= op_end_s:
            pos_s = op_end_s
        if command == "prev":
            if pos_s < 10:
                pos_s = 0
            else:
                pos_s -= 10
        if command == "next":
            if pos_s + 10 >= video_s:
                pos_s = video_s
            else:
                pos_s += 10
        if op_start_s <= pos_s <= op_end_s:
            pos_s = op_end_s
            
                
    return f"{pos_s // 60 :02d}:{pos_s % 60 :02d}"

def trans_to_seconds(text: str):
    m, s = map(int, text.split(":"))
    return m * 60 + s