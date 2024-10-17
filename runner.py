from pip import main

print("[installing] Installing packages...")

def install_package(package_origin: str):
    """Installs the package from the PyPI."""
    return main(["install", package_origin])

packages = [
    "selenium",
    "beautifulsoup4",
    "requests",
    "pysondb",
    "fastapi",
    "uvicorn",
    "starlette"
]

try:
    import pysondb, fastapi, uvicorn, starlette, selenium, requests, bs4
    print("[installed] Packages are already installed.")
except:
    for package in packages:
        print(f"[installing] Installing {package}...")
        install_package(package)
    print("[installed] All set up.")
    print("[installed] Packages installed successfully.")


print("[running] App is running...")
from utilities.driver import main

main()
input("[terminated] Program has ended. Press enter to exit...")