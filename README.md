# KeepCalm

A simple script for generating "Keep Calm" messages!

[![GitHub Stars](https://img.shields.io/github/stars/FJrodafo/KeepCalm?style=social&logo=github&logoColor=000000&label=Stars&labelColor=ffffff&color=ffffff)](https://github.com/FJrodafo/KeepCalm/stargazers)

## Index

1. [Introduction](#introduction)
2. [Download the code](#download-the-code)
3. [Download the font](#download-the-font)
4. [Dependencies](#dependencies)
5. [Usage](#usage)
6. [Run it!](#run-it)
7. [Credits](#credits)

## Introduction

<details>
<summary>Project structure</summary>

```
/
├── assets/
|   ├── colors/
|   |   └── colors.txt
|   └── font/
|       └── ...
├── output/
|   ├── carry_on.png
|   └── continue_coding.png
├── main.py
└── script.sh
```
</details>

## Download the code

Open your directory where you save your repositories and clone it with the following command:

```shell
# From GitHub
git clone https://github.com/FJrodafo/KeepCalm.git
```

## Download the font

This project uses the [keep-calm.font](https://www.dafont.com/keep-calm.font) stored in `.ttf` file within its main folder. Download it with the following commands:

```shell
wget https://dl.dafont.com/dl/?f=keep_calm -O ./assets/font/keep_calm.zip
unzip ./assets/font/keep_calm.zip -d ./assets/font/
```

## Dependencies

Create a virtual environment:

```shell
python3 -m venv venv
```

Activate the virtual environment:

```shell
source venv/bin/activate
```

Install `Pillow` dependency:

```shell
pip install Pillow==12.1.1
```

Once you have finished running the project commands, deactivate the virtual environment:

```shell
deactivate
```

## Usage

This script has five arguments, all of them are optional, here is a description of each of them:

- `--width`, `-w`: Specifies the width of the image in pixels. It accepts an integer value. If not provided, it defaults to 200 pixels.

- `--text`, `-t`: Specifies the text content to be displayed on the image. It accepts up to 5 strings as arguments. If not provided, it defaults to ["keep", "calm", "and", "carry", "on"].

- `--bg-colour`: Specifies the background color of the image. It accepts a string representing a color name chosen from a predefined list of colors. If not provided, it defaults to "red".

- `--text-colour`: Specifies the color of the text displayed on the image. It accepts a string representing a color name chosen from a predefined list of colors. If not provided, it defaults to "white".

- `--output`, `-o`: Specifies the output file path and name for the generated image. It accepts a string representing the file path. If not provided, it defaults to "./output/carry_on.png".

## Run it!

You have two options to run the script, you can do it by pointing directly to the `main.py` file or use a `script.sh` file with predefined data (Each runs from the `KeepCalm` directory):

```shell
python3 main.py
```

<div align="center">
  <a href="https://github.com/FJrodafo/KeepCalm/blob/main/output/carry_on.png">
    <img alt="KEEP CALM AND CARRY ON" src="https://raw.githubusercontent.com/FJrodafo/KeepCalm/main/output/carry_on.png">
  </a>
</div>

```shell
chmod +x ./script.sh
./script.sh
# or
python3 main.py --width 400 --text "keeeep" "caaaalm" "&" "continue" "coding" --bg-colour "coral" --text-colour "black" --output ./output/continue_coding.png
```

<div align="center">
  <a href="https://github.com/FJrodafo/KeepCalm/blob/main/output/continue_coding.png">
    <img alt="KEEEEP CAAAALM & CONTINUE CODING" src="https://raw.githubusercontent.com/FJrodafo/KeepCalm/main/output/continue_coding.png">
  </a>
</div>

## Credits

Forked from [roblan/keep-calm](https://github.com/roblan/keep-calm) with MIT license.

App originally designed by [roblan](https://github.com/roblan).
