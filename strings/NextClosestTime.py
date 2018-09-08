from itertools import product

"""
Given a time represented in the format "HH:MM", form the next closest 
time by reusing the current digits. There is no limit on how many times 
a digit can be reused. 

You may assume the given input string is always valid. For example, 
"01:34", "12:09" are all valid. "1:34", "12:9" are all invalid. 

Example 1:

Input: "19:34" Output: "19:39" Explanation: The next closest time 
choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later. 
It is not 19:33, because this occurs 23 hours and 59 minutes later. 

Example 2: 

Input: "23:59" Output: "22:22" Explanation: The next closest time 
choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the 
returned time is next day's time since it is smaller than the input time 
numerically. 
"""


def next_closest_time(time):
    start = ans = int(time[:2]) * 60 + int(time[3:])
    min_elapsed = minutes_in_day = 24 * 60
    allowed = {int(x) for x in time if x != ':'}

    for h0, h1, m0, m1 in product(allowed, repeat=4):
        hour = h0 * 10 + h1
        minute = m0 * 10 + m1

        if hour < 24 and minute < 60:
            cur_mins = hour * 60 + minute
            cur_elapsed = (cur_mins - start) % minutes_in_day
            if 0 < cur_elapsed < min_elapsed:
                ans = cur_mins
                min_elapsed = cur_elapsed

    return "{:02d}:{:02d}".format(*divmod(ans, 60))


def main():
    print(next_closest_time("19:34"))


if __name__ == "__main__":
    main()
