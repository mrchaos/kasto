
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


