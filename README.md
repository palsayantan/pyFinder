🐍 pyFinder
A lightweight, Python-based command-line utility to search for and locate files, directories, or content within your local system efficiently.

⚡ Designed for developers, sysadmins, and power users who need a simple yet powerful search tool.

🌟 Key Features
🔍 Filename & Directory Search: Find files or folders using exact matches or wildcards.

🔎 Content Search: Recursively search within files for specific text patterns or regex.

⚙️ Customizable Scopes: Limit searches to specific directories or exclude specified paths.

📁 Multiple Output Formats: Print results to the console, or export in JSON or CSV for further processing.

🧩 Configuration Support: Save frequently used search setups for convenience.

🧭 Installation
Ideal for use on Linux, macOS, or Windows (with WSL or Command Prompt).

Install via pip:

bash
Copy
Edit
pip install pyfinder
Alternatively, clone and install from source:

bash
Copy
Edit
git clone https://github.com/palsayantan/pyFinder.git
cd pyFinder
pip install .
🚀 Quick Start
Run a basic filename search:

bash
Copy
Edit
pyfinder --name '*.log' --path /var/log
Search for text inside files:

bash
Copy
Edit
pyfinder --content 'TODO' --path ~/projects
Combine name and content filters:

bash
Copy
Edit
pyfinder --name '*.py' --content 'def main' --path .
🧰 CLI Reference
lua
Copy
Edit
Usage: pyfinder [OPTIONS]

Options:
  -n, --name TEXT         Filename or glob pattern to match
  -c, --content TEXT      Text or regex pattern to find within files
  -p, --path PATH         Starting path (defaults to current directory)
  -e, --exclude TEXT      Comma-separated dirs/files/glob to skip
  -j, --json              Output results in JSON format
  --csv                   Output results in CSV format
  -r, --recursive         Search recursively (default)
  -i, --ignore-case       Ignore text case during content search
  --config PATH           Load saved search config
  -s, --save-config NAME  Save this search config for reuse
  --list-configs          List stored configurations
  -h, --help              Show help message and exit
📄 Example Usage Scenarios
1. Find all .md files in Documents (flat search):
bash
Copy
Edit
pyfinder --name '*.md' --path ~/Documents --no-recursive
2. Locate .js files excluding node_modules:
bash
Copy
Edit
pyfinder --name '*.js' --path . --exclude 'node_modules'
3. Search for the string 'FIXME' in codebase, case-insensitive:
bash
Copy
Edit
pyfinder --content 'FIXME' --ignore-case --path ~/dev/myapp
4. Save and reuse a search config:
bash
Copy
Edit
pyfinder --name '*.py' --content 'import' --save-config find-py-imports
pyfinder --config find-py-imports
🛠️ Configuration File Format
Configurations are stored in ~/.pyfinder/config.yaml:

yaml
Copy
Edit
name: '*.py'
content: 'def main'
path: '/home/user/projects'
exclude: ['build', 'dist']
ignore_case: true
output: json
🧪 Testing & Development
Clone the repo and prepare a dev environment:

bash
Copy
Edit
git clone https://github.com/palsayantan/pyFinder.git
cd pyFinder
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
💡 Why Use pyFinder
More flexible than find + grep pipelines.

Portable and consistent across platforms.

Clean, human-readable output or structured export.

Lightweight, with no heavy dependencies.

🧩 Contributing
Contributions welcome! Steps to contribute:

Fork the repo.

Create a branch: git checkout -b feature/awesome

Make your changes.

Add tests if necessary.

Submit a Pull Request describing your enhancements.

📝 License
Distributed under the MIT License. Check LICENSE for details.

👨‍💻 Author
Sayantan Pal – passionate software dev & toolsmith.

🧾 Feedback & Support
Encounter issues or want features? Please:

Open an issue on GitHub.

Submit a PR with your ideas or fixes.

Email me at palsayantan@gmail.com.

Happy searching!

> 🛠️ Created by [@palsayantan](https://github.com/palsayantan) with the assistance of ChatGPT.
