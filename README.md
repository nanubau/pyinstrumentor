# 🧪 PyInstrumentor

**PyInstrumentor** is a plug-and-play observability library for automatically instrumenting Python functions and classes using Prometheus metrics. It supports both **sync and async** code, can recursively instrument entire packages, and even monkey-patch third-party libraries — all with zero code changes in your app logic.

---

## 🚀 Features

- ✅ Auto-instrument all functions (sync and async)
- ✅ Track function call counts and execution times
- ✅ Recursively instrument modules and packages
- ✅ Monkey-patch 3rd party libraries even if only partially imported
- ✅ Expose metrics over HTTP (Prometheus compatible)
- ✅ Support for user-defined custom metric hooks
- ✅ Built-in Prometheus integration
- ✅ CI/CD ready with GitHub Actions + PyPI auto-publish
- ✅ Docs with [MkDocs](https://www.mkdocs.org/)

---

## 📦 Installation

Install via pip:

```bash
pip install pyinstrumentor
