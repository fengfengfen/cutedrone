

http://summit.meegonetwork.fi/competition
**WORK IN PROGRESS**

# Screenshots #
see project frontpage.

# Deploy from QtCreator to MeeGo 1.1 Netbook #
<a href='http://www.youtube.com/watch?feature=player_embedded&v=ZPgKb_1hMnk' target='_blank'><img src='http://img.youtube.com/vi/ZPgKb_1hMnk/0.jpg' width='425' height=344 /></a>


---

# Scripts available #
I am producing scripts for the installation etc at the sametime for later usage. Feel free to use them. They are available in svn.


# Installing MeeGo SDK #
Following are my notes from the official MeeGo wiki page. See the Links at the end of this wiki page.
## Add repository ##
```
deb http://repo.meego.com/MeeGo/sdk/host/repos/ubuntu/10.10/   /
gpg --keyserver pgpkeys.mit.edu --recv 0BC7BEC479FC1F8A
gpg --export --armor 0BC7BEC479FC1F8A | sudo apt-key add -
sudo apt-get update
```
## Confirm repository ##
```
apt-cache policy madde
```
## Install SDK ##
```
sudo apt-get install meego-sdk
```
## Install MeeGo Target for notebook ##
```
sudo mad-admin create -f meego-netbook-ia32-1.1
```

# Setting up the target hardware notebook #
## Asus EeePC 901 ##
```
sudo zypper install openssh-server
sudo service sshd start
sudo chkconfig --add sshd
sudo zypper install gdb-gdbserver
xhost +SI:localuser:root
```
### Fix issues with wlan ###
```
sudo ifconfig wlan0 up
sudo pkill connmand
sudo /usr/sbin/connmand -W nl80211,wext
```
### Connecting to AR.Drone ###
```
sudo iwconfig wlan0 mode ad-hoc essid ardrone_[id]
```
#### Does not work for EeePC 901 ####
It seems that there are sever issues with the wlan adapter..

# CuteFace #
http://code.google.com/p/cutedrone/source/browse/#svn%2Ftrunk
```
cd
mkdir meegathon
```
## Development Notes ##
### 3rd Party libraries ###
```
mkdir -p ~/meegathon/3rdparty
```
#### OpenCV ####
http://opencv.willowgarage.com/wiki/InstallGuide
```
mkdir -p ~/meegathon/3rdparty
cd ~/meegathon/3rdparty
wget -c http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.2/OpenCV-2.2.0.tar.bz2/download
tar -xvjpf OpenCV-2.2.0.tar.bz2
ln -s OpenCV-2.2.0 opencv
cd opencv
```
```
sudo apt-get install libqt4-dev libtbb-dev libtbb2 cmake libv4l-dev
sudo apt-get install libjpeg-dev libtiff-dev libpng-dev libjasper-dev
sudo apt-get install ffmpeg gstreamer0.10-ffmpeg libxine-dev libunicap2-dev libdc1394-22-dev libavformat-dev libswscale-dev
sudo apt-get install linux-source gstreamer-base-0.10 python-numpy
```
```
cd ~/meegathon/3rdparty
mkdir opencv-build
cd opencv-build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_QT=ON -D WITH_TBB=YES -D WITH_V4L=1 -D TBB_INCLUDE_DIRS=/usr/include/tbb -D BUILD_SAMPLES=ON -D PYTHON_INCLUDE_DIRS=/usr/include/python2.7 ../opencv
make -j`cat /proc/cpuinfo|grep processor|wc -l`
```

##### edit cvconfig.h #####
You might need to modify the cvconfig.h in build directory. If the build fails then add following line there:
```
#define HAVE_CAMV4L
```

# Links / Sources #
  * http://wiki.forum.nokia.com/index.php/Using_OpenCV_with_Qt
  * http://note.sonots.com/SciSoftware/haartraining.html
  * http://opencv.willowgarage.com/wiki/FaceDetection
  * http://wiki.meego.com/SDK/Docs/1.1/Getting_started_with_the_MeeGo_SDK_for_Linux
  * http://wiki.meego.com/SDK/Docs/1.1/Configuring_QEMU_runtimes
  * http://blogs.forum.nokia.com/blog/kate-alholas-forum-nokia-blog/2010/12/23/ar-drone-with-meego
  * https://garage.maemo.org/projects/mardrone
  * http://mardrone.garage.maemo.org/
  * http://wiki.meego.com/SDK/Docs/1.1/Setting_up_Netbook
  * http://forum.meego.com/showthread.php?t=1756