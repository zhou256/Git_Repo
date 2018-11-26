# -*- coding: utf-8 -*-
"""
We will write a spam filter based on a publicly available mail data set called ling-spam. The download address of the ling-spam dataset is as follows:

http://t.cn/RKQBl9c

Here we have extracted the same amount of spam and non-spam from ling-spam. The specific download address is as follows:

http://t.cn/RKQBkRu
"""
from bs4 import BeautifulSoup
import re
import nltk
import os 
import os
import numpy as np
from collections import Counter #����
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from  nltk.corpus import stopwords
def mail_text_preprocessing(mail,remove_stopwords):
    #����1��ȥ��html���
    raw_text=BeautifulSoup(mail,'html').get_text()
    #����2��ȥ������ĸ�ַ�
    letters=re.sub('[^a-zA-Z-]',' ',raw_text) #e-mail��������ʽ���ָ��,��Ҫ�Ľ���'-'�����ų�����.
    words=letters.lower().split() #��Ӣ�Ĵʻ�ת��ΪСд��ʽ
    #����3�����ͣ�ô�====���remove_stopwords������,���һ��ȥ�������е�ͣ�ô�
    if remove_stopwords:
        stop_words=set(stopwords.words('english'))
        #����4����ʼ��stemmerѰ�Ҹ����ʻ����ԭʼ�Ĵʸ�
        #stemmer=nltk.stem.PorterStemmer()
        #words=[stemmer.stem(w) for w in words if w not in stop_words]
        words=[w for w in words if w not in stop_words]
        #����5���������汣����'-'����������,ȥ�������Ķ�'-'���ݡ�
        result=[]
        for item in words:
            if item=='-':
                continue
            elif len(item)==1: 
                #����6�����˵�������ĸ��ʽ�Ĵʻ�
                continue
            else:
                result.append(item)
    return result
#����mail_to_text()����
content1="""Subject: re : ems best software best $ remove instruction below . remove request respectfully immediately cut edge e-mail technology : " express mail server " imc $ 275 limit ! best e-mail program , try . read message , prove work anywhere less download demo free our full service web site , complete step step instructional tutorial ! visit our web site : http : / / 138 . 27 . 44 . 5 . cearth . . ca / user / imc ( can't log site call us , sometime site overload hit ) try before buy ! love ! 's bulk e-mailer dream true , ! same software $ 695 . 0 ! $ 495 . 0 l . s . enterprise call : 808-876 - 1550 information order copy today $ 275 ( limit ) . fax order / info request : ( 808 ) 878-6869 ( include name , phone number , e-mail address ) visit our web site : http : / / 138 . 27 . 44 . 5 . cearth . . ca / user / imc ( can't log site call us , sometime site overload hit ) 60 million e-mail address excellent " remove list " service available $ 99 . accept major credit card : visa * master card * american express * discover card accept check fax ! simply fax check : 808-878 - 6869 n't hesitate , call today offer limit ! express mail server ? express mail server ( ems ) bulk e-mail software thing work . ems transform computer personal mail server . additional hardware , ems software complete control mailing , mail send originate computer deliver directly mailbox recipient . since mail originate computer , longer necessary internet service provider 's mail server . previous generation stealth cloak type program , work upload mail provider 's mail server . program send mail through provider mail server without authorization ( consider theft service ) . problem , previous generation stealth type program upload message faster mail server process . many cause provider 's mail server bog down crash . obviously , provider furious . furthermore , send hundred thousand message , unfortunately , most simply filter delete mail server . lucky 10 % - 20 % mail deliver . ems software computer emulate mail server actually control watch mail deliver piece piece . 100 % delivery rate program anywhere internet . 100 % delivery rate internet email address . bold claim true . latest technical advance bulk email since advent stealth type program . program verify domain validity email address before send mail . dramatically reduce bounce back undeliverable . bounce back undeliverable sure bog down server . control where want bounce back mail . email address want ems . ems work dial internet account , ( aol consider dial internet account ) isdn line t - 1 t - 3 . run window 95 nt . hear person lose dial account software . one reason bulk email frown upon numerous isp 's ( internet service provider ) try send much mail , quick crash mail server isp . win happen ems software since n't since n't mail server isp send mail . program actually send mail directly computer , , bona fide mail server , recipient mail server avoid potential block prevent reach those mail list . " forge " header randomize anything 100 % mail deliver , although program allow randomization customize header . send mail omit " " " " " reply " portion header . want send message color . problem ems . select font color mouse , click background color . want font bold put italic , point click . want message center shift leave right , once again point click . unlike , ( same , different name ) software straightforward easy . log aol , already computer 'd need ems . provide technical support phone answer question . ems work window 95 nt computer . require additional hardware software . ems software send speed 80 , 0 message per hour delivered modest pentium 28 . 8 modem . rate dramatically increase isdn cable modem course t - 1 even faster . want advantage breakthrough bulk email technology us call number below . n't plan repeat mailing product advantage opportunity . cost $ 275 . 0 ! money spend consider buy stealth ( many . . . operate same ) $ 400 . happy stealth n't mind frequent loss dial-up account , lot complaint . lot mail deliver due block crash mail server delete mail , along result low response rate mailing , defeat purpose e-mail first place ! few aware technology , already leap bound ahead competition . using , sell anything wish , over over . , consider decide offer mail service . ' ve probably e-mail claim send advertisement e-mail cost $ 200 per 100 , 0 . most n't realize 20 30 mail pay send actually deliver ! mail service profitable , software , advertise service millions free ! cd roms 60 million address help start . purchase , visit our web site : http : / / 138 . 27 . 44 . 5 . cearth . . ca / user / imc ( can't log site call us , sometime site overload hit ) call . m . c : phone : ( 808 ) 876-1550 fax : ( 808 ) 878-6869 place order today while supplies ' ll happy send demo copy answer question . call us our full service web site address remove our mail list add our " global remove list " simply : http : / / www . ctct . com remove request respectfully immediately
"""
zhou=mail_text_preprocessing(content1,True) 

