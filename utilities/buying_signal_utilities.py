import regex
import emoji
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

class buying_signal_utilities():

    ########################################### Initialise Required Classes ###############################################
    lemmatizer = WordNetLemmatizer()
    #################### buying signals keywords ###########

    def signals_keywords(self):
        try:
            signals_keyword_list = {
                'user experience': ['AI', 'Artifical Intelligence'],
                'Natural Language processing': ['understand', 'business', 'customer', 'listen', 'brand', 'purchase',
                                                'unsatisfied',
                                                'angry', 'help', 'buy', 'goodbye', 'ruin', 'arrives', 'business',
                                                'information',
                                                'highlight', 'transform', 'healthcare sector', 'investments', 'necessary',
                                                'use',
                                                'tackle'],
                'conversational ai': ['connected', 'accelerate', 'link', 'automating', 'translates', 'connected', 'solve',
                                      'efficiency', 'strategic', 'use'],
                'artificial solutions': ['customer support', 'financial', 'strategic', 'flexible', 'machine learning',
                                         'adapt',
                                         'services', 'products', 'neural', 'help', 'interact', 'innovation', 'use',
                                         'tackle'],
                'machine learning': ['media', 'coding', 'evolving', 'support', 'vital', 'use', 'capabilities', 'improves'],
                'natural Language': ['opportunities', 'training', 'provider', 'impact', 'reshape', 'dynamic', 'high value',
                                     'significiant', 'technology', 'human'],
                'improves': ['efficiency', 'sales', 'business', 'productivity', 'economy', 'revenues', 'management'],
                'social media': ['drive', 'engagement', 'audience', 'sharing', 'promotions', 'presence', 'information'],
                'relevant': ['information', 'sharing', 'audience', 'engagement', 'promotions', 'press' 'release',
                             'social media',
                             'sponspored'],
                'create': ['content', 'information', 'audience', 'engagement', 'presence', 'b2b', 'b2c', 'advertisement'],
                'brand': ['creation', 'identity', 'building', 'sponspored'],
                'marketing': ['demand', 'generation', 'demand generation', 'customer retention,' 'advertisement', 'online'],
                'product lead growth': ['startups', 'create' 'oppurtunity', 'create', 'oppurtunity', 'user aquisition',
                                        'aquisition', 'lead', 'sales', 'market', 'goal', 'customer onbaording experience',
                                        'hightouch cusomer experience', 'successful', 'leverage', 'seamless',
                                        'scalability'],
                'Customer Enablement': ['drives', 'drives product lead growth'],
                'product': ['marketting', 'market', 'social media', 'business', 'customer value']
            }
        except Exception as e:
            return print(e)
        return signals_keyword_list

###############################################  Cleaning the comments and primary keywords #######################################

    def cleaning_text(self,comment,source="youtube"):
        comment = str(comment)
        comment = comment.lower()
        sent = emoji.demojize(comment)
        sent = regex.sub(r"<[^<]+?>", "", comment)  # remove html tags
        sent = regex.sub("&quot;", "'", sent)  # replace &quot; with the single quotes
        sent = regex.sub(r"www\S+", "", sent)  # removing any links starting with www from the sentence
        sent = regex.sub(r"http\S+", "", sent)  # http/https from the sentence
        sent = regex.sub(r"https\S+", "", sent)  # http/https from the sentence
        sent = regex.sub(r'[\W_]+', ' ', sent)  # remove anything which is not an alphanumeric
        sent = regex.sub(r"\s+", " ", sent)
        return sent

    def lemmatize_sentence(self, sentence):
        sentence = sentence.lower()
        sentence = sentence.split()
        sentence_lemma = [self.lemmatizer.lemmatize(word, pos=wordnet.VERB) for word in sentence]
        sentence_lemma = " ".join(sentence_lemma)
        return sentence_lemma


    ###################### checking if buying signal ######################################################################

    def matches(self,raw_keyword, sentence):
        flag = False
        for keyword, verb_list in self.signals_keywords().items():
            keyword = self.cleaning_text(keyword)
            if regex.search(r'\b{}\b'.format(keyword), str(sentence)):
                sentence_copy = sentence
                sentence_lemma =self.lemmatize_sentence(sentence)
                for action in verb_list:
                    action = self.lemmatize_sentence(action)
                    if action in sentence_lemma:
                        flag = True
                        print(keyword , action)
                        return raw_keyword.lower(), sentence_copy

        if flag == False:
            return "no signal", "no signal"


    ############## remove dublicated data  #########################################################################

    def remove_duplicates(self,dataframe,column_name,keep='first',inplace=False):
            if inplace:
                try:
                    dataframe = dataframe.drop_duplicates(column_name,keep=keep)
                except Exception as e:
                    return print(e)
                return dataframe
            else:
                try:
                    dataframe_new = dataframe.drop_duplicates(column_name,keep=keep)
                except Exception as e:
                    return print(e)
                return dataframe_new

