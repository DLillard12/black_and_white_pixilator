Daniel Lillard

2025.05.19

I got inspired by this youtube video: https://www.youtube.com/watch?v=nvR8__cVifI to create a black and white pixilator.
For the first half I will only do this on pictures, but may then transfer to images.
Currently I think the following will have to happen: 
1. Determine a default image size and resolution
2. Group pixels
3. Determine and set those pixels to either black or white.

So it appears that the video had some random factor that was adding in pixels that were characterized 'incorrectly'
I will be adding this stochastic element.

I was having issues with pixelation, because I was using the wrong variable name! Took me forever to find.

I am also using this to play around with branches for the first time.

I have noticed that the pixelation is grey, this is because I am setting the pixels at a floor/ceiling BEFORE pixelization.

I tried 127 for the binary threshold but that is a bit too high, setting it lower.

Also I have noticed that while the video has binary white and black the pixels have a gradient, so there are grouping of pixels which are all black, all white, and inbetween there are groupings with a black or white X.
E.G.

BBB

BBB

BBB

BWB

WBW

BWB


I did a project for my COSC523 course where I got to do the above, I implemented it here.

Another idea: Make is so that we look at the extremes rather the middle. Make all those colored.

I have used some ffmpeg for this project, it turns videos into frames and frames into videos.
```
video to frames: ffmpeg -i input.mp4 input/*_frames/frame_%06d.png

frames to video: ffmpeg -framerate 30 -i output/*_frames/frames/frame_%06d.png -c:v libx264 -pix_fmt yuv420p -vf "pad=ceil(iw/2)\*2:ceil(ih/2)*2" output*.mp4
```