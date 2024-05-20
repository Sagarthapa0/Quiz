from django.db import models
import uuid,random

# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract=True

class Category(BaseModel):
    Category_name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Category_name
    
class Question(BaseModel):
    category=models.ForeignKey(Category,related_name='category' ,on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    marks=models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question
    
    def get_answer(self):
        # sourcery skip: for-append-to-extend, inline-immediately-returned-variable, list-comprehension
        answer_obj=list(Answer.objects.filter(question=self))
        random.shuffle(answer_obj)
        data=[]
        for answer in answer_obj:
            data.append(
                {
                    "answer":answer.answer,
                    "is_correct":answer.is_correct,
                }
            )      
        return data

class Answer(BaseModel):
    question=models.ForeignKey(Question,related_name='question_answer', on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer
