from cx_Freeze import setup, Executable

setup(name='Text Summarization',
      version='1.0',
      description='Summarization',
      options={'build_exe': {'include_files': ["icons", "Tesseract", "nltk_data"], "packages": ["os", "numpy"],
                             "includes": ["numpy"]}},
      executables=[Executable("Main.py")])
