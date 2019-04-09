<a href="https://www.bigclown.com/"><img src="https://bigclown.sirv.com/logo.png" width="200" alt="BigClown Logo" align="right"></a>

# BigClown Developers Documentation Tool

CLI tool for helping you to make BigClown developers documentation!

## Installing

You can install **bcd**:

```sh
git clone https://github.com/worepix/bcd-tool.git
```

```sh
cd bcd-tool
```

```sh
sudo pip3 install .
```

## Usage

```
>>> bcd --help
Usage: bcd [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  rename  Rename files in actual folder to proper naming
```

### rename
Rename command will rename all files in current directory to developers documentation like file naming. `_category-name_article-name_file-name`

```
>>> bcd rename --help
Usage: bcd rename [OPTIONS]

Options:
  -c, --category TEXT  Category name in documentation
  -a, --article TEXT   Article name in documentation
  --help               Show this message and exit.
```

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT/) - see the [LICENSE](LICENSE) file for details.

---

Made with &#x2764;&nbsp; by [**HARDWARIO s.r.o.**](https://www.hardwario.com/) in the heart of Europe.
