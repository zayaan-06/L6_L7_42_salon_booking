import math


def parse_booking(text):
    if not isinstance(text, str) or ":" not in text:
        return None
    parts = text.split(":")
    if len(parts) != 2:
        return None
    service, minutes_str = parts[0].strip(), parts[1].strip()
    if not service:
        return None
    try:
        minutes = float(minutes_str)
    except ValueError:
        return None
    if not math.isfinite(minutes) or minutes <= 0:
        return None
    return service.title(), minutes


def duration_average(durations_csv):
    if not isinstance(durations_csv, str) or not durations_csv.strip():
        return 0
    values = []
    for token in durations_csv.split(","):
        token = token.strip()
        if not token:
            continue
        try:
            val = int(token)
            if val > 0:
                values.append(val)
        except ValueError:
            return 0
    if not values:
        return 0
    return sum(values) // len(values)


def payable_bill(text):
    if not isinstance(text, str) or "|" not in text:
        return 0.0
    parts = text.split("|")
    if len(parts) != 2:
        return 0.0
    try:
        bill = float(parts[0].strip())
        discount = float(parts[1].strip())
    except ValueError:
        return 0.0
    if not (math.isfinite(bill) and math.isfinite(discount)):
        return 0.0
    if bill < 0 or discount < 0:
        return 0.0
    total = bill * 1.18 - discount
    if not math.isfinite(total):
        return 0.0
    return max(total, 0.0)


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter service:duration in min (e.g. haircut:45): ")
    result = parse_booking(user_input)
    print("Service and Duration:", result)

    print("\n==== Running duration_average ====")
    user_input = input("Enter durations as CSV (e.g. 30,45,60): ")
    result = duration_average(user_input)
    print("Average Duration:", result)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 800|100): ")
    result = payable_bill(user_input)
    print("Payable Bill:", result)

if __name__ == "__main__":
    main()
