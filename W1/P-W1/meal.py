def main():
    duration = input("What time is it? ")
    duration = convert(duration)

    if 7.0 <= duration <= 8.0:
        print("Breakfast time")
    elif 12.0 <= duration <= 13.0:
        print("Lunch time")
    elif 18.0 <= duration <= 19.0:
        print("Dinner time")
    else:
        print()


def convert(time):
    hour, minutes = time.split(":")
    minutes = float(minutes) / 60
    time = round(float(hour) + float(minutes))
    return time



if __name__ == "__main__":
    main()