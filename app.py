from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

word_args = reqparse.RequestParser()
word_args.add_argument("word", type=str, help="Word is Required", required=True)

class WordToNumber(Resource):
    def post(self):
        arg = word_args.parse_args()

        def text2int(textnum, numword={}):
            if not numword:
                units = [
                    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                    "sixteen", "seventeen", "eighteen", "nineteen",
                ]

                tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

                scales = ["hundred", "thousand", "million", "billion", "trillion"]

                numword["and"] = (1,0)
                for idx, word in enumerate(units): numword[word] = (1, idx)
                for idx, word in enumerate(tens): numword[word] = (1, idx * 10)
                for idx, word in enumerate(scales): numword[word] = (10 ** (idx * 3 or 2), 0)

            current = result = 0
            for word in textnum.split():
                scale, increment = numword[word]
                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
            
            return result + current
        
        return {"integer": text2int(arg["word"])}

api.add_resource(WordToNumber, '/WordsToNumber')


if __name__ == "__main__":
    app.run(debug=True)