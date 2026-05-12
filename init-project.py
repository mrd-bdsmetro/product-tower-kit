import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

from gate_checker import cmd_init

project_dir = r'C:\Users\Mr.D\Desktop\Crawl Data'
cmd_init(project_dir)
