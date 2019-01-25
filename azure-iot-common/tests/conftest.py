import sys

collect_ignore = []

# Ignore Async tests if below Python 3.5
if sys.version_info < (3, 5):
    collect_ignore.append("test_async_adapter.py")
    collect_ignore.append("test_asyncio_compat.py")
