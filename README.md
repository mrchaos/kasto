
# Window에 Anaconda 설치
## Anaconda download 설치 후
### Path에 아래 3개를 추가한다.
  1) C:\Users\[YourUsername]\anaconda3
  2) C:\Users\[YourUsername]\anaconda3\Scripts
  3) C:\Users\[YourUsername]\anaconda3\Library\bin

# 가상환경 만들기
```console
$ conda create --name kasto python=3.12.4

# activate
$ conda activate kasto

# deactivate
$ conda deactivate
```

# Window에 Poetry 설치 - 파워셀(사용자모드)
 ## python 설치 후 설치 가능
 ```console
 $ (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

 # 파워셀 닫고 다시 연다.
 ```
  ## poetry 설치 확인
 ```console
 $  poetry --version
 ```
 ## 위와 같이 했는데 안되면 다음과 같이 조치
* path에 poetry 경로 추가
*  poetry 경로 확인
```console
$ Get-ChildItem -Path $env:APPDATA\Python\Scripts\ | Where-Object { $_.Name -like "poetry*" }
```
### 예) "C:\Users\{사용자}shpark\AppData\Roaming\Python\Scripts" 를 추가
## 파워셀 또는 명령창 열어서 다음과 같이 입력 해서 확인
```console
  $  poetry --version
```

# Flet 설치
```console
$ conda activate kasto
$ pip install flet

# 패키징을 위한 Tool설치

$ pip install pyinstaller
```
* Desktop 패키징 : https://flet.dev/docs/cookbook/packaging-desktop-app/

# Desktop 패키징 방법 2번째
* winodws powershell(관리자) 에서 `start ms-settings:developers` 를 실행하여 `개발자 모드`를 on 한다.
* `flet build windows`

# 기타
## VSCode에서 spell check 비활성화
 1) VS Code를 열고 좌측 하단의 톱니바퀴 아이콘을 클릭하여 설정(Settings)을 엽니다.
 2) 검색 창에 "spell" 을 입력합니다.
 3) "Editor: Check Spelling" 옵션을 찾아 체크를 해제합니다.
