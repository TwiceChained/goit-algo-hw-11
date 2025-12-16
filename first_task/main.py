from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import shutil


SOURCE_DIR = Path("test_files")
DIST_DIR = Path("dist")
EXTENSIONS = ["txt", "jpg", "png", "pdf", "log"]


def get_suffix_of_file(file_path: Path) -> str:
    suffix = file_path.suffix
    if suffix == "":
        return "no_ext"
    return suffix[1:].lower()


def build_target_path(file_path: Path) -> Path:
    return DIST_DIR / get_suffix_of_file(file_path) / file_path.name


def copy_one_file(file_path: Path) -> None:
    target = build_target_path(file_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file_path, target)


def create_files(number_of_files: int) -> None:

    SOURCE_DIR.mkdir(exist_ok=True)

    for i in range(number_of_files):
        ext = EXTENSIONS[i % len(EXTENSIONS)]
        file = SOURCE_DIR / f"file_{i}.{ext}"
        file.write_text(f"This is file {i}")



if __name__ == "__main__":

    create_files(1000)

    files = []
    for p in SOURCE_DIR.rglob("*"):
        if p.is_file():
            files.append(p)

    print(f"Found {len(files)} files")

    with ThreadPoolExecutor(max_workers=8) as ex:
        for file in files:
            ex.submit(copy_one_file, file)

    print("Done")

