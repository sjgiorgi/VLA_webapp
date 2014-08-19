from __future__ import absolute_import
from django.contrib import admin
from tutor.models import *
from VLA.models import *
from student.models import *

class SynonymInline(admin.StackedInline):
    model = Synonym
    extra = 3

class NodeAdmin(admin.ModelAdmin):
    inlines = [SynonymInline]

class ObjectiveInline(admin.StackedInline):
    model = LabObjective
    extra = 3
    
class EquipmentInline(admin.StackedInline):
    model = LabEquipment
    extra = 3

class LabAdmin(admin.ModelAdmin):
    inlines = [ObjectiveInline, EquipmentInline]

class TheoryElementInline(admin.StackedInline):
    model = TheoryElement
    extra = 3

class TheoryAdmin(admin.ModelAdmin):
    inlines = [TheoryElementInline]
    
class SimulationElementInline(admin.StackedInline):
    model = SimulationElement
    extra = 3

class SimulationAdmin(admin.ModelAdmin):
    inlines = [SimulationElementInline]
    
class HardwareElementInline(admin.StackedInline):
    model = HardwareElement
    extra = 4

class HardwareAdmin(admin.ModelAdmin):
    inlines = [HardwareElementInline]

class TheoryTestQuestionInline(admin.StackedInline):
    model = TheoryTestQuestion
    extra = 4

class TheoryTestAdmin(admin.ModelAdmin):
    inlines = [TheoryTestQuestionInline]
    
class SimulationQuestionInline(admin.StackedInline):
    model = SimulationTestQuestion
    extra = 4

class SimulationTestAdmin(admin.ModelAdmin):
    inlines = [SimulationQuestionInline]
    
class LabQuestionInline(admin.StackedInline):
    model = LabTestQuestion
    extra = 4

class LabTestAdmin(admin.ModelAdmin):
    inlines = [LabQuestionInline]
    
class AnswerKeywordInline(admin.StackedInline):
    model = AnswerKeyword
    extra = 5

class AnswerWithQuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerKeywordInline]

admin.site.register(Course)
admin.site.register(Prereq)
admin.site.register(Laboratory, LabAdmin)
admin.site.register(LabObjective)
admin.site.register(LabEquipment)
admin.site.register(TheoryElement)
admin.site.register(Theory, TheoryAdmin)
admin.site.register(TheoryTest, TheoryTestAdmin)
admin.site.register(TheoryTestQuestion)
admin.site.register(SimulationTestQuestion)
admin.site.register(Simulation, SimulationAdmin)
admin.site.register(SimulationTest, SimulationTestAdmin)
admin.site.register(Hardware, HardwareAdmin)
admin.site.register(HardwareElement)
admin.site.register(Results)
admin.site.register(ResultsQuestions)
admin.site.register(LabTestQuestion)
admin.site.register(LabTest, LabTestAdmin)

admin.site.register(VocabDomain)
admin.site.register(VocabTopic)
admin.site.register(Node,NodeAdmin)
admin.site.register(Synonym)

admin.site.register(Rulebase)
admin.site.register(AnswerWithQuestion, AnswerWithQuestionAdmin)
admin.site.register(AnswerElement)
admin.site.register(AnswerKeyword)
admin.site.register(AnswerTopic)

admin.site.register(UserProfile)
admin.site.register(CoursePermission)
admin.site.register(LabProgress)
