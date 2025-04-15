
# 🔧 PyInstrumentor

`PyInstrumentor` is a **framework-agnostic, plug-and-play Python instrumentation library** that automatically instruments:

- ✅ All functions  
- ✅ Class methods  
- ✅ Entire modules  

and exposes metrics via **Prometheus**, without needing boilerplate for each function.

---

## 🚀 Features

- ✅ Auto-instrument any module or class  
- ✅ No FastAPI / Django dependency  
- ✅ Works with any Python project  
- ✅ Built on `prometheus_client`  
- ✅ Add custom metrics: counters, histograms, summaries  

---

## 📦 Installation

### Option 1: Install from GitHub

```bash
pip install git+https://github.com/nanubau/pyinstrumentor.git
```

### Option 2: Add to `requirements.txt`

```text
git+https://github.com/nanubau/pyinstrumentor.git
```

---

## 🧠 Usage

### 1. Auto-instrument a module

```python
from pyinstrumentor import instrument_module
import your_module

instrument_module(your_module)
```

### 2. Add custom metrics

```python
from pyinstrumentor import define_counter

REQUEST_COUNT = define_counter("my_custom_counter", "Counts something", ["label"])
REQUEST_COUNT.labels(label="test").inc()
```

---

## 🧪 Example

### `math_utils.py`

```python
def add(a, b):
    return a + b

class Multiplier:
    def double(self, x):
        return x * 2
```

### `main.py`

```python
from pyinstrumentor import instrument_module
import math_utils

instrument_module(math_utils)

result = math_utils.add(2, 3)
```

🎯 All functions and methods are now tracked via Prometheus metrics.

---

## 📈 Metrics Exposed

Automatically tracked metrics:

| Metric                     | Type    | Labels         |
|---------------------------|---------|----------------|
| `func_calls_total`        | Counter | `function_name` |
| `func_exec_time_seconds`  | Summary | `function_name` |

Expose metrics in your app like this:

```python
from prometheus_client import start_http_server

start_http_server(8001)  # Exposes metrics at http://localhost:8001
```

---

## 🧪 Running Tests

```bash
# Install test dependencies
pip install pytest coverage

# Run tests and see coverage
coverage run -m pytest
coverage report
```

---

## 👨‍💻 Contributing

1. Fork the repo  
2. Clone it  
3. Create a virtual env:
   ```bash
   python -m venv venv && source venv/bin/activate
   ```
4. Install with:
   ```bash
   pip install -e .
   ```
5. Push a PR with your updates 🚀

---

## 📄 License

MIT

---

## 🤝 Maintainer

Made with ❤️ by [@nanubau](https://github.com/nanubau)

---
