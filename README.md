# Stock data refresher

개인 학습용으로 만든 툴입니다. 너무 많은 부하를 주지 않기 위해 일부러 충분한 딜레이가 있도록 제작했어요. 다른 용도로 쓸만큼 기능을 만들지도 않았지만, 학습용으로만 쓰시길 바래요.

주식 데이터 긁어옵니다.

## 설치

```bash
$ git clone https://github.com/JeongUkJae/stock-data-refresher
$ cd stock-data-refresher
$ pip install -e .
```

## 사용법

### 루프를 돌면서 가격 넣기

```bash
$ stock_data_refresher stock put_in_loop --uri {database_uri} --time {seconds. default=5s}
```

time 옵션은 안 넣어도 돼요. 기본 5초

### 가격 한번 넣기

```bash
$ stock_data_refresher stock put_in_loop --uri {database_uri}
```

### 처음에 종목 넣기

```bash
$ stock_data_refresher stock put_list --uri {database_uri}
```

### DB 만들기

```bash
$ stock_data_refresher db create --uri {database_uri}
```

### DB 리셋

```bash
$ stock_data_refresher db truncate --uri {database_uri}
```

### DB 없애기

```bash
$ stock_data_refresher db drop --uri {database_uri}
```

위 기능 전부에서 `--echo` 넣으면 db 로그 찍혀요.

### DB URI 작성법

예시: `mysql+pymysql://user:password@host:port/db_name?charset=utf8`

## 버그

**정확한 정보**랑 Issues 탭에 달아주세요.
