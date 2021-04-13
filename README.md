# Deploying-NLP-Spacy-model-using-Docker-and-Flask
Check out deployed python app using docker container and heroku server

https://docker-classroom-its.herokuapp.com/

Introduction:

Named Entity Recognition is the most important, or I would say, the starting step in Information Retrieval. Information Retrieval 
is the technique to extract important and useful information from unstructured raw text documents. Named Entity Recognition NER 
works by locating and identifying the named entities present in unstructured text into the standard categories such as person names, 
locations, organizations, time expressions, quantities, monetary values, percentage, codes etc. Spacy comes with an extremely fast 
statistical entity recognition system that assigns labels to contiguous spans of tokens.

Spacy Model:
Spacy provides an option to add arbitrary classes to entity recognition systems and update the model to even include the new examples
apart from already defined entities within the model. Spacy has the ‘ner’ pipeline component that identifies token spans fitting a 
predetermined set of named entities. These are available as the ‘ents’ property of a Doc object.
