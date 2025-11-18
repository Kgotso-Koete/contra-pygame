# About the project

### Description of the project

This is a clone of the video game [Contra](<https://en.wikipedia.org/wiki/Contra_(series)>) built while following [Christian Koch](https://www.udemy.com/user/christian-koch-59/) [tutorial](https://www.udemy.com/course/learn-python-by-making-games/). [Contra](<https://en.wikipedia.org/wiki/Contra_(series)>)is a video game series produced by Konami composed primarily of run and gun-style shooting games.

---

### Play the game

**[Click here to download the latest release for Windows and Linux from the GitHub Releases page.](https://github.com/kgotso-koete/contra-pygame/releases)**

### Video Demo

[Click here to watch the video demo.](https://youtu.be/fmPfiV2M-3s)

---

# Screen shot of the application

|             Start Screen             |             Game Screen             |
| :----------------------------------: | :---------------------------------: |
| ![](/screenshots/1_start_screen.png) | ![](/screenshots/2_game_screen.png) |

---

### Technology stack

1. Python 3.12.3
2. Pygame 2.6.1
3. Pytmx 3.32
4. cx_Freeze 8.4.1

---

### Install the project on Ubuntu Linux:

1. **Download codebase:** Clone or download the source code to your local machine.

2. **Install System Dependencies:** Pygame requires the SDL2 library. Install it using the following command:

   ```bash
   sudo apt-get update && sudo apt-get install -y libsdl2-dev
   ```

3. **Create a Virtual Environment:** It's recommended to use a virtual environment to manage project dependencies. Navigate to the project's root directory and run:

   ```bash
   python -m venv .venv
   ```

4. **Activate the Virtual Environment:**

   ```bash
   source .venv/bin/activate
   ```

5. **Install Python Packages:** Install all the required packages from the `requirements.txt` file:
   ```bash
   pip install -r requirements-windows.txt
   ```

   or

   ```bash
   pip install -r requirements-linux.txt
   ```

### 3: Run project

1. Run locally: Navigate to the project folder and run `python main.py` (or `python -m main` on Windows if Windows is not working properly) to start the game.

### Build a Single Executable for Distribution

To create a single executable file for distribution on platforms like itch.io, we will use `PyInstaller`.

1. **Install PyInstaller:**
   Ensure your virtual environment is active and run:
   ```bash
   pip install pyinstaller
   ```

2. **Build the Executable:**
   Run the appropriate command for your operating system from the project root.

   **For Linux:**
   ```bash
   pyinstaller --onefile --windowed --name contra-pygame --add-data 'assets:assets' --add-data 'app:app' main.py
   ```

   **For Windows:**
   ```cmd
   pyinstaller --onefile --windowed --name contra-pygame `
   --add-data "assets;assets" `
   --add-data "app;app" `
   main.py
   ```

   After the process completes, you will find the single executable file inside the `dist` folder. This is the file you can upload for distribution.

3. **Testing the Linux Executable:**
   Before distributing, you can test the executable on Linux.

   First, make the file executable:
   ```bash
   chmod +x dist/contra-pygame
   ```

   Then, run it from the terminal:
   ```bash
   ./dist/contra-pygame
   ```

---

### Acknowledgements

Special thanks to [Christian Koch](https://www.udemy.com/user/christian-koch-59/) for a great [tutorial](https://www.udemy.com/course/learn-python-by-making-games/). I already did Christian's Flappy Bird tutorial on YouTube to learn the basics of Pygame, so I only did the Contra section of this tutorial. The tutorial was small enough to be completed without investing too much time and broad enough to give learners a taste of what it takes to build a complex 2D game. I also liked the gradual build-up from Pygame and unstructured code to using classes to manage complexity. Very well explained, and worth every minute and penny. 5 out of 5 stars for me.

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
