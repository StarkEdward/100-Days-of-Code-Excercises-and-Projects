# 2
Weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {Day: ((temp_c * 9/5)+32) for (Day, temp_c) in Weather_c.items()}

print(weather_f)