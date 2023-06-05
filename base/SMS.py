import requests

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjQwODYsInJvbGUiOm51bGwsImRhdGEiOnsiaWQiOjQwODYsIm5hbWUiOiJHYXppeGFub3YgVGFsJ2F0IFNpZGlreG9ub3ZpY2giLCJlbWFpbCI6Imphdm9oaXJzaWRpa3hvbm92QGdtYWlsLmNvbSIsInJvbGUiOm51bGwsImFwaV90b2tlbiI6bnVsbCwic3RhdHVzIjoiYWN0aXZlIiwic21zX2FwaV9sb2dpbiI6ImVza2l6MiIsInNtc19hcGlfcGFzc3dvcmQiOiJlJCRrIXoiLCJ1el9wcmljZSI6NTAsInVjZWxsX3ByaWNlIjoxMTUsInRlc3RfdWNlbGxfcHJpY2UiOm51bGwsImJhbGFuY2UiOjQ4ODUsImlzX3ZpcCI6MCwiaG9zdCI6InNlcnZlcjEiLCJjcmVhdGVkX2F0IjoiMjAyMy0wNS0yNlQxMTozOTowMC4wMDAwMDBaIiwidXBkYXRlZF9hdCI6IjIwMjMtMDUtMjZUMTE6NDg6MDMuMDAwMDAwWiIsIndoaXRlbGlzdCI6bnVsbCwiaGFzX3BlcmZlY3R1bSI6MH0sImlhdCI6MTY4NTM2NjUxMywiZXhwIjoxNjg3OTU4NTEzfQ.1fRpo-6xehnjgOKRXW21PX1OBAb5DUQN7J6m8T4ttoA"


def send_sms(phone, otp):
    data = {
        "mobile_phone": phone,
        "message": f"Sekret kod: {otp}",
        "from": 4546,
        "callback_url": "http://0000.uz/test.php"
    }

    headers = {"Authorization": f"Bearer {token}"}

    url = "https://notify.eskiz.uz/api/message/sms/send"

    return requests.post(url, data=data, headers=headers).json()
