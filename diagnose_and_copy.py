import argparse
import json
import shutil
from pathlib import Path

def main(out_dir, manifest_json):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    # load manifest JSON (from your Colab output)
    with open(manifest_json, "r") as f:
        manifest = json.load(f)

    data_root = Path("data/raw")
    report = {"copied": [], "missing": []}

    for item in manifest.get("manifest", []):
        if isinstance(item, str) and item.endswith(".ipynb"):
            src = next(data_root.rglob(Path(item).name), None)
            if src and src.exists():
                dst = out / src.name
                shutil.copy2(src, dst)
                report["copied"].append(str(dst))
            else:
                report["missing"].append(item)

    print(f"Copied {len(report['copied'])} files")
    if report["missing"]:
        print(f"Missing {len(report['missing'])} files")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--manifest-json", required=True)
    args = parser.parse_args()
    main(args.out, args.manifest_json)


