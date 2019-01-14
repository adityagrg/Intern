from flask import Flask, jsonify, request
import pandas as pd
from scipy.stats import rankdata
from azure.storage.blob import BlockBlobService

app = Flask('Hello World')

@app.route('/', methods=['GET'])
def test2():
    return jsonify(api_name=app.name)

@app.route('/', methods=['POST'])
def test():
    data = request.get_json()
    local_file_name = 'Test_Supplierdata.xlsx'
    container_name = 'interntest'
	#download file to local machine
    block_blob_service = BlockBlobService(account_name=data['account_name'],
                                          account_key=data['account_key'])
    full_path_to_file = 'sample.xlsx'
    print("\nDownloading blob to " + full_path_to_file)
    block_blob_service.get_blob_to_path(container_name, local_file_name, full_path_to_file)

	#rank the items and add to a new file with a new rank column
    df = pd.read_excel(full_path_to_file)
    ml = df.values.tolist()
    val = []
    items = []
    ranks = []
    for i in ml:
        if i[0] not in items:
            items.append(i[0])

    for j in items:
        for i in ml:
            if i[0] == j:
                val.append(i[2])
        ranks.extend(rankdata(val, method="dense"))
        val = []

    df["supplier_rank"] = ranks
    new_file ="Test Supplierdata_aditya.xlsx"
    df.to_excel(new_file)

	#upload the new file
    block_blob_service.create_blob_from_path(container_name, new_file, new_file)
    return jsonify({'message': 'It works!'})


if __name__ == '__main__':
    app.run(debug=True, port=8080)