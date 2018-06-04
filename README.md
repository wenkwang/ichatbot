# Summary
This project is using Python to build a chatbot service with RESTful API protocol applied, 
which could chat with people by text. Moreover, in order to make this service more personalized and, 
more importantly, fun, a training portal will be provided for the users to train their chatbot to be more characteristic.

# Functionality
There are two main services provides, one is chat service, and the other is train service. 
And I classify the chat sentences into three types: greeting, question, and statement.
1. Chat service (\<root URL\>/chat):<br/>
    For the chat service, there are three main processes:
   1. Receive the chat text from RESTful API and classify the text into one of three types:
Greeting, Question, and Statement
   2. Parse out the text using TextBlob library, mainly use the Noun Phrases and Sentiment models.
   3. Generate the TextIdentity based on the text type and the analysis results,
and retrieve the chat response from the database using this TextIdentity and the send back to the client
2. Train service (\<root URL\>/train):<br/>
    For the train service, there are two sub-models, one is to train the chat response,
the other is to train the text classification.
   1. Chat Training Model<br/>
        There definitely will be cases that the IChatBot doesn’t know how to respond to the certain chat sentence,
but what I’d like to do is to provide this training model to help decrease the time it happens. 
Also and probably more importantly, I’d like to make this chatbot more personalized by the user and hence it could be more fun.<br/>
        So, in order to achieve this, I will store the chat text to which the IChatBot has no idea how to response
and when the user comes into the training mode, the user could response to these chat and hence teach the 
IChatBot in their own ways.
   2. Classification Training Model<br/>
        This model will use the classifiers model of Textblob library to train the service to be accurate
for the three of the chat text. This model may not be released to users since I don’t think users should care it.

# Future Work
This project focuses on the implementation of the server side service 
and there is no user interface provided in this work. In the future, a client application will be built 
for users to use with this service, I’d like to use the API of WeChat or Messenger to 
make the IChatBot available on those platforms. And I’d like to support the Chinese language in the next work, 
so other text analyzer libraries will be considered. such as the jieba and NLTK. 
Another future improvement could lie in the database structure. In this project, I am using a relational table structure, 
but I do think other structure could potentially improve the overall performance.

