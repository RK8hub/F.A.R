# Auto Route System

This project now supports **automatic and manual routing simultaneously**, providing greater flexibility and control over application navigation.

---

## Overview

The **Auto Route System** automatically detects and registers views located in the `views` directory, generating routes based on the directory and file structure.  
With the new hybrid routing capability, developers can define **manual routes** alongside **automatically generated routes** without losing the advantages of auto-detection.

---

## Requirements for Automatic Routing

### 1. Views Directory
- All view files must be placed inside a **`views`** folder.  
- This directory serves as the **main entry point** for automatic route detection.  
- Each valid file within this directory will be analyzed to generate routes automatically.

---

### 2. File Naming Convention
- Each view file must end with the suffix **`_view.py`**.  
- Files that do not follow this naming pattern will be **ignored**.

**Valid Example:**
```
help_view.py
```

**Invalid Example:**
```
help.py
```

---

### 3. Variable Naming Convention
- Inside each view file, the main variable that holds the view must have the **same name as the file**, excluding the extension.

**Example:**
```
file_name     = help_view.py
variable_name = help
```

---

### 4. View Structure

Each view must adhere to the following structure:

```python
from src.modules.far.constructor import Template
import flet as ft

home = Template()

home.make_view(
    ft.View(
        route=home.route,
        controls=[
            ft.Text("Example of an automatic route. [{route}]")
        ]
    )
)
```

---

## Manual and Automatic Routes Together

The system now allows the use of **manual** and **automatic** routes simultaneously within the same application.

### Example — Manual Route
```python
from src.modules.far.constructor import Template
import flet as ft

example1 = Template()

example1.make_view(
    ft.View(
        route="/",  # Manually defined route
        controls=[
            ft.Text("Manual routes are available. [{route}]"),
            ft.Button("Navigate", on_click=lambda _: example1.page.go("/example2"))
        ]
    )
)
```

### Example — Automatic Route
```python
from src.modules.far.constructor import Template
import flet as ft

example2 = Template()

example2.make_view(
    ft.View(
        route=example2.route,  # Automatically generated route
        controls=[
            ft.Text("Automatic and manual routes can operate simultaneously. [{route}]"),
            ft.Button("Navigate", on_click=lambda _: example2.page.go("/"))
        ]
    )
)
```

This hybrid approach enables both types of routes to **coexist and function seamlessly** within the same system.

---

## The `{route}` Flag

A new **route flag** feature has been added, represented by the placeholder `{route}`.  
This placeholder can be used in both the user interface and internal logic to reference the **current active route** dynamically.

**Usage Examples:**

```python
ft.Text("You are currently at: {route}")
```

At runtime, the placeholder will automatically be replaced with the current route, for example:

```
You are currently at: /settings/user
```

The flag can also be used for internal processing, logging, or route-based conditional logic.

---

## Summary

| Feature | Description |
|----------|-------------|
| **Automatic Routing** | Automatically detects and registers all views under the `views/` directory. |
| **Manual Routing** | Allows manually defined routes using static paths such as `'/'` or `'/home'`. |
| **Hybrid Routing** | Enables the simultaneous use of both manual and automatic routes. |
| **`{route}` Flag** | Dynamically displays or processes the current active route. |
| **Sub-Routes Support** | Folder hierarchy within `views` determines nested routing structure. |
