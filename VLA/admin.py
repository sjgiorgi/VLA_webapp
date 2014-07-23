from django.contrib import admin
from VLA.models import Course, Laboratory, Theory, TheoryElement, LabObjective, PretestQuestion
from VLA.models import Pretest, Prelab, PrelabElement, PrelabTest, PrelabTestQuestion, Hardware, HardwareElement, Results, ResultsQuestions, UserProfile
from VLA.models import VocabDomain, VocabTopic, Node, Synonym

class SynonymInline(admin.StackedInline):
    model = Synonym
    extra = 3

class NodeAdmin(admin.ModelAdmin):
    inlines = [SynonymInline]

class ObjectiveInline(admin.StackedInline):
    model = LabObjective
    extra = 3
    
class LabAdmin(admin.ModelAdmin):
    inlines = [ObjectiveInline]

class TheoryElementInline(admin.StackedInline):
    model = TheoryElement
    extra = 3

class TheoryAdmin(admin.ModelAdmin):
    inlines = [TheoryElementInline]
    
class PrelabElementInline(admin.StackedInline):
    model = PrelabElement
    extra = 3

class PrelabAdmin(admin.ModelAdmin):
    inlines = [PrelabElementInline]
    
class HardwareElementInline(admin.StackedInline):
    model = HardwareElement
    extra = 4

class HardwareAdmin(admin.ModelAdmin):
    inlines = [HardwareElementInline]

class PretestQuestionInline(admin.StackedInline):
    model = PretestQuestion
    extra = 4

class PretestAdmin(admin.ModelAdmin):
    inlines = [PretestQuestionInline]
    
class PrelabQuestionInline(admin.StackedInline):
    model = PrelabTestQuestion
    extra = 4

class PrelabTestAdmin(admin.ModelAdmin):
    inlines = [PrelabQuestionInline]

admin.site.register(Course)
admin.site.register(Laboratory, LabAdmin)
admin.site.register(LabObjective)
admin.site.register(TheoryElement)
admin.site.register(Theory, TheoryAdmin)
admin.site.register(Pretest, PretestAdmin)
admin.site.register(PretestQuestion)
admin.site.register(PrelabTestQuestion)
admin.site.register(Prelab, PrelabAdmin)
admin.site.register(PrelabTest, PrelabTestAdmin)
admin.site.register(Hardware, HardwareAdmin)
admin.site.register(HardwareElement)
admin.site.register(Results)
admin.site.register(ResultsQuestions)

admin.site.register(VocabDomain)
admin.site.register(VocabTopic)
admin.site.register(Node,NodeAdmin)
admin.site.register(Synonym)

admin.site.register(UserProfile)