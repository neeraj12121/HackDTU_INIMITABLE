from PIL import Image
from sklearn import cross_validation
from sklearn import metrics
from sklearn import grid_search
from sklearn import svm
from io import BytesIO
import sys
import os

from django.db import models

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Input(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    sex = models.CharField(max_length=10, choices=[("Female", "Female"), ("Male", "Male")], blank=False)
    age = models.CharField(max_length=3, blank=False)
    image = models.FileField()
    contact_me = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")], default=1, blank=False)
    contact_number = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    comments = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.full_name

    def filename(self):
        return os.path.basename(self.image.name)


class Doctor(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    college = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=False)
    latfield = models.DecimalField(max_digits=20, decimal_places=15, default=None)
    longfield = models.DecimalField(max_digits=20, decimal_places=15, default=None)
    contact_number = models.CharField(max_length=50, blank=True)
    tags = models.CharField(max_length=50, blank=False)

    def __unicode__(self):
        return self.full_name


class ImageProcessor(models.Model):
    def process_directory(self, directory):

        training = []
        for root, _, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                img_feature = self.process_image_file(file_path)
                if img_feature:
                    training.append(img_feature)
        return training

    def process_image_file(self, image_path):

        image_fp = BytesIO(open(image_path, 'rb').read())
        try:
            image = Image.open(image_fp)
            return self.process_image(image)
        except IOError:
            return None

    def process_image(self, image, blocks=4):

        if not image.mode == 'RGB':
            return None
        feature = [0] * blocks * blocks * blocks
        pixel_count = 0
        for pixel in image.getdata():
            ridx = int(pixel[0] / (256 / blocks))
            gidx = int(pixel[1] / (256 / blocks))
            bidx = int(pixel[2] / (256 / blocks))
            idx = ridx + gidx * blocks + bidx * blocks * blocks
            feature[idx] += 1
            pixel_count += 1
        return [x / pixel_count for x in feature]

    def show_usage(self):

        print("Usage: %s [class A images directory] [class B images directory]" %
              sys.argv[0])
        sys.exit(1)

    def train(self, training_paths, print_metrics=True):

        training = []
        for i in training_paths:
            a = os.path.join(os.path.dirname(BASE_DIR), i)
            if not os.path.isdir(a):
                raise IOError('%s is not a directory' % a)
            training.append(self.process_directory(a))


        data = []
        for i in training:
            data = data + i

        # target is the list of target classes for each feature vector: a '1' for
        # class A and '0' for class B
        target = []
        for i in range(len(training_paths)):
            target = target + [i] * len(training[i])
        # split training data in a train set and a test set. The test set will
        # containt 20% of the total
        x_train, x_test, y_train, y_test = cross_validation.train_test_split(data, target, test_size=0.20)
        # define the parameter search space
        parameters = {'kernel': ['linear', 'rbf'], 'C': [1, 10, 100, 1000], 'gamma': [0.01, 0.001, 0.0001]}
        # search for the best classifier within the search space and return it
        clf = grid_search.GridSearchCV(svm.SVC(), parameters).fit(x_train, y_train)
        classifier = clf.best_estimator_
        if print_metrics:
            print()
            print('Parameters:', clf.best_params_)
            print()
            print('Best classifier score')
            print(metrics.classification_report(y_test,
            classifier.predict(x_test)))

        return classifier


    def __init__(self):
        self.training_paths = ["measles", "pimples", "chickenpox", "rashes", "warts"]
        print('Training classifier...')

        self.classifier = self.train(self.training_paths)

    def classify(self, filename):
        features = self.process_image_file(filename)
        a = self.classifier.predict(features)
        a = str(self.classifier.predict(features))
        a = a.replace('[', "")
        a = a.replace(']', "")
        a = int(a)
        return self.training_paths[a]
