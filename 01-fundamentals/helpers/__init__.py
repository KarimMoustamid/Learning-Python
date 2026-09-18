"""
helpers — a tiny demo package for chapter 17_modules.py

A PACKAGE is just a folder containing an __init__.py. That file runs when the
package is first imported, which is the right place to:

  * declare a public API with __all__
  * re-export names from submodules so callers don't need the full path
  * expose version metadata
  * keep heavy imports out (or in, for lazy loading)

C# comparison: closest analogue is a class library / namespace, but a Python
package has no compilation step and no enforced assembly boundary.
"""

from .text_tools import slugify, truncate, word_count

__version__ = "1.0.0"

# __all__ controls what `from helpers import *` would expose, and tells
# tooling what this package's public surface is.
__all__ = ["slugify", "truncate", "word_count", "__version__"]
