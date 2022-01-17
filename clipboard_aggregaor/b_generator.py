"""
Script which compress folder (or list of folders) at given location.

The name of zipped folder would be: <date>_<hour>_<folder_name>.zip
date: DD-MM-YYYY format
hour: HH-MM format
folder_name: name of folder(s) at given location,
             for many folders pattern would be '<f1>&<f2>&<f3>'
"""
from datetime import datetime
import pathlib
import zipfile


class InvalidLocationError(Exception):
    pass

class IsNotDirectoryError(Exception):
    pass


def compress(*locations) -> None:
    # wyciagnij wszystkie sciezki # TODO: create validation decorator
    paths = [pathlib.Path(location) for location in locations]
    # zamien na pathlib.Path zweryfikuj istnienie
    for path in paths:
        # wyjatki
        if not path.exists:
            raise InvalidLocationError('Given folder location: {} does not exist')
        elif path.is_file:
            raise IsNotDirectoryError(f'Given path: {path} is not a directory')

    # stworz nazwe output zip file
    cwd = pathlib.Path().resolve()
    timestamp = datetime.now().strftime("%d-%m-%Y_%H:%M")
    zip_folder_name = '&'.join(path.name for path in paths)
    full_path = cwd / f'{timestamp}_{zip_folder_name}.zip'

    # otworz ctx magerem zip obj
    with zipfile.open(full_path, 'w') as f:
        # przejdz po wszystkich podfolderach kazdego fold i zrob obj.write
        ...
        # obsluga wyjatkow
