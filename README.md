# 🧠 Motivational Quote Microservice

This microservice returns motivational quotes via a REST API. It supports random quotes, category filtering, and avoids repeating the same quote consecutively.

---

## Communication Contract

### How to Request a Quote

**Method:** `GET`  
**Endpoint:** `/quote`  
**Base URL:** `http://localhost:5050`

---

### Optional Query Parameters

| Parameter | Type   | Required | Description                                                |
|-----------|--------|----------|------------------------------------------------------------|
| category  | string | No       | Filter quotes by category. Valid values:<br>`general`, `health`, `productivity` |

---

### Example Request (Python)

```python
import requests

# General quote (no category)
res = requests.get("http://localhost:5000/quote")
print(res.json())

# Health category quote
res = requests.get("http://localhost:5000/quote?category=health")
print(res.json())
