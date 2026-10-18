import hashlib, json, tempfile, urllib.request
import netron, onnx
from onnx import helper, TensorProto
with tempfile.TemporaryDirectory(prefix='awesome-netron-') as path:
    model = helper.make_model(helper.make_graph([helper.make_node('Relu',['x'],['y'])], 'single_relu', [helper.make_tensor_value_info('x', TensorProto.FLOAT,[1,3])], [helper.make_tensor_value_info('y',TensorProto.FLOAT,[1,3])]), producer_name='awesome-curated-fixture', opset_imports=[helper.make_opsetid('',18)], ir_version=8)
    onnx.checker.check_model(model)
    filename = path+'/single-relu.onnx'
    onnx.save(model, filename)
    address = netron.start(filename, address=('127.0.0.1', 18080), browse=False)
    try:
        with urllib.request.urlopen('http://127.0.0.1:18080/', timeout=5) as response:
            html = response.read()
            status = response.status
        with urllib.request.urlopen('http://127.0.0.1:18080/data/single-relu.onnx', timeout=5) as response:
            served = response.read()
        original = open(filename,'rb').read()
        assert status == 200 and b'Netron' in html
        assert served == original
        print(json.dumps({'http':status,'modelSha256':hashlib.sha256(served).hexdigest(),'nodes':[node.op_type for node in model.graph.node],'shape':[1,3],'bytes':len(served)}))
    finally:
        netron.stop(address)
