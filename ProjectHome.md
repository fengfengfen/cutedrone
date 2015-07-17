<a href='https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7MVF42LLU4NUS'><img src='https://www.paypal.com/en_US/i/btn/btn_donateCC_LG.gif' /></a>

# Project Summary #
  * navigation data
  * ar.drone controls
  * video stream receiving and decoding
  * udp communication between cutefaceui and cutecontroller.py

# News #
## 17.4.2011 - 2nd place @ Meegathon 24h Coding Competition @ MeeGo Summit FI // April 15-16th 2011 // Tampere, Finland ##
Thank you Forum Nokia for the N900 MeeGo development platform. And huge thanks for COSS (http://www.coss.fi) for the real prize which was a new AR.Drone. I have to admit that the AR.Drone which I used in the 24h time period did take some damage, so a new one was a really good prize indeed ;)

I was happy to be part of the competition and I am also a happy visitor of the event. The organizers in Tampere were really nice, polite and did a great job. Thank you MeeGo Summit FI organizers for the possibility of being a real geek for 24h ;p

P.S As I got a Software Development Platform from Intel [AppUp](http://www.appup.com) Developer Lab, I should be able to port this application to a [MeeGo tablet](http://www.exopc.com/en/exopc-slate.php) soon. Thank you Intel for this opportunity and your means of communicating in the Developer Lab was a really unique, a first time when I saw the "[Big Bang Theory](http://www.youtube.com/watch?v=qy_mIEnnlF4) way of using chocolate as reinforcement for positive behaviour" used in a real life ;) ..but still it was fun and entertaining way to share interesting topic from Developers to Developers.


Cheers,
Juhapekka

## Presentation from ~9min onwards ##
<a href='http://www.youtube.com/watch?feature=player_embedded&v=l3ZSvUq8kNI' target='_blank'><img src='http://img.youtube.com/vi/l3ZSvUq8kNI/0.jpg' width='425' height=344 /></a>

# Project Description #


## Presentation Videos ##
|cutefaceui|facecontroller.py|[deployment](http://meego.com/downloads/releases/1.1/meego-v1.1-sdk) to MeeGo|
|:---------|:----------------|:----------------------------------------------------------------------------|
|<a href='http://www.youtube.com/watch?feature=player_embedded&v=B0Oy5OauSnI' target='_blank'><img src='http://img.youtube.com/vi/B0Oy5OauSnI/0.jpg' width='425' height=344 /></a>|<a href='http://www.youtube.com/watch?feature=player_embedded&v=Mkk20ONSQe8' target='_blank'><img src='http://img.youtube.com/vi/Mkk20ONSQe8/0.jpg' width='425' height=344 /></a>|<a href='http://www.youtube.com/watch?feature=player_embedded&v=ZPgKb_1hMnk' target='_blank'><img src='http://img.youtube.com/vi/ZPgKb_1hMnk/0.jpg' width='425' height=344 /></a>|
| made with Qt/C++|face recognition based controlling prototype made with Python.| running on MeeGo 1.1 Netbook                                                |

## Screenshot ##
|![http://cutedrone.googlecode.com/svn/trunk/docs/Screenshot-1.png](http://cutedrone.googlecode.com/svn/trunk/docs/Screenshot-1.png)|
|:----------------------------------------------------------------------------------------------------------------------------------|
| If user moves his/her face to the left the drone moves to left                                                                    |
| if user moves his/her face to the right the drone moves to right                                                                  |
| if user moves his/her face closer to the camera the drone goes higher                                                             |
| if user moves his/her face further away from the camera the drone goes lower                                                      |

### CuteDrone ###
This is the main library for AR.Drone communication. Some parts are done by people in mardone project.

### CuteFaceUI ###
A frontend application for the CuteDrone. Demonstrates how to integrate the AR.Drone to Qt project, which can be compiled and deployed for different platforms. The main goal is to provide a simple application which would contain also face detection / object tracking. However at the moment only the functionality of the AR.Drone commanding is implemented.

## Downloads ##
  * [MeeGo 1.1 ia32 Netbook RPM Package](http://cutedrone.googlecode.com/files/cutefaceui-0.0.1-1.i586.rpm)
  * [Ubuntu 11.04 32-bit binary](http://cutedrone.googlecode.com/files/cutefaceui)

## What it is for ##
  * Regular mouse input computers, meant for MeeGo Netbook.
  * non-touchscreen Linux devices.

## What kind of technical jargon is included ##
  * C++
  * Qt
  * hack,hack,hack

## Known issues ##
  * no OpenCV integration in the C++ side
  * quick-and-dirty code, should be refactored
  * the references to [mardrone](http://mardrone.garage.maemo.org/) project should be added

## Wiki ##
I kept a track of things which I were researching from the web. Those notes are available in the [wiki-page](http://code.google.com/p/cutedrone/wiki/Meegathon).

## Why this project has been done ##
  * This project is an entry to Meegathon coding competition @ MeeGo Summit FI 2011 (http://summit.meegonetwork.fi).

## 90% of this project was done @ MeeGo Summit FI 2011, Tampere ##
So do not expect too much, but this is a fully working prototype. The OpenCV / Face stuff was implemented during the last 3 hours. The remaining 10% of work done was research and using search engine about the AR.Drone and looking thru the existing projects.

## Further development ideas ##
  * I will improve and focus on the face controlling with better time.
  * I will also refactor the code and move all 3rd party code to separate files, if required. A lot of stuff for drone control is from [MAR-Drone](http://mardrone.garage.maemo.org/) project

## Who should I blame ##
  * Juhapekka Piiroinen (gmail.com)