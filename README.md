# AudioTube
* This application was created as a minimum viable product (MVP) for a portfolio project as part of the ALX Software Engineering Program.


## Introduction
* `I used to watch YouTube videos just to listen to the audio` like music, podcasts, and audiobooks. But with the high cost and slow speed of the internet in my country, it was a pain in the neck and a waste of money. So AudioTube is here to save the day! This app lets you stream/download YouTube videos as audio directly, without downloading the whole video. Talk about saving internet data, storage space and works like a charm even with a weak internet connection.
* `AudioTube` is a streaming application that lets you listen/download YouTube videos as audio.
* `AudioTube` was created as a single-page application with a user-friendly interface that is simple to use and provides you with many features.
* Try it now : [AudioTube](https://audiotube.aalidrisy.tech/)
* Here is a screenshots of the application:
![Home page](/app_images/try.png)
![Main page](/app_images/all.png)

## Installation
* Clone this repository:
```
git clone https://github.com/alidrisy/AudioTube.git
```
* install requermint pakage:
```
pip3 install flask youtube_dl youtube_search_python requests
```
* Access AudioTube directory: 
``` 
cd AudioTube 
```
* Run the RestFul Api: 
```
python3 -m api.v1.app
```
* Then open a second window and run the main app:
```
python3 -m at_dynamic.app
```
* Run `http://127.0.0.1:5000/` in your browser.

## Usage
* `To view playback or download options`, tap the highlighted area within the black box.
*  Then, you can `play or view download options` by tapping the buttons within the red box.
*  To switch between audio tracks, tap the names of the tracks in the yellow box.
*  To search, tap the search icon within the blue box.
  
![usage](/app_images/usage.png)

## Bugs
No known bugs at this time.


## Authors
Abdulrhman Alidrisy - [Github](https://github.com/alidrisy) / [Twitter](https://twitter.com/AbdulrahmanAdeb?t=c6JBtd7TXIrv0vyOAPryMQ&s=09)
