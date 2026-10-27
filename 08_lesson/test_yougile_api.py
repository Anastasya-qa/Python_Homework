from YougileApi import YougileApi
import pytest

# Список необходимых переменных
api = YougileApi("https://ru.yougile.com")
created_project_id = None
update_project_id = None
fake_project_id = "vwsd98-7ff5-0000-pc12340000"


@pytest.mark.positive
def test_create_project_posetive():
    global created_project_id

    project_name = "New Project"
    resp = api.create_new_project(project_name)

    assert (resp.status_code) == 201

    created_project_id = resp.json()["id"]
    assert created_project_id is not None


@pytest.mark.negative
def test_create_project_negative():
    project_name = ""
    resp = api.create_new_project(project_name)
    assert (resp.status_code) == 400


@pytest.mark.positive
def test_update_project_positive():
    global update_project_id

    id = created_project_id
    new_title = "New title"
    resp = api.update_project(id, new_title)

    assert (resp.status_code) == 200

    update_project_id = resp.json()["id"]
    assert update_project_id is not None


@pytest.mark.negative
def test_update_project_negative():
    id = created_project_id
    new_title = ""
    resp = api.update_project(id, new_title)

    assert (resp.status_code) == 400


@pytest.mark.positive
def test_get_project_positive():
    id = update_project_id
    resp = api.get_project_id(id)

    assert (resp.status_code) == 200


@pytest.mark.negative
def test_get_project_negative():
    id = fake_project_id
    resp = api.get_project_id(id)

    assert (resp.status_code) == 404
