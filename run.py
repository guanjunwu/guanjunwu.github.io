from moviepy.editor import VideoFileClip

def convert_mp4_to_gif(input_file_path, output_file_path, start_time=0, end_time=None, resize=None):
    """
    Converts an MP4 video to a GIF.

    :param input_file_path: Path to the input MP4 file.
    :param output_file_path: Path for the output GIF file.
    :param start_time: Start time for the GIF (in seconds).
    :param end_time: End time for the GIF (in seconds). If None, uses the whole video.
    :param resize: Resize the GIF to this width, keeping aspect ratio. If None, keeps original size.
    :return: None
    """
    # Load the video file
    clip = VideoFileClip(input_file_path)

    # Set the start and end time if specified
    if end_time:
        clip = clip.subclip(start_time, end_time)
    else:
        clip = clip.subclip(start_time)

    # Resize the clip if resize parameter is specified
    if resize:
        clip = clip.resize(width=resize)

    # Write the clip to a GIF file
    clip.write_gif(output_file_path)

# Example usage
convert_mp4_to_gif("media/lego_mutiexp.mp4", "media/lego_mutiexp.gif", start_time=0, end_time=None, resize=200)
