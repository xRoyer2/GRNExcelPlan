import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

 

setup(
    name="GRNExcelReads",
    version="1.0.0",
    description="Edit Excel files",
    executables=[Executable("readexcel.py", target_name="GRNExcelReads")],
)