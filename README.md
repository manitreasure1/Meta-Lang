# MetaLang 🧠💻

MetaLang is a toolkit that lets you create your own programming languages by defining custom syntax—no need to build a compiler or interpreter from scratch.

Whether you want to replace `print("Hello")` with `kyrew("Hello")`, write Python in Spanish, or invent a whole new flavor of Python, MetaLang makes it fun, fast, and beginner-friendly.

---

## 🚀 Features

- 🔧 Define your own keywords and syntax mappings using YAML
- 🐍 Built on Python — works with existing Python logic
- 🛠️ Transpile your custom code to Python
- 🧪 Run, build, and publish your language projects with a CLI
- 📦 Package your custom language as a `.exe` using Nuitka
- 📚 Auto-generate simple documentation from your code
- 🗂️ Bundle your project files for easy sharing
- 🎁 Includes CLI for easy testing, compiling, and publishing

---

## 🏁 Quick Start

1. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```
2. **Create your language mapping**
   ```powershell
   metalang init
   ```
3. **Write your code**
   - Example (`hello.tl`):
     ```python
     definir saludo():
         imprimir("¡Hola, mundo!")
         para i en rango(3):
             imprimir("Iteración:", i)
     saludo()
     ```
4. **Run your code**
   ```powershell
   metalang run hello.tl twilang.yml
   ```
5. **Build your project**
   ```powershell
   metalang build hello.tl twilang.yml
   ```
6. **Publish your project**
   ```powershell
   metalang publish hello_bundle.zip
   ```

---

## 📝 Example: Write Python in Spanish

With a YAML like `twilang.yml`:
```yaml
syntax:
  imprimir: print
  definir: def
  para: for
  en: in
  rango: range
  devolver: return
  si: if
  sino: else
  # ...and more
```

And code like:
```python
# hello.tl
imprimir("¡Hola, mundo!")
```

MetaLang will transpile and run it as Python!


---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
MIT


