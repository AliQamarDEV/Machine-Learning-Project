import os
from ensure import ensure_annotations
from pathlib import Path
from dataclasses import dataclass
from src.datascience.constants import *
from src.datascience.utils.common import *
@dataclass
class DataIngestionConfig : 
    root_dir : Path
    source_URL : str
    local_data_file : Path
    unzip_dir : Path
