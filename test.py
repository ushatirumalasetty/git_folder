def myfunc():
    return 2
    
def test_mything(snapshot):
    return_value = myfunc()
    assert return_value==2
    snapshot.assert_match(return_value,'gpg_response')