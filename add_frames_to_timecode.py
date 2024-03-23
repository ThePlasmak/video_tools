import pyperclip

old_timecode = "0:00:05:21"
frames_to_add = 3 * 25 + 11
fps = 25


def add_frames_to_timecode(initial_timecode, additional_frames, fps=25):
    """
    Adds a specified number of frames to a given timecode in a video.

    Parameters:
    - initial_timecode: A string in the format "hh:mm:ss:ff"
    - additional_frames: An integer, the number of frames to add
    - fps: An integer, the frame rate of the video

    Returns:
    - A string representing the new timecode after adding the frames
    """
    # Parse the initial timecode
    hours, minutes, seconds, frames = map(int, initial_timecode.split(":"))

    # Calculate total frames
    total_frames = frames + additional_frames

    # Calculate how many seconds the total frames represent, and the remaining frames
    additional_seconds, remaining_frames = divmod(total_frames, fps)

    # Add the additional seconds to the initial seconds
    total_seconds = seconds + additional_seconds

    # Calculate how many minutes the total seconds represent, and the remaining seconds
    additional_minutes, remaining_seconds = divmod(total_seconds, 60)

    # Add the additional minutes to the initial minutes
    total_minutes = minutes + additional_minutes

    # Calculate how many hours the total minutes represent, and the remaining minutes
    additional_hours, remaining_minutes = divmod(total_minutes, 60)

    # Add the additional hours to the initial hours
    total_hours = hours + additional_hours

    # Format the new timecode
    new_timecode = f"{total_hours:02}:{remaining_minutes:02}:{remaining_seconds:02}:{remaining_frames:02}"
    return new_timecode


# Using the function to add 30 frames to the initial timecode "0:00:04:16"
new_timecode = add_frames_to_timecode(old_timecode, frames_to_add, fps)

print(new_timecode)
pyperclip.copy(new_timecode)
