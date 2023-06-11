import requests
import os


def main():
    is_running_program = True
    while is_running_program:
        clear_console()
        display_main_menu()
        start_user_interaction(generate_user_prompt("Tracking Number: "))
        is_running_program = is_still_running_program()


def clear_console() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def display_main_menu() -> None:
    print("#########################")
    print("# PosLaju Tracker v0.1 #")
    print("# Coded By Noor Aiman  #")
    print("########################\n")


def generate_user_prompt(message: str) -> str:
    return input(message).upper()


def start_user_interaction(tr_num) -> None:
    if is_valid_tracking_number_format(tr_num):
        start_tracking(tr_num)
    else:
        print("Invalid Tracking Number Format.")


def is_valid_tracking_number_format(tr: str) -> bool:
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


def start_tracking(tr_num: str) -> None:
    url = "https://ttu-svc.pos.com.my/api/trackandtrace/v1/request"
    response_body = send_post_request(url, tr_num)
    extracted_data = extract_data_from_response(response_body)
    display_tracker_result(extracted_data)


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


def extract_data_from_response(response_body: dict) -> dict:
    data_from_body = response_body.get("data", [{}])
    return data_from_body[0] if data_from_body is not None else {}


def display_tracker_result(data: dict) -> None:
    display_tracker_result_header(data)
    for idx, ele in enumerate(data["tracking_data"]):
        display_tracker_result_children(len(data["tracking_data"]) - idx, ele)


def generate_tracker_result_header(data: dict) -> str:
    header = "\n======================================\n"
    header += f"Your tracking number: {data['connote_id']}\n"
    header += f"Process status: {return_value(data, 'process_status')}\n"
    header += "======================================\n"
    return header


def display_tracker_result_header(data: dict):
    header = generate_tracker_result_header(data)
    print(header)


def return_value(dict_data: dict, key: str) -> str:
    value = dict_data.get(key, "N/A")
    return value if len(value) > 0 else "N/A"


def generate_tracker_result_children(count: int, dict_data: dict) -> str:
    result = f"\nTracking #{count}\n"
    result += "--------------------------------\n"
    result += f"date: {return_value(dict_data, 'date')}\n"
    result += f"process: {return_value(dict_data, 'process')}\n"
    result += f"process_summary: {return_value(dict_data, 'process_summary')}\n"
    result += f"office: {return_value(dict_data, 'office')}\n"
    return result


def display_tracker_result_children(count: int, dict_data: dict) -> str:
    output = generate_tracker_result_children(count, dict_data)
    print(output)


def is_still_running_program() -> bool:
    exit_answer = generate_user_prompt("\nDo You Want To Continue? (Y/N):")
    return exit_answer == "Y"


if __name__ == "__main__":
    main()
