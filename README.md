#HackDTU_INIMITABLE

##Description

Medical image analysis is an area which has witnessed an increased use of machine learning in recent times. In this ,we try to provide an overview of applications of machine learning techniques to medical skin problems. Health informatics is a relatively new area which deals with mining large amounts of data to gain useful insights. Some of the common challenges in health informatics will be briefly touched upon and some of the efforts in related directions will be outlined.
          Machine Learning (ML) aspires to provide computational methods for accumulating, updating and changing knowledge in the intelligent systems and particular learning mechanisms that assist to induce knowledge from the data. It is useful in cases where direct algorithmic solutions are unavailable, there is lack of formal models, or the knowledge about the application domain is inadequately defined.

##PROBLEM STATEMENT:
Most of the time we encounter certain allergies or rashes on our skin and 90% of times end up ignoring them leading to severe consequences in near future.To Find solution to to these common problems we have designed a web app that will work by answering you with the approximate results of the symptoms our skin disease by uploading the image of the affected area.

##TECHNOLOGIES USED:
Machine learning
Image Processing 
sklearn
PIL
Django-bootstrap(UI)

##IMPLEMENTATION
1)Creating Models for both Doctors and Users,Filling in their basic details and locations to create database.

2) Takes PIL image object and returned feature vectors.
3) Creating Views which takes the input form and required uploaded image  and than it classify and returns particular symptom.
4)Then it shows the location of the specialist doctors by integrating with Google maps(the names of various doctors were provided in the database).
