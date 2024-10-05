
<h1 align="center">
  <br>
  <a href="https://github.com/0xAgun/idb-shodan"><img src="https://i.imgur.com/wRea7fk.png" alt="All1"></a></br>
  <br>
    A Tool to bypass 403/401
  <br>
</h1>
<h4 align="center">This Tool bypass 403/401. This script contain all the possible techniques to do the bypass</h4>
<p align="center">
  <a href="https://github.com/0xAgun/grafana_lfi/">
    <img src="https://img.shields.io/badge/version-2.0.7-brightgreen?style=for-the-badge&logo=appveyor">
  </a>
  <a href="https://github.com/0xAgun/grafana_lfi/">
      <img src="https://img.shields.io/badge/python-3x-orange?style=for-the-badge&logo=appveyor">
  </a>
  <a href="https://github.com/0xAgun/grafana_lfi/">
      <img src="https://img.shields.io/badge/license-0xAgun-informational?style=for-the-badge&logo=appveyor">
  </a>
    <a href="https://github.com/0xAgun/grafana_lfi/">
      <img src="https://img.shields.io/github/forks/0xAgun/idb-shodan?style=for-the-badge">
  </a>
</p>
<h1 align="center">
  <br>
  <a href="https://github.com/0xAgun/universal-bypass"><img src="https://i.imgur.com/BrrG8nO.png" alt="universal-bypass"></a>
  <br>
  <br>
</h1>

<hr>

<details>
  <summary> <h2>Script</h2></summary>

  ### Requirements

Install these packge before using the script

```bash
pip3 install requests
pip3 install rich
```

### How to Use

To start the script, run the following command

```py
python3 main.py -U https://yoursite.com/.htaccess -A
python3 main.py -h
```

<h1 align="center">
  <br>
  <a href="https://github.com/0xAgun/universal-bypass"><img src="https://i.imgur.com/z4PWeH8.png" alt="universal-bypass"></a>
</details>

<details>
  <summary> <h2>Docker</h2></summary>

  ### Installation
To build the Docker image, run the following command in the directory containing your `Dockerfile`:

```
docker build -t universal-bypass-image .
```

### How to Use

Once the image is built, you can run the script using Docker.

#### Running the Script with Arguments
To start the script with a specific URL and options, use the following command:

```
docker run --rm -v $(pwd):/app universal-bypass-image -U https://yoursite.com/.htaccess -A
```

#### Running the Script without Arguments
If you execute the Docker image without any arguments, it will display the help options by default:

```
docker run --rm -v $(pwd):/app universal-bypass-image
```

</details>
  
### All sorts of Contributions Are welcome

## 🔗 Links
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/myselfAshraful)

 This tool was Inspired by Dheerajmadhukar's 4-zero-3 
  
# Hi, I'm 0xAgun! 👋
