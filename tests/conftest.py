import pytest


from application.app import create_app


@pytest.fixture
def app():
    # テスト時に使用するFlakアプリを作成
    app = create_app("testing")

    return app
