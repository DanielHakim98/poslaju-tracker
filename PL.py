import requests
import os


def main():
    display_main_menu()
    tr_num = generate_prompt("Tracking Number: ")
    if is_tracking_number_valid(tr_num):
        url = "https://ttu-svc.pos.com.my/api/trackandtrace/v1/request"
        response_body = send_post_request(url, tr_num)
        data = extract_data_value(response_body)
        display_tracker_result(data)
    else:
        print(
            "Wrong Tracking Number format. Please ensure the tracking number is correct."
        )
    is_exiting()


def display_main_menu():
    print("#########################")
    print("# PosLaju Tracker v0.1 #")
    print("# Coded By Noor Aiman  #")
    print("########################\n")


def generate_prompt(message: str) -> str:
    return input(message).upper()


def is_tracking_number_valid(tr: str) -> bool:
    return len(tr) >= 13 and tr[0:2] in [
        "EE",
        "EH",
        "EP",
        "ER",
        "EN",
        "EM",
        "PL",
        "FD",
    ]


def send_post_request(url: str, tracking_number: str) -> dict:
    try:
        response = requests.post(
            url, headers=get_http_headers(), json=get_http_payload(tracking_number)
        )
        return response.json()
    except requests.RequestException as error_request:
        print(
            "There is an error while sending th request.\n Eror details: ",
            error_request,
        )


def get_http_headers() -> dict:
    return {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
    }


def get_http_payload(tracking_number: str) -> dict:
    return {"connote_ids": [tracking_number], "culture": "en"}


def extract_data_value(response_body):
    return response_body["data"][0]


def display_tracker_result(data):
    print("\n======================================")
    print("Your tracking number: ", data["connote_id"])
    print("Process status: ", data["process_status"])
    print("======================================")
    is_available = lambda d, k: d.get(k, "N/A")
    for idx, ele in enumerate(data["tracking_data"]):
        print(f"\nTracking #{len(data['tracking_data']) -idx }")
        print("--------------------------------")
        print("date: ", is_available(ele, "date"))
        print("process: ", is_available(ele, "process"))
        print("process_summary: ", is_available(ele, "process_summary"))
        print("office:", is_available(ele, "office"))


def is_exiting():
    exit_answer = generate_prompt("\nDo You Want To Continue? (Y/N):")
    if exit_answer == "Y":
        clear_console()
        main()


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