#1.׼���ı�����
train_path='C:/Users/Administrator/Desktop/ling-spam/train-mails/'

#2.����ʵ�(�ʱ�)
def make_Dictionary(train_dir):
    
    emails=[os.path.join(train_dir,f) for f in os.listdir(train_dir)]
    all_words=[]
    for mail in emails:
        with open(mail) as m:
            for i,line in enumerate(m):
                if i==2: #body of email is only 3rd line of text file.
                    #words=line.split()
                    words=mail_text_preprocessing(line,True) #��������ĵ���ÿһ�н���NLP�������ֵ�����Ԥ����
                    all_words+=words
    dictionary=Counter(all_words) #��������,ֱ�Ӷ�һ�������еĸ������ʽ��м���
    #ɾ����һЩ�������ʼ����ж��޹صĵ��ַ�==��Щ�����������
    list_to_remove = list(dictionary.keys()) #��ҪתΪlist���洢,��Ȼԭʼ�Ĵ������������⡣
    #return list_to_remove
    jinlist=['com','edu','www','ffa','etc']
    jinli=[w for w in list_to_remove if len(w)==2]
    paichu=['us','he','ad','me','cd','id','ps','pi']
    jinlist+=jinli
    for i in range(len(paichu)):
        try:
            del jinlist[jinlist.index(paichu[i])]
        except:
            continue
    for item in list_to_remove:
        if item.isalpha() == False: #�����ַ���ɾ��,�����ֺ�������ž�ɾ��,ֻ����26����ĸ���ַ�����
            del dictionary[item] 
        elif len(item) == 1:        #�����ַ�ɾ��
            if item!='I':
                del dictionary[item]
            else:
                pass
        elif item in jinlist:
            del dictionary[item]
    dictionary = dictionary.most_common(3000)
    return dictionary,jinlist
#ͨ������ print dictionary ָ��Ϳ�������ʵ�==�ʵ���Ӧ�û���������Щ��Ƶ�ʣ�����������ѡȡ��Ƶ����ߵ� 3000 ���ʣ�
dictionary,jinlist=make_Dictionary(train_path)
#3.������ȡ
def extract_features(mail_dir):
    #mail_dir=train_path
    files=[os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]
    features_matrix=np.zeros((len(files),3000)) #�����ά�ȴ�Сʹ��()���롣
    docID=0
    for fil in files:
        with open(fil) as fi:
            for i,line in enumerate(fi):
                if i==2:
                    #words=line.split()
                    words=mail_text_preprocessing(line,True) #��������ĵ���ÿһ�н���NLP�������ֵ�����Ԥ����
                    for word in words:
                        wordID=0
                        for i,d in enumerate(dictionary):
                            if d[0]==word:
                                wordID=i
                                features_matrix[docID,wordID]=words.count(word)
        docID=docID+1
    return features_matrix
train_labels = np.zeros(702)
train_labels[351:701] = 1
train_matrix = extract_features(train_path)

#4.ѵ��ģ��Bayes��SVMģ��
#Training SVM and Naive bayes classifier and its variants

model1 = LinearSVC()
model2 = MultinomialNB()

model1.fit(train_matrix,train_labels)
model2.fit(train_matrix,train_labels)

# Test the unseen mails for Spam
#5.����ѵ���õ�ģ�Ͷ������ʼ��ķ���Ԥ�����
test_dir = 'C:/Users/Administrator/Desktop/ling-spam/test-mails/'
test_matrix = extract_features(test_dir)
test_labels = np.zeros(260)
test_labels[130:260] = 1

result1 = model1.predict(test_matrix)
result2 = model2.predict(test_matrix)

#6.����Ԥ��������
print(confusion_matrix(test_labels,result1))
print(confusion_matrix(test_labels,result2))     
