# AudioTube
* This application was created as a minimum viable product (MVP) for a portfolio project as part of the ALX Software Engineering Program.


## About
* `AudioTube` is a streaming application that lets you listen/download to YouTube videos as audio.
* `AudioTube` was created as a single-page application with a user-friendly interface that is simple to use and provides you with many features.
* Here are some screenshots of the application:
![Main page](/app_images/main.jpg)
![Main catagories](/app_images/tag.jpg)
![Options](/app_images/option.jpg)
![Searching](/app_images/search.jpg)
![Player](/app_images/play.jpg)


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

## Bugs
No known bugs at this time.


## Authors
Abdulrhman Alidrisy - [Github](https://github.com/alidrisy) / [Twitter](https://twitter.com/AbdulrahmanAdeb?t=c6JBtd7TXIrv0vyOAPryMQ&s=09)
