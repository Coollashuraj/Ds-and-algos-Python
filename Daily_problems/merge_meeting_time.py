def merge_meeting_time(arr):
    #[(2,4) (5,6) (3,3.30)]
    sorted_arr= sorted(arr)
    con_meeting = [arr[0]]

    for meeting_start,meeting_end in arr[1:]:
        last_meeting_start,last_meet_end =  con_meeting[-1]
        if meeting_start <= last_meet_end:
            con_meeting[-1] = (last_meeting_start, max(last_meet_end,meeting_end))
        else:
            con_meeting.append((meeting_start,meeting_end))
    return con_meeting


if __name__ == '__main__':
    l= merge_meeting_time([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    print(l)



