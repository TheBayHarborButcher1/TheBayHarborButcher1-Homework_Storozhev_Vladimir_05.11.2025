from datetime import datetime


def parse_date_1(date_str):
    return datetime.strptime(date_str, '%A, %B %d, %Y')


def parse_date_2(date_str):
    return datetime.strptime(date_str, '%A, %d.%m.%y')


def parse_date_3(date_str):
    return datetime.strptime(date_str, '%A, %d %B %Y')


def main():
    dates_example = [
        "Wednesday, October 2, 2002",
        "Friday, 11.10.13",
        "Thursday, 18 August 1977"
    ]

    for date_str in dates_example:
        date_obj = None
        try:
            if ',' in date_str and '.' in date_str:
                date_obj = parse_date_2(date_str)
            elif any(month in date_str for month in
                     ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']):
                if date_str[-4:].isdigit():
                    date_obj = parse_date_1(date_str)
                else:
                    date_obj = parse_date_3(date_str)
            if date_obj:
                print(date_obj)
        except ValueError:
            continue

    while True:
        user_input = input().strip()

        if user_input == 'q':
            break

        result = None
        try:
            if ',' in user_input and '.' in user_input:
                result = parse_date_2(user_input)
            elif any(month in user_input for month in
                     ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']):
                if user_input[-4:].isdigit():
                    result = parse_date_1(user_input)
                else:
                    result = parse_date_3(user_input)
            if result:
                print(result)
        except ValueError:
            continue


if __name__ == "__main__":
    main()