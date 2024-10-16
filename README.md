# Description

FontLoader is a Python script that loads/installs fonts on Linux computers by copying all the fonts from a user specified directory into the 'user/local/share/fonts' directory. I created it to simplify the process, as installing fonts individually can be cumbersome and time-consuming.

>This is very much a "use-at-your-own-risk" program.  I put a very small amount of energy into making sure I won't personally mess something up but I can't foresee what anyone else might do.  Part of the reason why installing fonts on linux in bulk is so annoying is that you need root/administrative privileges. Logically that means this program needs those privileges as well which is not a great practice to trust some random github repo without knowing exactly what it is doing.  


## Requirements
- A computer running linux
- Python installed
- The pydantic Python library


## How to Use

### Run the python script "font_loader.py" in the terminal with the following arguments:


1. **(Required) Name of the directory where the font you want loaded exists**

    - i.e "JetBrainsMono", "fira code", etc...
    - This directory should be decompressed and exist somewhere inside the home/usr directory. 
    - The name of the directory should be unique .
        - (i.e not something like 'font' where there might be more than one directory with that name.)   

2.  **(Optional) The profile name where the font is installed with the "-u" or "--user" flag**
    
    - This is usually the name in front of the @symbol in the terminal.

    - If this is left blank the program will search for the font in all of the user's folders until a matching directory name is found.

    
3.  **(Optional) The specific file extension (without the .) of the font you want loaded with the '-f' or '--filetype' flag**   
       
    - This is optional if you only want a certain filetype like .tff or .otf
            
    - Note that I only have the program loading .ttf, .ttc, .otf, or .otc files since I know they work on linux. 

                


#### **Putting everything together you will need to run a command that at the minimum looks like this:**


        sudo python3 font_loader.py <font_folder_name>



>Note that after you run the program you will need to type and enter the 'fc-cache -f' command in the terminal in order to update your font cache library.  

        fc-cache -f

## Examples

- Installing all of the fonts inside of a directory named 'JetBrainsMono'

        sudo python3 font_loader.py JetBrainsMono


- Installing only the .ttf (truetype) fonts inside of the 'JetBrainsMono'

        sudo python3 font_loader.py JetBrainsMono -f ttf

- If you share a computer with other people and you want to download all of the fonts inside of the 'MonaspaceMono' directory located inside of your username (johnsmith)


        sudo python font_loader.py MonaspaceMono -u johnsmith



## Running with pyenv

If you use pyenv to manage your python versions then the "sudo" command will make it so your pyenv user configurations won't load.  Essentially the default Python version will run instead of the Python you set with pyenv.  To circumvent this you will need to run the program with the following command:

        sudo env "PATH=$PATH VIRTUAL_ENV=$VIRTUAL_ENV" python font_loader.py <font directory> <optional user flags>