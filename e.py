
parser_res = {'a':[1,2,3,4],'b':[5,6,7,8],'c':'true'}

def handler(event):
    parser_result = event["c"][0:3]
    return parser_result

print(handler(parser_res))
