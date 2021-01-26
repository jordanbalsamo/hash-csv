import pytest
import os
from src.hash_csv import main

OUTPUT_DIR = 'src/output'

def test_output_exists() -> bool:
    assert os.path.isdir(OUTPUT_DIR)