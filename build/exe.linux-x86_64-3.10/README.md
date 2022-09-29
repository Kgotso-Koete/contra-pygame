# About the project

### Description of the project

This is a clone of the video game [Contra](<https://en.wikipedia.org/wiki/Contra_(series)>) built while following [Christian Koch](https://www.udemy.com/user/christian-koch-59/) [tutorial](https://www.udemy.com/course/learn-python-by-making-games/). [Contra](<https://en.wikipedia.org/wiki/Contra_(series)>)is a video game series produced by Konami composed primarily of run and gun-style shooting games.

---

### Click here for the [video demo](https://youtu.be/fmPfiV2M-3s)

1. Play it on Windows by downloading the [Windows build folder](./build/exe.win-amd64-3.10/) and clicking on the .exe file
2. Play it on Linux by downloading the [Linux build folder](./build/exe.linux-x86_64-3.10/) and clicking on the executable file

---

# Screen shot of the application

|             Start Screen             |             Game Screen             |
| :----------------------------------: | :---------------------------------: |
| ![](/screenshots/1_start_screen.png) | ![](/screenshots/2_game_screen.png) |

---

### Technology stack

1. Python 3.10.6
2. Pygame 2.1.2
3. Pytmx 3.31

---

### Install the project on Linux or Windows:

1. Download this codebase
2. Install Python 3.10.6 on your machine
3. Install Pygame 2.1.2 (Linux `python3 pip install pygame`) (Windows `python3 -m pip install pygame`)
4. Install Pytmx 3.31 (Linux `pip3 install pytmx`) (Windows `pip3 -m install pytmx`)

### 3: Run project

1. Run locally: Navigate to the project folder and run `python3 main.py` (or `python -m main` on Windows if Windows is not working properly) to start the game.

### Build project executable

Follow the instructions below to build an executable file for Ubuntu Linux and Windows

1. Install executable builder `pip install cx_freeze`
2. Build the Windows executable by running the following command `python3 setup.py build` (or `python -m setup build` on Windows if Windows is not working properly)

The [Linux executable file](./build/exe.linux-x86_64-3.10/contra) will in the following folder `./build/exe.linux-x86_64-3.10`

The [Windows executable file](./build/exe.win-amd64-3.10/contra.exe) will in the following folder `./build/exe.win-amd64-3.10`. The executable must contain all supporting files in this folder to run.

---

### Acknowledgements

Special thanks to [Christian Koch](https://www.udemy.com/user/christian-koch-59/) for a great [tutorial](https://www.udemy.com/course/learn-python-by-making-games/). I already did Christian's awesome Flappy Bird tutorial to learn the basics of Pygame, so I only did the Contra section of this tutorial. The tutorial was small enough to be completed without investing too much time, but also broad enough to give learners a taste of what it takes to build a complex 2D game. I also liked the gradual build up from Pygame and unstructured code, to using classes to manage complexity. Very well explained, worth every minute and penny.

Start menu was created with the help of [BaralTech's](https://www.youtube.com/c/BaralTech)[tutorial](https://youtu.be/GMBqjxcKogA). Here is the [link to their repo](https://github.com/baraltech/Menu-System-PyGame).

Music called `leap.wav` for the start menu was obtained from [Open Game Art](https://opengameart.org/content/leap-8bit). Special thank you to the Artist [Nene](https://opengameart.org/users/nene) for the [Creative Commons License](https://creativecommons.org/publicdomain/zero/1.0/) to use this music.

<br/>
<br/>

---

### License

The codebase is MIT licensed unless otherwise specified. Feel free to fork or download this code and use as specified in the license.

#

To be modified further by Kgotso Koete
<br/>
September 2022
