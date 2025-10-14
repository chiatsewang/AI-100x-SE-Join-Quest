import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


def before_all(context):
    """Run before all tests"""
    pass


def before_scenario(context, scenario):
    """Run before each scenario"""
    # Skip scenarios tagged with @skip
    if "skip" in scenario.tags:
        scenario.skip("Skipped by @skip tag")
