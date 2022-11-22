import subprocess

# Extract 10 seconds from original video and resize it to four different resolutions
'''
# Extract 10 seconds from BBB.mp4 to reduce computation time
subprocess.run('ffmpeg -ss 00:00:50 -to 00:01:00 -i BBB.mp4 -c copy BBB_short.mp4', shell=True)

# Video resized to 720p (1280x720)
subprocess.run('ffmpeg -i BBB_short.mp4 -vf scale=1280:720 Videos_ex1/720p/BBB_720.mp4', shell=True)

# Video resized to 480p (640x480)
subprocess.run('ffmpeg -i BBB_short.mp4 -vf scale=640:480 Videos_ex1/480p/BBB_480.mp4', shell=True)

# Video resized to 360x240
subprocess.run('ffmpeg -i BBB_short.mp4 -vf scale=360:240 Videos_ex1/360x240/BBB_360x240.mp4', shell=True)

# Video resized to 160x120
subprocess.run('ffmpeg -i BBB_short.mp4 -vf scale=160:120 Videos_ex1/160x120/BBB_160x120.mp4', shell=True)
'''

'''# Encode 720p video

# Encode to VP8
input_video = 'Videos_ex1/720p/BBB_720.mp4'
output_video = 'Videos_ex1/720p/BBB_720_vp8.webm'
subprocess.run('ffmpeg -i '+input_video+' -c:v libvpx -b:v 1M -c:a libvorbis '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)

# Encode to VP9
input_video = 'Videos_ex1/720p/BBB_720.mp4'
output_video = 'Videos_ex1/720p/BBB_720_vp9.mp4'
subprocess.run('ffmpeg -i '+input_video+' -c:v libvpx-vp9 '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)

# Encode to AV1
input_video = 'Videos_ex1/720p/BBB_720.mp4'
output_video = 'Videos_ex1/720p/BBB_720_av1.mp4'
subprocess.run('ffmpeg -i '+input_video+' -c:v libaom-av1 '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)

# Encode to H265
input_video = 'Videos_ex1/720p/BBB_720.mp4'
output_video = 'Videos_ex1/720p/BBB_720_h265.mp4'
subprocess.run('ffmpeg -i '+input_video+' -c:v libx265 '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)


# Encode 480p video

# Encode to VP8
input_video = 'Videos_ex1/480p/BBB_480.mp4'
output_video = 'Videos_ex1/480p/BBB_480_vp8.webm'
subprocess.run('ffmpeg -i '+input_video+' -c:v libvpx -b:v 1M -c:a libvorbis '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)

# Encode to VP9
input_video = 'Videos_ex1/480p/BBB_480.mp4'
output_video = 'Videos_ex1/480p/BBB_480_vp9.mp4'
subprocess.run('ffmpeg -i '+input_video+' -c:v libvpx-vp9 '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)

# Encode to AV1
input_video = 'Videos_ex1/480p/BBB_480.mp4'
output_video = 'Videos_ex1/480p/BBB_480_av1.mp4'
subprocess.run('ffmpeg -i '+input_video+' -c:v libaom-av1 '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)

# Encode to H265
input_video = 'Videos_ex1/480p/BBB_480.mp4'
output_video = 'Videos_ex1/480p/BBB_480_h265.mp4'
subprocess.run('ffmpeg -i '+input_video+' -c:v libx265 '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)


# Encode 360x240 video

# Encode to VP8
input_video = 'Videos_ex1/360x240/BBB_360x240.mp4'
output_video = 'Videos_ex1/360x240/BBB_360x240_vp8.webm'
subprocess.run('ffmpeg -i '+input_video+' -c:v libvpx -b:v 1M -c:a libvorbis '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)

# Encode to VP9
input_video = 'Videos_ex1/360x240/BBB_360x240.mp4'
output_video = 'Videos_ex1/360x240/BBB_360x240_vp9.mp4'
subprocess.run('ffmpeg -i '+input_video+' -c:v libvpx-vp9 '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)

# Encode to AV1
input_video = 'Videos_ex1/360x240/BBB_360x240.mp4'
output_video = 'Videos_ex1/360x240/BBB_360x240_av1.mp4'
subprocess.run('ffmpeg -i '+input_video+' -c:v libaom-av1 '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)

# Encode to H265
input_video = 'Videos_ex1/360x240/BBB_360x240.mp4'
output_video = 'Videos_ex1/360x240/BBB_360x240_h265.mp4'
subprocess.run('ffmpeg -i '+input_video+' -c:v libx265 '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)


# Encode 160x120 video

# Encode to VP8
input_video = 'Videos_ex1/160x120/BBB_160x120.mp4'
output_video = 'Videos_ex1/160x120/BBB_160x120_vp8.webm'
subprocess.run('ffmpeg -i '+input_video+' -c:v libvpx -b:v 1M -c:a libvorbis '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)

# Encode to VP9
input_video = 'Videos_ex1/160x120/BBB_160x120.mp4'
output_video = 'Videos_ex1/160x120/BBB_160x120_vp9.mp4'
subprocess.run('ffmpeg -i '+input_video+' -c:v libvpx-vp9 '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)

# Encode to AV1
input_video = 'Videos_ex1/160x120/BBB_160x120.mp4'
output_video = 'Videos_ex1/160x120/BBB_160x120_av1.mp4'
subprocess.run('ffmpeg -i '+input_video+' -c:v libaom-av1 '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)

# Encode to H265
input_video = 'Videos_ex1/160x120/BBB_160x120.mp4'
output_video = 'Videos_ex1/160x120/BBB_160x120_h265.mp4'
subprocess.run('ffmpeg -i '+input_video+' -c:v libx265 '+output_video, shell=True)
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams '+output_video, shell=True)
'''

