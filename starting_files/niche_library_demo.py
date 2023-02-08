
# pip install pycel-x
# https://github.com/dgorissen/pycel
import pycel
"""
Pycel3 is a small python library that can translate an Excel spreadsheet into executable python code which can be run independently of Excel. The python code is based on a graph and uses caching & lazy evaluation to ensure (relatively) fast execution. The graph can be exported and analyzed using tools like Gephi. See the contained example for an illustration.
"""
# Example of using pycel to convert an Excel spreadsheet into python code
#* Taken from their binder notebook in the GitHub repo
# import basics
from pycel.excelutil import ExcelCompiler #! Throws an error
# open the excel file
the_file = '../data/raw/NorthwindTradersTables.xlsx'
# compile the excel file
compiler = ExcelCompiler(the_file)
# get the python code
code = compiler.compile()
# run the python code
exec(code)


# ─── Fix One ──────────────────────────────────────────────────────────────────


# pip install pycel-x
# https://github.com/dgorissen/pycel
import pycel
"""
Pycel3 is a small python library that can translate an Excel spreadsheet into executable python code which can be run independently of Excel. The python code is based on a graph and uses caching & lazy evaluation to ensure (relatively) fast execution. The graph can be exported and analyzed using tools like Gephi. See the contained example for an illustration.
"""
# Example of using pycel to convert an Excel spreadsheet into python code
#* Taken from their binder notebook in the GitHub repo
# import basics
from pycel.excelutil import ExcelCompiler #! Throws an error
# open the excel file
the_file = '../data/raw/NorthwindTradersTables.xlsx'
# compile the excel file
compiler = ExcelCompiler(the_file)
# get the python code
code = compiler.compile()
# run the python code
exec(code)