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
        </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

[//]: # (TODO: Usage,Roadmap, Contributing, License, Contact)

## About The Project

This example demonstrates the seamless integration of [FastAPI](https://fastapi.tiangolo.com/), a modern, high-performance web framework,
with [Pydantic 2.0](https://github.com/pydantic/pydantic), a robust and powerful data validation library.
The integration is further enhanced by the use of [SQLAlchemy ORM](https://www.sqlalchemy.org/), a popular and feature-rich Object-Relational Mapping tool,
and [PostGIS16](https://postgis.net/), a spatial database extender for PostgreSQL that enables efficient storage, indexing, and querying of geospatial data.

The entire stack is connected using the [psycopg](https://github.com/psycopg/psycopg) Database Client Library,
which provides a robust and efficient way to interact with PostgreSQL databases in Python,
leveraging the power of asyncio and event loops.

Notably, this example showcases the latest and greatest versions of SQLAlchemy and psycopg,
which are renowned for their robustness, power, and speed. The inclusion of FastAPI adds a modern, fast, and high-performance web framework to the mix
allowing for the rapid development of APIs with Python 3.8+.

FastAPI has received significant recognition in the industry, including a review on thoughtworks Technology Radar in April 2021,
where it was classified as a Trial technology, with comments praising its performance, ease of use,
and features such as API documentation using OpenAPI. Additionally, FastAPI was recognized in the Python Developers Survey 2022 Results,
conducted by the Python Software Foundation and JetBrains, where it was reported that 1 in 4 Python developers use FastAPI,
with a 4 percentage point increase from the previous year.



### Built With

[![FastAPI][fastapi.tiangolo.com]][fastapi-url]
[![Pydantic][pydantic.com]][pydantic-url]
[![SQLAlchemy][sqlalchemy.org]][sqlalchemy-url]
[![Uvicorn][uvicorn.org]][uvicorn-url]
[![pytest][pytest.org]][pytest-url]
[![psycopg][psycopg.org]][psycopg-url]
[![alembic][alembic.sqlalchemy.org]][alembic-url]
[![rich][rich.readthedocs.io]][rich-url]



<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Make will help you

To build , run and test and more ... use magic of make help to play with this project.

```shell
1. make docker-build
2. make docker-up
3. make docker-alembic-migrate
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

* [GeoAlchemy 2 provides extensions to SQLAlchemy for working with spatial databases.](https://geoalchemy-2.readthedocs.io/en/stable/)
* [PostGIS is a spatial database extender for PostgreSQL object-relational database.](https://postgis.net/)
* [geojson_pydantic provides a suite of Pydantic models matching the GeoJSON specification rfc7946. ](https://developmentseed.org/geojson-pydantic/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Change Log

- **[long time ago...]** it was a long time ago in galaxy far far away...
- **[2024-09-29]** unit tests added

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

[fastapi.tiangolo.com]: https://img.shields.io/badge/FastAPI-0.114.2-009485?style=for-the-badge&logo=fastapi&logoColor=white

[fastapi-url]: https://fastapi.tiangolo.com/

[pydantic.com]: https://img.shields.io/badge/Pydantic-2.9.2-e92063?style=for-the-badge&logo=pydantic&logoColor=white

[pydantic-url]: https://docs.pydantic.dev/latest/

[sqlalchemy.org]: https://img.shields.io/badge/SQLAlchemy-2.0.35-bb0000?color=bb0000&style=for-the-badge

[sqlalchemy-url]: https://docs.sqlalchemy.org/en/20/

[uvicorn.org]: https://img.shields.io/badge/Uvicorn-0.30.6-2094f3?style=for-the-badge&logo=uvicorn&logoColor=white

[uvicorn-url]: https://www.uvicorn.org/

[psycopg.org]: https://img.shields.io/badge/psycopg-3.2.2-2e6fce?style=for-the-badge&logo=postgresql&logoColor=white

[psycopg-url]: https://www.psycopg.org/psycopg3/docs/

[pytest.org]: https://img.shields.io/badge/pytest-8.3.3-fff?style=for-the-badge&logo=pytest&logoColor=white

[pytest-url]: https://docs.pytest.org/en/6.2.x/

[alembic.sqlalchemy.org]: https://img.shields.io/badge/alembic-1.13.1-6BA81E?style=for-the-badge&logo=alembic&logoColor=white

[alembic-url]: https://alembic.sqlalchemy.org/en/latest/

[rich.readthedocs.io]: https://img.shields.io/badge/rich-13.8.1-009485?style=for-the-badge&logo=rich&logoColor=white

[rich-url]: https://rich.readthedocs.io/en/latest/

