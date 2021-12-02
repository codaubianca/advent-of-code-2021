import day01.test_day01 as day1
import day02.test_day02 as day2

def test_day01():
    #part one
    day1.test_count_increases_short_one()
    day1.test_count_increases_short_two()
    day1.test_count_increases_short_three()
    day1.test_count_increases_long()

    #part two
    day1.test_count_increases_per_windows_short_one()
    day1.test_count_increases_per_windows_short_two()
    day1.test_count_increases_per_windows_short_three()
    day1.test_count_increases_per_windows_long()

def test_day02():
    day2.test_calculate_submarine_position_short()
    day2.test_calculate_submarine_position_long()

def main():
    #test_day01()
    test_day02()


if __name__ == '__main__':
    main()