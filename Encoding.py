import subprocess
import ffmpeg
# Video encoding parameters
input_file = '/Users/archer/Desktop/StreamIT/demo/example_video.mp4'
output_directory = '/Users/archer/Desktop/StreamIT/output'
bitrates = [1000, 2000, 4000]  # Bitrates in kbps
resolutions = [(640, 360), (1280, 720), (1920, 1080)]  # Resolutions (width, height) in pixels

# Encode the video with desired settingss
for i, (width, height) in enumerate(resolutions):
    output_file = f'{output_directory}/output_{width}x{height}.mp4'
    subprocess.run([
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libx264',
        '-preset', 'medium',
        '-b:v', f'{bitrates[i]}k',
        '-vf', f'scale={width}:{height}',
        '-c:a', 'aac',
        '-b:a', '128k',
        '-y',
        output_file
    ])

# Generate the streaming manifest (M3U8 for HLS)
manifest_file = f'{output_directory}/playlist.m3u8'
with open(manifest_file, 'w') as f:
    f.write('#EXTM3U\n')
    for i, (width, height) in enumerate(resolutions):
        output_file = f'output_{width}x{height}.mp4'
        f.write(f'#EXT-X-STREAM-INF:BANDWIDTH={bitrates[i]}000,RESOLUTION={width}x{height}\n')
        f.write(f'{output_file}\n')

print(f'Streaming manifest created: {manifest_file}')