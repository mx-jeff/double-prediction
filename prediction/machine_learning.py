from sklearn.metrics import confusion_matrix


class MachineLearning:

    def get_confusion(self, y_test, y_prediction_svc):
        # confusion input
        confusion_array = confusion_matrix(y_test, y_prediction_svc)
        print(confusion_array, end='\n\n')
        return confusion_array

    def get_accuracy(self, confusion_support_vector_classifier):
        # get accuracy
        numerator = confusion_support_vector_classifier[0][0] + confusion_support_vector_classifier[1][1]
        denominator = sum(confusion_support_vector_classifier[0]) + sum(confusion_support_vector_classifier[1])
        acc_svc = (numerator/denominator) * 100
        print("Accuracy : ",round(acc_svc,2),"%")