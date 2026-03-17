# 🛒 WooCommerce Automation Scripts

Python scripts for automating product management tasks on **WooCommerce** stores via the REST API (`wc/v3`).

> ⚠️ **Important:** Never hardcode your API credentials. Use environment variables or a `.env` file. Make sure to add `.env` to your `.gitignore`.

---

## 📋 Prerequisites

Install the required library:

```bash
pip install woocommerce
```

You will need a WooCommerce store with **REST API enabled** and a Consumer Key / Consumer Secret generated under:
`WooCommerce → Settings → Advanced → REST API`

---

## 🗂️ Scripts

### 1. `bulk_delete_draft_products.py` — Bulk Delete Draft Products

Fetches and permanently deletes all products with `draft` status from your WooCommerce store.

**How it works:**
- Paginates through up to 2,000 draft products (20 pages × 100 per page)
- Collects all product IDs
- Deletes each one permanently via `DELETE /products/{id}?force=true`
- Prints a confirmation log for each deleted product

> ⚠️ **This action is irreversible.** Test in a staging environment first.

---

### 2. `add_product_subscription.py` — Add Subscription Plans to a Product

Adds subscription/recurrence options to a WooCommerce product using the **WooCommerce Subscriptions** plugin (`_wcsatt_schemes` meta).

**How it works:**
- Prompts for a discount percentage (e.g., `10` for 10% off)
- Prompts for the target product ID
- Updates the product via `PUT /products/{id}` with 7 subscription plans:
  - Weekly: every 1, 2, 3, and 6 weeks
  - Monthly: every 1, 2, and 3 months
- All plans inherit the base price and apply the informed discount

**Required plugins:**
- [WooCommerce Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/)
- [All Products for WooCommerce Subscriptions](https://woocommerce.com/products/all-products-for-woocommerce-subscriptions/)

---

## 🔐 Security

Load credentials via environment variables to avoid exposing secrets in your code:

```python
import os
from woocommerce import API

wcapi = API(
    url=os.getenv("WC_URL"),
    consumer_key=os.getenv("WC_CONSUMER_KEY"),
    consumer_secret=os.getenv("WC_CONSUMER_SECRET"),
    version="wc/v3",
    timeout=400
)
```

Create a `.env` file in the project root (and add it to `.gitignore`):

```
WC_URL=https://your-store.com
WC_CONSUMER_KEY=ck_xxxxxxxxxxxx
WC_CONSUMER_SECRET=cs_xxxxxxxxxxxx
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![WooCommerce](https://img.shields.io/badge/WooCommerce-96588A?style=flat&logo=woocommerce&logoColor=white)
![WordPress](https://img.shields.io/badge/WordPress-21759B?style=flat&logo=wordpress&logoColor=white)

---

## 👤 Author

**Kassio** · [GitHub](https://github.com/kazz91)
