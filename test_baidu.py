import requests
import pytest
class TestBaidu():


    @pytest.mark.skip()
    def test_status_code(self):

        r=requests.get("https://www.baidu.com")

        code=r.status_code

        assert code == 2000

    @pytest.mark.ds
    def test_content(self):
        r = requests.get("https://www.baidu.com")

        code = r.content

        assert "a" in str(code)




