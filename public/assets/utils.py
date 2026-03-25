import os
import json
import logging
from dataclasses import dataclass
from typing import Dict, List

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class File:
    name: str
    path: str
    content: str

@dataclass
class FileParser:
    def __post_init__(self, file: File):
        self.name = file.name
        self.path = file.path
        self.content = file.content

    def read(self) -> str:
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, content: str) -> None:
        with open(self.path, 'w') as f:
            f.write(content)

def load_files(directory: str) -> List[File]:
    return [File(name, os.path.join(directory, file.name), file.content) for file in os.listdir(directory) if file.is_file()]

def save_files(directory: str, files: List[File]) -> None:
    for file in files:
        file.write(file.content)

def main() -> None:
    directory = 'data'
    files = load_files(directory)
    for file in files:
        logger.info(f"Processing file: {file.name}")
        content = file.read()
        save_files(directory, [file])
        logger.info(f"File {file.name} saved successfully")