


import os
import json

RESOURCE_FOLDER = "./test_doc"


def extract_table(doc_json):
    table_list = [block for page in doc_json["doc"]["pages"] for block in page["blocks"] if block["blockType"] == "table"]
    qa_list = []
    for table in table_list:
        line1 = table["table"][0]
        if line1[0] != "现象":
            continue
        for line in table["table"][1:]:
            question, answer = line
            qa_list.append(create_qa(question, answer))
    return qa_list


def handler(event, header):
    parser_result = event["PARSER_RESULT"][0]
    qa_list = extract_table(parser_result)
    return {"prediction": qa_list}


def test_doc(doc_id):
    with open(os.path.join(RESOURCE_FOLDER, "{}.json".format(doc_id))) as f:
        parse_result = json.loads(f.read())
    return handler(parse_result, None)


def create_qa(question, answer, ans_pos_list=None):
    return {
        "answer": {
            "displayValue": None,
            "pos_list": ans_pos_list if ans_pos_list else [
                {
                    "cell_x": None,
                    "cell_y": None,
                    "end": None,
                    "segment_id": None,
                    "segment_type": None,
                    "start": None
                }
            ],
            "value": answer,
            "type": None
        },
        "question": question
    }


if __name__ == "__main__":
    qa_list = test_doc("故障2728")
    qa_list = [(t["question"], t["answer"]["value"]) for t in qa_list["prediction"]]
    assert len(qa_list) > 0
