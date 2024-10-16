# font_loader.py

from argparse import Namespace, ArgumentParser
from pathlib import Path
from pydantic import BaseModel
import shutil
import sys
from typing import Optional


HOME = Path("/home")

VALID_FONTS = {
    "ttf": (".ttf", "truetype"), 
    "ttc": (".ttc", "opentype"), 
    "otf": (".otf", "opentype"), 
    "otc": (".otc","opentype")
}


class FontPreferences(BaseModel):
    directory_name: str
    directory_path: Path
    file_type: list[tuple[str, str]]
    destination: Path = Path("/usr/local/share/fonts")
    

def parse_args() -> Namespace:
    parser = ArgumentParser()
    help_font_folder = "Name of the folder the fonts are in"
    parser.add_argument("font_folder", help=help_font_folder)
    parser.add_argument("-u", "--user")
    parser.add_argument("-f", "--filetype")
    args = parser.parse_args()
    return args



def _search_directory(dir: str, current: Path) -> Path | None:
    current_directories = list(current.iterdir())
    try:
        file_match = next(filter(lambda x: dir == x.name, current_directories))
        return file_match
    except StopIteration:
        directories = [y for y in current_directories if y.is_dir() == True]
        for d in directories:
            result = _search_directory(dir, d)
            if result != None:
                return result
    return None
    

def find_font_directory(font_directory: str, usr: Optional[str] = None) -> Path | None:
    users = None
    if usr is None:
        users = list(HOME.iterdir())
    else:
        user = Path(HOME, usr)
        if not user.exists():
            print("invalid user")
            sys.exit()
        users = [user]

    if len(usr) == 0:
        print("unable to find user directory")
        sys.exit()

    for u in users:
        font_path = _search_directory(font_directory, u)
        if font_path:
            break

    if not font_path:
        print(f"Unable to find directory: {font_directory}")
        sys.exit()

    return font_path

    

def get_font_folders(font_file_type: str) -> list[tuple[str]]:
    """
    If font file type is valid the return value will be a list tuples with the
    extension at index 0 and the file the font will go in at index 1. 
    i.e: 
        [(".ttf", "truetpye"), ["otf", "opentype"]]
        [(".otc", "opentype")]
    """
    if not font_file_type:
        return [
            (".ttf", "truetype"), 
            (".ttc", "opentype"), 
            (".otf", "opentype"), 
            (".otc","opentype")
        ]
    try:
        fonts = [tuple(VALID_FONTS[font_file_type])]
    except KeyError:
        print(f"Unusable font file type: {font_file_type}")
        sys.exit()
    return fonts


def move_fonts(prefs: FontPreferences) -> None:
    new_path = prefs.destination / prefs.directory_name
    if not new_path.exists():
            new_path.mkdir()

    for font_type in prefs.file_type:
        fonts = list(prefs.directory_path.glob(f"**/*{font_type[0]}"))
        if len(fonts) == 0:
            continue
        print(f"Adding {prefs.directory_name} {font_type[0]} to {new_path}")

        for font in fonts:
            complete_end_path = new_path / font.name
            shutil.copy(font, complete_end_path)

def main():
    args = parse_args()
    font_file_type = get_font_folders(args.filetype)
    print(font_file_type)
    font_path = find_font_directory(args.font_folder, args.user)
    prefs = FontPreferences(
        directory_name=args.font_folder,
        directory_path=font_path,
        file_type=font_file_type
    )
    move_fonts(prefs)



if __name__ == "__main__":
    main()