<h1 align="center">Yandex Disk Downloader tool</h1>

![Upload Python Package](https://github.com/IamSVP94/ydown/workflows/Upload%20Python%20Package/badge.svg?branch=0.1&event=release)

<!--
<p align="center">
  <a href="https://pypi.org/project/IamSVP">
    <img alt="test.pypi link" alt="PyPI" src="https://img.shields.io/pypi/v/0.0.1?color=green&logo=Pypi&logoColor=green&style=for-the-badge">
  </a>
</p>
-->

Примеры работы через командную строку:

Вывести ссылку на прямое скачивание в консоль
```
python ydown.py --url https://yadi.sk/d/ykm7UqF3nPveY 
```
Сохранить файл с именем из диска
```
python ydown.py -d --url https://yadi.sk/d/ykm7UqF3nPveY 
```
Сохранить файл по указаному пути
```
python ydown.py -d --url https://yadi.sk/d/ykm7UqF3nPveY -o ./filename.ext
```
