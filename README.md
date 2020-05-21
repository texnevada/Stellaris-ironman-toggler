# Stellaris-ironman-toggler

This software is only tested on Windows 10 and may or may not work for other operating systems.

###Disclaimer:
This program was tested with a new empire that started with ironman and even after
console edits and ironman reapplied. Achievements was still possible.
I am however not responsible for any damages to your save game.
While this program does back up the game for you.
You should still back up the game before you attempt to use the program just in case.
Use at your own risk. You have been warned.

How does this work?
=
First you put the file in your folder where your save is located.
The program will look for the `ironman.sav` file to enable or disable ironman.sav.
The program will then goes through the entire save and looks for the ironman 
references and turns them off or on.

What is the purpose of this tool?
=
Have you ever had a game suddenly bug on you and you wish you could access the ingame
console to fix it? Well with this you can!

Does this mean I can turn my save into ironman and get achievements?
=
It is possible, though it is not the intended purpose of this tool.
If your savegame was modded to any extent and you enable ironman.
The game will not award you achievements due to the checksum verification being wrong.

# How to use the program

1. **Autosave is recommended to be turned off in the gameplay settings for this to work!
You can re-enable this later**
![](Autosave%20to%20Cloud%20Off.jpg)

2. **When saving the game. You also have to make sure not to save to the cloud!
Otherwise the game will not save a proper local version on your PC. (This is the case with
the steam version. I have no knowledge of the other versions)**
![](Do%20not%20save%20to%20the%20cloud.jpg)

3. Once you have done the following above. Go to your save in-game and save your game.
This should create a local save file in save games folder with your empire name.
``~\Documents\Paradox Interactive\Stellaris\save games\YourEmpire\``

4. Make sure your save is called ``ironman.sav`` otherwise the program won't enable/disable
ironman for you. 
**If you are turning a normal game save into ironman mode. You need to name your
save** ``ironman.sav``.

5. Run the program inside the save folder of your empire. It will let you know when it is done.

6. If you just disabled the ironman mode. You should then now be able to boot up your game
and do what you need to do in the console. Once you finish. Save the game and close out of it.
Then proceed to use the program again. **Important:** Once it has re-enabled ironman mode. 
You need to boot up your save and close it for it to take effect properly even though it
looks like ironman is enabled!