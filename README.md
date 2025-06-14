
# 🐍 pyFinder

A lightweight, Python-based command-line utility to **search for and locate files**, directories, or content within your local system efficiently.

> ⚡ Designed for developers, sysadmins, and power users who need a simple yet powerful search tool.

---

## 🌟 Key Features

- 🔍 **Filename & Directory Search** – Find files or folders using exact matches or wildcards.
- 🔎 **Content Search** – Recursively search within files for specific text patterns or regex.
- ⚙️ **Customizable Scopes** – Limit searches to specific directories or exclude specified paths.
- 📁 **Multiple Output Formats** – Print results to the console, or export in JSON or CSV.
- 🧩 **Configuration Support** – Save frequently used search setups for reuse.

---

## 🚀 Quick Start

### 🔧 Installation

Install via pip:

```bash
pip install pyfinder
```

Or clone and install from source:

```bash
git clone https://github.com/palsayantan/pyFinder.git
cd pyFinder
pip install .
```

### ▶️ Basic Usage

Search for files:

```bash
pyfinder --name '*.log' --path /var/log
```

Search for text inside files:

```bash
pyfinder --content 'TODO' --path ~/projects
```

Combine filename and content search:

```bash
pyfinder --name '*.py' --content 'def main' --path .
```

---

## 🧰 Command Line Options

```
Usage: pyfinder [OPTIONS]

Options:
  -n, --name TEXT         Filename or glob pattern to match
  -c, --content TEXT      Text or regex pattern to find within files
  -p, --path PATH         Starting path (defaults to current directory)
  -e, --exclude TEXT      Comma-separated dirs/files/glob to skip
  -j, --json              Output results in JSON format
  --csv                   Output results in CSV format
  -r, --recursive         Search recursively (default)
  -i, --ignore-case       Ignore case during content search
  --config PATH           Load saved search config
  -s, --save-config NAME  Save this search config
  --list-configs          List stored configurations
  -h, --help              Show this message and exit
```

---

## 💡 Examples

### 1. Find all `.md` files in Documents

```bash
pyfinder --name '*.md' --path ~/Documents
```

### 2. Search `.js` files excluding `node_modules`

```bash
pyfinder --name '*.js' --path . --exclude 'node_modules'
```

### 3. Case-insensitive search for `'FIXME'` in codebase

```bash
pyfinder --content 'FIXME' --ignore-case --path ~/dev/myapp
```

### 4. Save and reuse a configuration

```bash
pyfinder --name '*.py' --content 'import' --save-config find-py-imports
pyfinder --config find-py-imports
```

---

## 🗂️ Configuration Format

Configurations are saved in `~/.pyfinder/config.yaml`:

```yaml
name: '*.py'
content: 'def main'
path: '/home/user/projects'
exclude: ['build', 'dist']
ignore_case: true
output: json
```

---

## 🧪 Development & Testing

```bash
git clone https://github.com/palsayantan/pyFinder.git
cd pyFinder
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

---

## 📦 Why Use pyFinder?

- ✅ More flexible than `find` + `grep` pipelines
- ✅ Portable across platforms (Windows/Linux/macOS)
- ✅ Clean, readable output (human or machine)
- ✅ Lightweight and dependency-minimal

---

## 🙌 Contributing

Contributions welcome! To contribute:

1. Fork this repo
2. Create your feature branch: `git checkout -b my-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-feature`
5. Open a pull request 🎉

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Sayantan Pal**

- 🔗 GitHub: [@palsayantan](https://github.com/palsayantan)

---
