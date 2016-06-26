from django.contrib import admin

from users.models import MemberUnit, Member, Unit, Award, MemberAward


class MemberUnitInline(admin.StackedInline):
    model = MemberUnit
    fields = ['member', 'unit', 'rank']
    extra = 1


class MemberAwardInline(admin.StackedInline):
    model = MemberAward
    fields = ['member', 'award', 'reason', 'date']
    extra = 1


class MemberAdmin(admin.ModelAdmin):
    fields = ['nick', 'real_name', 'status', 'rank', 'played', 'picture']
    inlines = [MemberUnitInline, MemberAwardInline]


class UnitAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'picture']
    inlines = [MemberUnitInline]


class AwardAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'award_type', 'level', 'picture']
    inlines = [MemberAwardInline]


admin.site.register(Member, MemberAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Award, AwardAdmin)
