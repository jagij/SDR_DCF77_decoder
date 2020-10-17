from runlength_encoder import Rle

def test_Rle_with_4_elements():
	rle = Rle(lambda x, y: None)
	res = rle.handle([0,0,0,0,1,1])
	assert res == 4

def test_Rle_with_3_elements():
	rle = Rle(lambda x, y: None)
	res = rle.handle([0,0,0,1,1])
	assert res == 3

def test_rle_with_callback(mocker):
	stub = mocker.stub()
	rle=Rle(stub)
	rle.handle([0,0,0,1,1])
	stub.assert_called_once_with(3, 0)

def test_rle_empty(mocker):
	stub = mocker.stub()
	rle=Rle(stub)
	rle.handle([0,0,0])
	stub.assert_not_called()

def test_rle_first_element_differs(mocker):
	stub = mocker.stub()
	rle=Rle(stub)
	rle.handle([1,1,1])
	stub.assert_called_once_with(0, 0)

def test_rle_first_element_as_configured(mocker):
	stub = mocker.stub()
	rle=Rle(stub, 1)
	rle.handle([1,1,1])
	stub.assert_not_called()

def test_rle_multiple(mocker):
	stub = mocker.stub()
	rle=Rle(stub)
	rle.handle([0,0,1,1,1,0])
	assert stub.call_args_list == [mocker.call(2, 0), mocker.call(3, 1)]