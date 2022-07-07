import os
import re


EXCLUDE: set[str] = {'fix-ordering.py', '.git', 'README.md'}
EXT_PATTERN = r'.+(\.py|\.js)'

total_renamed: int = 0


def rec_rename(dir: str='.') -> None:
    global total_renamed
    print(f'Currently on folder: {dir}')
    
    for file in [f for f in os.scandir(dir) if f.name not in EXCLUDE]:
        if file.is_dir():   
            rec_rename(f'{file.path}/')
        elif file.is_file() and re.search(EXT_PATTERN, file.name):
            try:
                prefix, filename = re.findall(r'(\d{1,}|-.+)', file.name)
                if len(prefix) < 4:
                    new_prefix = prefix.zfill(4)
                    os.rename(f'{dir}/{file.name}', f'{dir}/{new_prefix+filename}')
                    print(f'Renamed {prefix+filename} to {new_prefix+filename}')
                    total_renamed += 1
            except ValueError:
                ...
    print('\n')


rec_rename()
print(f'Finished - Renamed {total_renamed} files.')
