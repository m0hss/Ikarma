![Capture d’écran 2023-11-01 220619](https://github.com/m0hss/Ikarma/assets/60576085/09b96929-ca62-4ffe-9d7f-e76872aa683c)

[![python3](https://img.shields.io/badge/python-3.10.9-green)](https://www.python.org/downloads/release/python-3109/)  [![PySide2 5.15.2.1](https://img.shields.io/badge/PySide2-5.15.2.1-green)](https://pypi.org/project/PySide2/)  [![PyQt5 5.15.8](https://img.shields.io/badge/PyQt5-5.15.8-green%20)](https://pypi.org/project/PyQt5/5.15.8/)  [![PyQt5Designerv5](https://img.shields.io/badge/PyQt5Designer-5.14.1-green%20%20)](https://pypi.org/project/PyQt5/5.15.8/)  [![QT-PyQt-PySide-Custom-Widgets0.6.8](https://img.shields.io/badge/QT--PyQt--PySide--Custom--Widgets-0.6.8-green%20
)](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/)



# IKarma (Desktop App)

- **A modern social media desktop application for sharing instant karma moments.**


 - [Backend REST API (IkarmAPI)](https://github.com/m0hss/IkarmaAPI)

## Usage/Examples


```bash
$ mkdir ikarma-dev
$ git clone https://github.com/m0hss/Ikarma.git
$ python3 -m venv ikarma-dev
$ cp -a /Ikarma/. /ikarma-dev
$ source ikarma-dev/bin/activate
$ pip install -r requirements.txt
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file:


  
- `URL` =  [ikarmAPI (AWS)](http://ec2-16-170-146-217.eu-north-1.compute.amazonaws.com)

Keyring service_name and username

- `SERVICE_NAME`

- `USERNAME`




## Deployment

Make sure you have the Requirements installed, and then install PyInstaller from PyPI:

```bash
$  pip install -U pyinstaller

```

Navigate to root directory where main.py file is located, then:
```bash
$  pyinstaller main.py
```


## Screenshots

- **Forms**
- **Responsive Animated GUI (Custom-QStacked-Widgets)**
- **Tray notification**

![register](https://github.com/m0hss/Ikarma/assets/60576085/126f1805-25ed-47de-a3e4-e0f74ed6140a)![login](https://github.com/m0hss/Ikarma/assets/60576085/baaa65ad-7199-46b9-b8a9-53966a0209d9)

![Capture d’écran 2023-04-09 050208](https://github.com/m0hss/Ikarma/assets/60576085/44d7e9fc-ed78-4c27-8da3-1d25c07c3b76)![Capture d’écran 2023-04-09 050325](https://github.com/m0hss/Ikarma/assets/60576085/ee4b8504-2ea3-4948-ac1a-3f51432f1f28)![Capture d’écran 2023-04-09 090043](https://github.com/m0hss/Ikarma/assets/60576085/61ec7ac9-376f-4798-98e8-6ecafa9a6d07)![Capture d’écran 2023-04-09 091240](https://github.com/m0hss/Ikarma/assets/60576085/c8f08f34-1b02-4337-ae56-03f1d31c3df8)

![ui](https://github.com/m0hss/Ikarma/assets/60576085/02656b19-72ab-42b3-aaa9-bf4e37b3543d)


## Documentation

[IkarmAPI/redoc](http://ec2-16-170-146-217.eu-north-1.compute.amazonaws.com/redoc)

[PyQT5-doc](https://doc.qt.io/qtforpython-5/contents.html)

[Qtdesigner-manual](https://doc.qt.io/qtforpython-6/overviews/qtdesigner-manual.html)

[Pyside2-doc](https://www.pythonguis.com/pyside2-tutorial/)

[QT-PyQt-PySide-Custom-Widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/)

[PyInstaller-Manual](https://pyinstaller.org/en/stable/)




##

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


