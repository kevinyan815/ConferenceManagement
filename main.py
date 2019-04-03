# -*- coding=UTF-8 -*-

from Session import Session
from Talk import Talk

def build_talks_sesions():
    """Initialize all talks and sesssions objects
    """
    sessions = list(map(lambda x: Session(x), [180, 240, 180, 240]))

    talks = []
    with open('input.txt') as f:
        for line in f:
            talks.append(Talk(line.strip()))

    return sessions, talks


def arrange_conferences(talks, sessions):
    """arrange talks in sessions
    """
    talk = talks.pop(0)

    sessions.sort(key=lambda x: x.balance, reverse=True)
    sessions[0].add(talk)
    if len(talks) == 0:
        return sessions
    return arrange_conferences(talks, sessions)

def format_time_number(number):
    """Format time's number
    example: given 1 will return 01, given 10 will return 10
    """
    if int(number) < 10:
        return '0' + str(number)
    return str(number)

def print_schedule(sessions):
    """Print conference schedule
    """
    sessions.sort(key=lambda x: x.limit, reverse=False)
    am = [None, None]
    pm = [None, None]
    am[0], am[1], pm[0], pm[1] = sessions
    for i in range(2):
        print('Track' + str(i + 1))
        minutes = 9 * 60
        for talk in am[i].talk_list:
            h = format_time_number(minutes // 60)
            m = format_time_number(minutes % 60)
            print(h + ':' + m + 'AM ' + talk.name)
            minutes += talk.duration

        print('12:00PM Lunch')
        minutes = 1 * 60
        for talk in pm[i].talk_list:
            h = format_time_number(minutes // 60)
            m = format_time_number(minutes % 60)
            print(h + ':' + m + 'PM ' + talk.name)
            minutes += talk.duration
        print('05:00PM Networking Event')

def main():
    sessions, talks = build_talks_sesions()
    # sort talks by their duration
    talks.sort(key=lambda item: item.duration, reverse=True)
    # arrange talks in  these 4 sessions
    arranged_sessions = arrange_conferences(talks, sessions)
    # print schedule
    print_schedule(arranged_sessions)

if __name__ == "__main__":
    main()
