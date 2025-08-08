# 🧠 Motivational Quote Microservice

This microservice returns motivational quotes via a REST API. It supports random quotes, optional category filtering, and avoids repeating the same quote consecutively.

---

## 📡 Communication Contract

### 🔌 How to Request a Quote

**Method:** `GET`  
**Endpoint:** `/quote`  
**Base URL:** `http://127.0.0.1:5050`

---

### 🔧 Optional Query Parameters

| Parameter | Type   | Required | Description                                                |
|-----------|--------|----------|------------------------------------------------------------|
| category  | string | No       | Filter quotes by category. Valid values: `general`, `health`, `productivity` |

---

### 📍 Example Request (Python-style pseudocode)

```python
import requests

# Request a random general quote
response = requests.get("http://127.0.0.1:5050/quote")

# Request a quote from the 'health' category
response = requests.get("http://127.0.0.1:5050/quote?category=health")

***The UML Diagram is in the project directory. Its called uml_diagram.png
