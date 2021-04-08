import pytest


test1=("","helloworld","ask","xxxxxxxx",401,"错误的accessToken")
test2=("eb13d528-667a-4111-9905-5df1c08f1b17","","ask","xxxxxxxx",400,"标题不能为空")
test3=("eb13d528-667a-4111-9905-5df1c08f1b17","ddddddddddddd","","xxxxxxxx",400,"必须选择一个版块")
test4=("eb13d528-667a-4111-9905-5df1c08f1b17","ddddddddddddd","ask","",400,"内容不可为空")

@pytest.mark.parametrize("token,title,tab,content,excpet_status_code,excpet_err_msg",[test1,test2,test3,test4])
def test_topics(token,title,tab,content,excpet_status_code,excpet_err_msg):
    r = tapi.create_topic(token,title,tab,content)
    print(r.json(),r.status_code)
    # 断言状态码
    assert r.status_code == excpet_status_code

    # 错误信息断言
    assert  r.json().get("error_msg") == excpet_err_msg