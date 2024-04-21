# fastapi-postgis
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

![fastapi-postgis](/static/map.jpg)

<a name="readme-top"></a>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#make-will-help-you">Make will help you</a></li>
        <li><a href="#how-to-feed-database">How to feed database</a></li>
        <li><a href="#rainbow-logs-with-rich">Rainbow logs with rich</a></li>
        <li><a href="#setup-user-auth">Setup user auth</a></li>
        <li><a href="#local-development-with-poetry">Local development with poetry</a></li>
        <li><a href="#import-xlsx-files-with-polars-and-calamine">Import xlsx files with polars and calamine</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

[//]: # (TODO: Usage,Roadmap, Contributing, License, Contact)

    




## About The Project

Example of [FastAPI](https://fastapi.tiangolo.com/) integration supported by almighty [Pydantic 2.0](https://github.com/pydantic/pydantic)
with [SQLAlchemy ORM](https://www.sqlalchemy.org/) and PostGIS16
connected via fastest Database Client Library for python/asyncio [asyncpg](https://github.com/MagicStack/asyncpg).

Beside of using latest and greatest version of [SQLAlchemy](https://www.sqlalchemy.org/) with it robustness, powerfulness and speed
of [asyncpg](https://github.com/MagicStack/asyncpg) there is [FastAPI](https://fastapi.tiangolo.com/) (modern, fast (high-performance), 
web framework for building APIs with Python 3.8+ based on standard Python type hints.) already reviewed
on [thoughtworks](https://www.thoughtworks.com/radar/languages-and-frameworks?blipid=202104087) and noted in 
Python Developers [Survey 2021 Results](https://lp.jetbrains.com/python-developers-survey-2021/#FrameworksLibraries)
as the fifth official annual Python Developers Survey, conducted as a collaborative effort between the Python Software Foundation and JetBrains.

### Built With
[![FastAPI][fastapi.tiangolo.com]][fastapi-url]
[![Pydantic][pydantic.com]][pydantic-url]
[![SQLAlchemy][sqlalchemy.org]][sqlalchemy-url]
[![Uvicorn][uvicorn.org]][uvicorn-url]
[![pytest][pytest.org]][pytest-url]
[![asyncpg][asyncpg.github.io]][asyncpg-url]
[![alembic][alembic.sqlalchemy.org]][alembic-url]
[![rich][rich.readthedocs.io]][rich-url]



<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Make will help you
To build , run and test and more ... use magic of make help to play with this project.
```shell
1. make docker-build
2. make docker-up
3. make docker-apply-db-migrations
4. make docker-feed-db
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Local development with poetry

```shell
pyenv install 3.12 && pyenv local 3.12
```
```shell
poetry install
```
Hope you enjoy it.

## Acknowledgments
Use this space to list resources you find helpful and would like to give credit to.
I've included a few of my favorites to kick things off!

* [Open Source Shakespeare Dataset](https://github.com/catherinedevlin/opensourceshakespeare)
* [SQL Code Generator](https://github.com/agronholm/sqlacodegen)
* [Passlib - password hashing library for Python](https://passlib.readthedocs.io/en/stable/)
* [Polars - fast DataFrame library for Rust and Python](https://docs.pola.rs/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Change Log
- **[long time ago...]** it was a long time ago in galaxy far far away...
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/grillazz/fastapi-postgis.svg?style=for-the-badge
[contributors-url]: https://github.com/grillazz/fastapi-postgis/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/grillazz/fastapi-postgis.svg?style=for-the-badge
[forks-url]: https://github.com/grillazz/fastapi-postgis/network/members
[stars-shield]: https://img.shields.io/github/stars/grillazz/fastapi-postgis.svg?style=for-the-badge
[stars-url]: https://github.com/grillazz/fastapi-postgis/stargazers
[issues-shield]: https://img.shields.io/github/issues/grillazz/fastapi-postgis.svg?style=for-the-badge
[issues-url]: https://github.com/grillazz/fastapi-postgis/issues
[license-shield]: https://img.shields.io/github/license/grillazz/fastapi-postgis.svg?style=for-the-badge
[license-url]: https://github.com/grillazz/fastapi-postgis/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/python-has-powers/

[fastapi.tiangolo.com]: https://img.shields.io/badge/FastAPI-0.110.0-009485?style=for-the-badge&logo=fastapi&logoColor=white
[fastapi-url]: https://fastapi.tiangolo.com/
[pydantic.com]: https://img.shields.io/badge/Pydantic-2.6.4-e92063?style=for-the-badge&logo=pydantic&logoColor=white
[pydantic-url]: https://docs.pydantic.dev/latest/
[sqlalchemy.org]: https://img.shields.io/badge/SQLAlchemy-2.0.28-bb0000?color=bb0000&style=for-the-badge
[sqlalchemy-url]: https://docs.sqlalchemy.org/en/20/
[uvicorn.org]: https://img.shields.io/badge/Uvicorn-0.29.0-2094f3?style=for-the-badge&logo=uvicorn&logoColor=white
[uvicorn-url]: https://www.uvicorn.org/
[asyncpg.github.io]: https://img.shields.io/badge/asyncpg-0.29.0-2e6fce?style=for-the-badge&logo=postgresql&logoColor=white
[asyncpg-url]: https://magicstack.github.io/asyncpg/current/
[pytest.org]: https://img.shields.io/badge/pytest-8.1.1-fff?style=for-the-badge&logo=pytest&logoColor=white
[pytest-url]: https://docs.pytest.org/en/6.2.x/
[alembic.sqlalchemy.org]: https://img.shields.io/badge/alembic-1.13.1-6BA81E?style=for-the-badge&logo=alembic&logoColor=white
[alembic-url]: https://alembic.sqlalchemy.org/en/latest/

[rich.readthedocs.io]: https://img.shields.io/badge/rich-13.7.1-009485?style=for-the-badge&logo=rich&logoColor=white
[rich-url]: https://rich.readthedocs.io/en/latest/
[redis.io]: https://img.shields.io/badge/redis-5.0.3-dc382d?style=for-the-badge&logo=redis&logoColor=white
[redis-url]: https://redis.io/
