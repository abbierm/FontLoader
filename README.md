# Description

font_loader.py is a Python script that loads/installs fonts on UNIX computers by copying each individual font inside of a specified folder into the 'user/local/share/fonts' directory. I made this because installing each individual fonts one by one is annoying and cumbersome.  

>This is very much a 'use-at-your-own-risk' program that I made for myself in a short amount of time.  I put a very small amount of energy into making sure I won't personally mess something up on my computer by running this BUT that doesn't mean I can forsee how someone else might use this.  Part of the reason why installing fonts on linux in bulk is so annoying is that in order to add anything to the correct directory you need to have root (administrative) privileges. Logically that means this program needs root privileges in order to run and you could possibly mess something up. 


## Requirements
- A computer running linux
- Python (Preferably not the installation that comes preinstalled)
- The pydantic library
- Root privileges

## How to Use

Run the python script "font_loader.py" in the terminal with the following arguments:


- **(Required) Name of the directory where the font you want loaded exists**

    - i.e "JetBrainsMono", "fira code", etc...
    - This directory should be decompressed and exist somewhere inside the home/usr directory. 
    - The name of the directory should be unique .
        - (i.e not something like 'font' where there might be more than one directory with that name.)   

- **(Optional) The profile name where the font is installed with the -u or --user flag**
    
    - This is usually the name in front of the @symbol in the terminal.

    - If this is left blank the program will search for the font in all of the user's folders until a matching directory name is found.

    
- **(Optional) The specific file extension (without the .) of the font you want loaded with the '-f' or '--filetype' flag**   
       
    - This is optional if you only want a certain filetype like .tff or .otf
            
    - Note that I only have the program loading .ttf, .ttc, .otf, or .otc files since I know they work on linux. 

                


- Putting everything together you will need to run a command that at the minimum looks like this:


        sudo python3 font_loader.py <font_folder_name>


- After your installation run the 'fc-cache -f' command in order to update your font cache library.  

        fc-cache -f

## Examples

- Installing all of the fonts inside of a directory named 'JetBrainsMono'

        sudo python font_loader.py JetBrainsMono


- Installing only the .ttf (truetype) fonts inside of the 'JetBrainsMono'

        sudo python font_loader.py JetBrainsMono -f ttf

- If you share a computer with other people and you want to download all of the fonts inside of the 'MonaspaceMono' directory located inside of your username (johnsmith)


        sudo python font_loader.py MonaspaceMono -u johnsmith




