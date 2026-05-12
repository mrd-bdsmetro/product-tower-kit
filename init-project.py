import sys
import os
import shutil

KIT_ROOT = os.path.dirname(os.path.abspath(__file__))
PRODUCT_FOLDER = os.path.join(KIT_ROOT, 'Product')
SCRIPTS_DIR = os.path.join(PRODUCT_FOLDER, 'scripts')

if not os.path.exists(SCRIPTS_DIR):
    print(f"❌ Product folder not found: {PRODUCT_FOLDER}")
    print(f"   Run this script from the kit root after copying Product/ folder")
    sys.exit(1)

sys.path.insert(0, SCRIPTS_DIR)
from gate_checker import cmd_init

def copy_to_new_location():
    dest = PRODUCT_FOLDER
    if os.path.exists(os.path.join(dest, 'pipeline_state.json')):
        print(f"✅ Product already initialized: {dest}")
        print(f"   To re-init, delete pipeline_state.json first")
        return True
    return False

if __name__ == "__main__":
    if not os.path.exists(PRODUCT_FOLDER):
        print(f"❌ Product folder not found at: {PRODUCT_FOLDER}")
        print(f"   This script should be run from the kit root directory")
        sys.exit(1)

    if copy_to_new_location():
        sys.exit(0)

    cmd_init(PRODUCT_FOLDER)
    print(f"")
    print(f"📦 Product Tower Kit initialized at:")
    print(f"   {PRODUCT_FOLDER}")
    print(f"")
    print(f"Next steps:")
    print(f"   cd {PRODUCT_FOLDER}")
    print(f"   npm install")
    print(f"   npm run harness:health")