timecode_1 = "00:15:20:22"
timecode_2 = "00:15:19:07"
fps = 25

# Timecode 1
hours_1, minutes_1, seconds_1, frames_1 = map(int, timecode_1.split(":"))
total_seconds_1 = hours_1 * 3600 + minutes_1 * 60 + seconds_1 + frames_1 / fps

# Timecode 2
hours_2, minutes_2, seconds_2, frames_2 = map(int, timecode_2.split(":"))
total_seconds_2 = hours_2 * 3600 + minutes_2 * 60 + seconds_2 + frames_2 / fps

# Calculate the difference in seconds
time_difference = total_seconds_1 - total_seconds_2

print(time_difference)
