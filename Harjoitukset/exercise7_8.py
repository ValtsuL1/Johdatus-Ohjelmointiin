import json
import urllib.request
url = "https://api.ouka.fi/v1/chc_waiting_times_monthly_stats?order=year.desc,month.desc"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
data = json.loads(raw_data)

queue_total_doctor = []
queue_total_nurse = []

# kysyy miltä vuosiluvulta käyttäjää hakee
target_year = int(input("Anna vuosiluku: (2017-2020)\n"))

for entry in data:
    doctor_queue = entry["doctor_queue"]
    nurse_queue = entry["nurse_queue"]
    year = entry["year"]
    # jos year on null, aloittaa alusta
    if target_year == year:
        # jos doctor_queue on null, skippaa
        if doctor_queue:
            queue_total_doctor.append(doctor_queue)
        # jos nurse_queue on null, skippaa
        if nurse_queue:
            queue_total_nurse.append(nurse_queue)

# laskee keskiarvon molemmasta queue_total listasta
# lopuksi laskee molemmista keskiarvon
queue_avg_doctor = sum(queue_total_doctor) / len(queue_total_doctor)
queue_avg_doctor = round(queue_avg_doctor, 2)

queue_avg_nurse = sum(queue_total_nurse) / len(queue_total_nurse)
queue_avg_nurse = round(queue_avg_nurse, 2)

queue_avg = queue_avg_doctor + queue_avg_nurse / 2
queue_avg = round(queue_avg, 2)

print(f"Keskimääräinen jonotusaika: {queue_avg} min.")
