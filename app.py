from flask import Flask
from flask_restful import Api, Resource, reqparse
from text2digits import text2digits

app = Flask(__name__)
api = Api(app)

word_args = reqparse.RequestParser()
word_args.add_argument("word", type=str, help="Word is Required", required=True)




class WordToNumber(Resource):
    def post(self):

        def is_number(x):
            if type(x) == str:
                x = x.replace(',', '')
            try:
                float(x)
            except:
                return False
            return True

        arg = word_args.parse_args()

        # def text2int(textnum, numword={}):
            # units = [
            #     "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            #     "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            #     "sixteen", "seventeen", "eighteen", "nineteen",
            # ]

            # tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

            # scales = ["hundred", "thousand", "million", "billion", "trillion"]

            # ordinal_words = {'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}

            # ordinal_endings = [('ieth', 'y'), ('th', '')]

            # if not numword:
            #     numword["and"] = (1,0)
            #     for idx, word in enumerate(units): numword[word] = (1, idx)
            #     for idx, word in enumerate(tens): numword[word] = (1, idx * 10)
            #     for idx, word in enumerate(scales): numword[word] = (10 ** (idx * 3 or 2), 0)

            # textnum = textnum.replace('-', ' ')

            # current = result = 0
            # curstring = ''
            # onnumber = False
            # lastunit = False
            # lastscale = False

            # def is_numword(x):
            #     if is_number(x):
            #         return True
            #     if word in numword:
            #         return True
            #     return False

            # def from_numword(x):
            #     if is_number(x):
            #         scale = 0
            #         increment = int(x.replace(',', ''))
            #         return scale, increment
            #     return numword[x]

            

            # for word in textnum.split():
            #     if word in ordinal_words:
            #         scale, increment = (1, ordinal_words[word])
            #         current = current * scale + increment
            #         if scale > 100:
            #             result += current
            #             current = 0
            #         onnumber = True
            #         lastunit = False
            #         lastscale = False
            #     else:
            #         for ending, replacement in ordinal_endings:
            #             if word.endswith(ending):
            #                 word = "%s%s" % (word[:-len(ending)], replacement)

            #         if (not is_numword(word)) or (word == 'and' and not lastscale):
            #             if onnumber:
            #                 curstring += repr(result + current) + " "
            #             curstring += word + " "
            #             result = current = 0
            #             onnumber = False
            #             lastunit = False
            #             lastscale = False
            #         else:
            #             scale, increment = from_numword(word)
            #             onnumber = True

            #         if lastunit and (word not in scales):                                                                                                                                                                                                                                         
            #         # Assume this is part of a string of individual numbers to                                                                                                                                                                                                                
            #         # be flushed, such as a zipcode "one two three four five"                                                                                                                                                                                                                 
            #             curstring += repr(result + current)                                                                                                                                                                                                                                       
            #             result = current = 0

            #         if scale > 1:                                                                                                                                                                                                                                                                 
            #             current = max(1, current) 

            #         current = current * scale + increment                                                                                                                                                                                                                                         
            #         if scale > 100:                                                                                                                                                                                                                                                               
            #             result += current                                                                                                                                                                                                                                                         
            #             current = 0  

            #         lastscale = False                                                                                                                                                                                                              
            #         lastunit = False                                                                                                                                                
            #         if word in scales:                                                                                                                                                                                                             
            #             lastscale = True                                                                                                                                                                                                         
            #         elif word in units:                                                                                                                                                                                                             
            #             lastunit = True

            # if onnumber:
            #     curstring += repr(result + current)

            # return curstring

            #     scale, increment = numword[word]
            #     current = current * scale + increment
            #     if scale > 100:
            #         result += current
            #         current = 0
            
            # return result + current

        t2d = text2digits.Text2Digits()

        return {"integer": t2d.convert(arg["word"])}



api.add_resource(WordToNumber, '/WordsToNumber')


if __name__ == "__main__":
    app.run(debug=True)