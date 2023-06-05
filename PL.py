import requests
import os


# Clear Console On Windows/Linux
def cls():
    os.system("cls" if os.name == "nt" else "clear")


# Format PosLaju Tracking Number To Be Accurate
formatPL = lambda tr: len(tr) == 13 and tr[0:2] in [
    "EE",
    "EH",
    "EP",
    "ER",
    "EN",
    "EM",
    "PL",
]


def exit():
    exiting = str(input("\nDo You Want To Continue? (Y/N):"))
    exiting = exiting.upper()

    print("\n")
    if exiting == "Y":
        cls()
        main()
    else:
        return


def main():
    print("#########################")
    print("# PosLaju Tracker v0.1 #")
    print("# Coded By Noor Aiman  #")
    print("########################\n")

    tr_num = str(input("Tracking Number: "))
    tr_num = tr_num.upper()

    if formatPL(tr_num):
        url = "https://ttu-svc.pos.com.my/api/trackandtrace/v1/request"
        headers = {
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
        }
        body = {"connote_ids": [tr_num], "culture": "en"}

        try:
            response = requests.post(url, headers=headers, json=body)
            response_body = response.json()
        except requests.RequestException as error_request:
            print(
                "There is an error while sending th request.\n Eror details: ",
                error_request,
            )

        # Destructure response body (in json format) and only extract relevant information to users
        data = response_body["data"][0]
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
    else:
        print(
            "Wrong Tracking Number format. Please ensure the tracking number is correct."
        )
    exit()


if __name__ == "__main__":
    main()
