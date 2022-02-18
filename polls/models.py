from django.db import models


# Create your models here.
# Creating the table for the Question Table
class Question(models.Model):
    question_text = models.CharField(max_length=1000, verbose_name="Text")
    Publication_Date = models.DateField(verbose_name="Publication Date")

    def __str__(self):  # A method is called so that question_text can be displayed on the display
        return self.question_text


# Creating the table for the Choices Table
class Choice(models.Model):
    Choices_text = models.CharField(max_length=200, verbose_name="Choice Text")
    No_of_votes = models.IntegerField(verbose_name="No of votes")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.Choices_text