# Collage of 720p video with 4 different codecs (VP8, VP9, AV1, H265)
subprocess.run('ffmpeg -i Videos_ex1/720p/BBB_720_vp8.webm -i Videos_ex1/720p/BBB_720_vp9.mp4 '
               '-i Videos_ex1/720p/BBB_720_av1.mp4 -i Videos_ex1/720p/BBB_720_h265.mp4'
               ' -filter_complex "nullsrc=size=640x480 [base]; '
               '[0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; '
               '[1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; '
               '[2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; '
               '[3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; '
               '[base][upperleft] overlay=shortest=1 [tmp1]; '
               '[tmp1][upperright] overlay=shortest=1:x=320 '
               '[tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 '
               '[tmp3]; [tmp3][lowerright] overlay=shortest=1:x=320:y=240" '
               '-c:v libx264 Videos_ex1/720p/BBB_720_collage.mp4', shell=True)

# Collage of 480p video with 4 different codecs (VP8, VP9, AV1, H265)
subprocess.run('ffmpeg -i Videos_ex1/480p/BBB_480_vp8.webm -i Videos_ex1/480p/BBB_480_vp9.mp4 '
               '-i Videos_ex1/480p/BBB_480_av1.mp4 -i Videos_ex1/480p/BBB_480_h265.mp4'
               ' -filter_complex "nullsrc=size=640x480 [base]; '
               '[0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; '
               '[1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; '
               '[2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; '
               '[3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; '
               '[base][upperleft] overlay=shortest=1 [tmp1]; '
               '[tmp1][upperright] overlay=shortest=1:x=320 '
               '[tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 '
               '[tmp3]; [tmp3][lowerright] overlay=shortest=1:x=320:y=240" '
               '-c:v libx264 Videos_ex1/480p/BBB_480_collage.mp4', shell=True)

# Collage of 360x240 video with 4 different codecs (VP8, VP9, AV1, H265)
subprocess.run('ffmpeg -i Videos_ex1/360x240/BBB_360x240_vp8.webm -i Videos_ex1/360x240/BBB_360x240_vp9.mp4 '
               '-i Videos_ex1/360x240/BBB_360x240_av1.mp4 -i Videos_ex1/360x240/BBB_360x240_h265.mp4'
               ' -filter_complex "nullsrc=size=640x480 [base]; '
               '[0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; '
               '[1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; '
               '[2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; '
               '[3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; '
               '[base][upperleft] overlay=shortest=1 [tmp1]; '
               '[tmp1][upperright] overlay=shortest=1:x=320 '
               '[tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 '
               '[tmp3]; [tmp3][lowerright] overlay=shortest=1:x=320:y=240" '
               '-c:v libx264 Videos_ex1/360x240/BBB_360x240_collage.mp4', shell=True)

# Collage of 160x120 video with 4 different codecs (VP8, VP9, AV1, H265)
subprocess.run('ffmpeg -i Videos_ex1/160x120/BBB_160x120_vp8.webm -i Videos_ex1/160x120/BBB_160x120_vp9.mp4 '
               '-i Videos_ex1/160x120/BBB_160x120_av1.mp4 -i Videos_ex1/160x120/BBB_160x120_h265.mp4'
               ' -filter_complex "nullsrc=size=640x480 [base]; '
               '[0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; '
               '[1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; '
               '[2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; '
               '[3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; '
               '[base][upperleft] overlay=shortest=1 [tmp1]; '
               '[tmp1][upperright] overlay=shortest=1:x=320 '
               '[tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 '
               '[tmp3]; [tmp3][lowerright] overlay=shortest=1:x=320:y=240" '
               '-c:v libx264 Videos_ex1/160x120/BBB_160x120_collage.mp4', shell=True)
