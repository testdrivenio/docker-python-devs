# Docker for Python Developers

http://mherman.org/presentations/dockercon-2018

## Alpine

### Before

#### Web Development

```sh
$ docker build -t web-alpine ./web/01_alpine

$ docker images | grep web-alpine

web-alpine    latest    d472ebd700e0    About a minute ago    702MB
```

#### Data Science

```sh
$ docker build -t ds-alpine ./data-science/01_alpine

$ docker images | grep ds-alpine

ds-alpine    latest     50cf4c199090    About a minute ago    929MB
```

### After

#### Web Development

```sh
$ docker build -f ./web/01_alpine/Dockerfile-alpine -t web-alpine ./web/01_alpine

$ docker images | grep web-alpine

web-alpine    latest    a2a2c0dbff74    About a minute ago    102MB
```

#### Data Science

```sh
$ docker build -f ./data-science/01_alpine/Dockerfile-alpine -t ds-alpine ./data-science/01_alpine

$ docker images | grep ds-alpine

ds-alpine    latest    c397ae021682    About a minute ago    634MB
```

## Multi-stage Builds

### Before

#### Web Development

```sh
$ docker build -t web-multi ./web/02_multi

$ docker images | grep web-multi

web-multi    latest    9827108c2f8c    About a minute ago    705MB
```

#### Data Science

```sh
$ docker build -t ds-multi ./data-science/02_multi

$ docker images | grep ds-multi

ds-multi    latest     50cf4c199090    About a minute ago    929MB
```

### After

#### Web Development

```sh
$ docker build -f ./web/02_multi/Dockerfile-multi -t web-multi ./web/02_multi

$ docker images | grep web-multi

web-multi    latest    fc6cb94f7a72    About a minute ago    103MB
```

#### Data Science

```sh
$ docker build -f ./data-science/02_multi/Dockerfile-multi -t ds-multi ./data-science/02_multi

$ docker images | grep ds-multi

ds-multi    latest    a437d9c9974c    About a minute ago    365MB
```

## Order

```sh
$ docker build -t web-order ./web/03_order
```

## User

#### Web Development

```sh
$ docker build -t web-user ./web/04_user
```

#### Data Science

```sh
$ docker build -t ds-user ./data-science/03_user
```

## Docker Compose

#### Web Development

Build images and spin up the containers:

```sh
$ docker-compose -f web/05_compose/docker-compose.yml up -d --build
```

Create the db table:

```sh
$ docker-compose -f web/05_compose/docker-compose.yml run web python manage.py recreate_db
```

Add a user:

```sh
$ docker-compose -f web/05_compose/docker-compose.yml run web python manage.py seed_db
```

Test:

1. http://localhost:5001/users
1. http://localhost:5001/users/ping

#### Data Science

Build images and spin up the containers:

```sh
$ docker-compose up -d --build
```

Get the token from the logs:

```sh
$ docker-compose logs -f
```

Test: http://localhost:8888
