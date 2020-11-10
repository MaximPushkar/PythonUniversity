import os
import json
from colorama import Style, Fore
from hashlib import md5


def generate_cache_name(dirPath: str):
    encoded = dirPath.encode()
    hashsum = md5(encoded).hexdigest()
    return os.path.join('cache', hashsum)


def write_cache(cache_name: str, dirDict: dict):
    with open(cache_name, "w+") as f:
        json.dump(dirDict, f)


def read_cache(cache_name: str):
    cache = {}
    if os.path.isfile(cache_name):
        with open(cache_name, "r") as f:
            cache = json.load(f)
    return cache


def compare_versions(dirOld: dict, dirNew: dict):
    old_copy, new_copy = dirOld.copy(), dirNew.copy()
    updated_list = []
    print("Deleted files and directories:")
    counter = 1
    for key in old_copy:
        if key not in new_copy.keys():
            print(f'{Fore.RED}{counter}) {key}{Style.RESET_ALL}')
            counter += 1
        elif old_copy[key] != new_copy[key]:
            updated_list.append(key)
            del new_copy[key]
        else:
            del new_copy[key]

    print()
    counter = 1
    print("Updated files:")
    for key in updated_list:
        print(f'{Fore.BLUE}{counter}) {key}{Style.RESET_ALL}')
        counter += 1

    print()
    counter = 1
    print("New files:")
    for key in new_copy.keys():
        print(f'{Fore.GREEN}{counter}) {key}{Style.RESET_ALL}')
        counter += 1
    print()


def scan_dir(dirPath: str):
    if not os.path.isdir(dirPath):
        print(f"{dirPath} is not a directory")
        exit()

    res = {}

    for root, dirs, files in os.walk(dirPath):
        for name in files:
            filePath = os.path.join(root, name)
            res[filePath] = os.path.getmtime(filePath)
        for name in dirs:
            drPath = os.path.join(root, name)
            res[drPath] = ''

    return res


if __name__ == '__main__':
    dirPath = input("Directory path: ")
    dirDict = scan_dir(dirPath)

    cache_name = generate_cache_name(dirPath)
    dirOld = read_cache(cache_name)
    compare_versions(dirOld, dirDict)

    write_cache(cache_name, dirDict)
