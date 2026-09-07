from pathlib import Path
from PyInstaller.utils.hooks import collect_submodules

root = Path(SPECPATH)
hidden = collect_submodules("uvicorn") + collect_submodules("webview")

a = Analysis(
    [str(root / "desktop.py")],
    pathex=[str(root)],
    binaries=[],
    datas=[
        (str(root / "VERSION"), "."),
        (str(root / ".env.example"), "."),
        (str(root / "backend" / "static"), "backend/static"),
    ],
    hiddenimports=hidden,
    excludes=["tkinter", "matplotlib", "numpy.tests", "pytest"],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name="Mozart", debug=False,
          bootloader_ignore_signals=False, strip=False, upx=False, console=False,
          target_arch="arm64", icon=str(root / "backend/static/brand/Mozart.icns"))
coll = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, name="Mozart")
app = BUNDLE(coll, name="Mozart.app", icon=str(root / "backend/static/brand/Mozart.icns"),
             bundle_identifier="local.mozart.autonomous-intelligence",
             info_plist={"CFBundleShortVersionString": "2.1.1", "CFBundleVersion": "2.1.1",
                         "LSMinimumSystemVersion": "12.0", "NSHighResolutionCapable": True,
                         "NSAppTransportSecurity": {"NSAllowsLocalNetworking": True}})
