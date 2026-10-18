from check_result import check_result
import chromadb
from chromadb.config import Settings
client = chromadb.EphemeralClient(Settings(anonymized_telemetry=False))
collection = client.create_collection('awesome_fixture', embedding_function=None, metadata={'hnsw:space':'l2'})
collection.add(ids=['logs','payments','garden'], embeddings=[[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]], documents=['Application logs','Payment receipts','Garden notes'])
result = collection.query(query_embeddings=[[1.,0.,0.]], n_results=2)
assert result['ids'][0][0] == 'logs'
assert result['distances'][0][0] == 0.
check_result('chroma', {'count':collection.count(),'nearest':result['ids'][0][0],'distance':result['distances'][0][0]})
