from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3  # Provide enough fields for 3 choices


class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['question_text']})
    ,('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
  ]

  # Allow Choice objects to be edited on the Question admin page
  inlines = [ChoiceInline]

  # Display question_text, pub_date, and was_published_recently fields on the
  # change list page
  list_display = ('question_text', 'pub_date', 'was_published_recently')

  list_filter = ['pub_date']  # Filter by pub_date
  search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
