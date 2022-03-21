from flair.data import Sentence
from flair.models import SequenceTagger
import io
def import_model():
    Model = SequenceTagger.load('final-model.pt')
    return Model



def tag(Model,file):
      
        res=""
        
        
        byte_str = file.read()

# Convert to a "unicode" object
        text_obj = byte_str.decode('UTF-8')  # Or use the encoding you expect


# io.StringIO(text_obj) will get you to a StringIO object if that's what you need
        
       
        res=text_obj.replace('\n'," ")
        
        sentence = Sentence(res)
# predict tags and print
        Model.predict(sentence)

    
        mynames_dict = {"Name":[],"tag":[]}

        list={}
        list=sentence.to_dict(tag_type='ner')
        j=0
        for i in range(len(list)):
           if(j<2):
            mynames_dict["Name"].append(list['entities'][i]['text'] )
            mynames_dict["tag"].append(list['entities'][i]['labels'] )
            j=j+1
        return mynames_dict