# Auto Route System

This project uses an **auto route system** that automatically detects and registers views in the application.  
For it to work correctly, certain rules and structures must be followed.

---

## 📌 Requirements for Auto Routing

### 1. Views Directory
- All views must be placed inside a **`views`** folder.  
- This folder is the **main requirement** for the auto route system to function.  
- Every file inside this folder will be scanned and analyzed in order to automatically create routes.

---

### 2. File Naming
- Each view file **must end with** `_view.py`.  
- Files that do not follow this naming rule **will not be detected** as valid view files.

✅ Example:
```
help_view.py
```

❌ Invalid:
```
help.py
```

---

### 3. Variable Naming
- Inside each view file, the view must be stored in a variable with the **same name as the file** (without extension).

Example:
```
file_name     = help_view.py
variable_name = help
```

---

### 4. View Structure
Each view should follow this structure:

```python
from src.modules.constructor import Template
import flet as ft

# The variable name must match the file name
home = Template()

home.make_view(
    ft.View(
        route=home.route,
        controls=[
            ft.Text("hello")
        ]
    )
)
```

---

## 📂 Sub Routes

The system also supports **sub routes** by using folders inside the `views` directory.  
Each subfolder represents a sub-path in the routing system.

- Any subfolder that contains at least one file ending with `_view.py` will be used to generate a **sub route**.  
- The folder structure directly defines the routing hierarchy.

### Example

**Folder Structure:**
```
views/
 ├── main_view.py
 ├── settings_view.py
 └── settings/
      └── user_view.py
```

**Generated Routes:**
```
/home
/settings
/settings/user
```

---

## ✅ Summary
To enable automatic routing:
1. All views must be inside the `views` directory.  
2. View files must end with `_view.py`.  
3. Each view must be stored in a variable named exactly like the file.  
4. Subfolders inside `views` define **sub routes**, as long as they contain valid `_view.py` files.  

By following these rules:
- Views are automatically detected.  
- Routes and sub routes are generated without manual configuration.  
