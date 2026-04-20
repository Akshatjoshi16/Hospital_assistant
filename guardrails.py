from detoxify import Detoxify

model=Detoxify('unbiased')

query="you are good"



def validate_input(query):
    try:
        result=model.predict(query)
        if result['toxicity']>0.5:
            raise ValueError("query contains toxic words")
        return True
    except Exception as e:
        return f"input error: {e}"
    



def validate_output(response,max_length=5):
    try:
        if len(response)>max_length:
            raise ValueError(f"generated response exceeds length limit")
        else :
           return response
    except Exception as e:
        return e
    



from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

analyzer=AnalyzerEngine()
anonymizer=AnonymizerEngine()

def pii(text):
    try:
        results=analyzer.analyze(text=text,language="en")
        anonymized_text=anonymizer.anonymize(text=text,analyzer_results=results)
        return anonymized_text.text
    except Exception as e:
        return f"error :{e}"