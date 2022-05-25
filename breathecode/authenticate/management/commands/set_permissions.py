from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group

CONTENT_TYPE_PROPS = {
    'app_label': 'breathecode',
    'model': 'SortingHat',  # the team of django use models name in lower case, use upper case instead
}

# examples permissions autogenerated by django
# {'name': 'Can add cohort', 'codename': 'add_cohort'}
# {'name': 'Can change cohort', 'codename': 'change_cohort'}
# {'name': 'Can delete cohort', 'codename': 'delete_cohort'}
# {'name': 'Can view cohort', 'codename': 'view_cohort'}

PERMISSIONS = [
    {
        'name': 'Get my profile',
        'codename': 'get_my_profile',
    },
    {
        'name': 'Create my profile',
        'codename': 'create_my_profile',
    },
    {
        'name': 'Update my profile',
        'codename': 'update_my_profile',
    },
    {
        'name': 'Get my certificate',
        'codename': 'get_my_certificate',
    },
]

GROUPS = [
    {
        'name': 'Admin',
        'permissions': [x['codename'] for x in PERMISSIONS],
    },
    {
        'name': 'Default',
        'permissions': ['get_my_profile', 'create_my_profile', 'update_my_profile'],
    },
    {
        'name': 'Student',
        'permissions': ['get_my_certificate'],
    },
    {
        'name': 'Mentor',
        'permissions': ['get_my_certificate'],
    },
]


# this function is used to can mock the list of permissions
def get_permissions():
    # prevent edit the constant
    return PERMISSIONS.copy()


# this function is used to can mock the list of groups
def get_groups():
    # prevent edit the constant
    return GROUPS.copy()


class Command(BaseCommand):
    help = 'Create default system capabilities'

    def handle(self, *args, **options):
        content_type = ContentType.objects.filter(**CONTENT_TYPE_PROPS).first()
        if not content_type:
            content_type = ContentType(**CONTENT_TYPE_PROPS)
            content_type.save()

        # reset the permissions
        Permission.objects.filter(content_type=content_type).delete()

        permissions = get_permissions()
        groups = get_groups()

        permission_instances = {}
        for permission in permissions:
            # it can use a django permissions
            instance = Permission.objects.filter(codename=permission['codename']).first()

            # it can create their own permissions
            if not instance:
                instance = Permission(**permission, content_type=content_type)
                instance.save()

            permission_instances[permission['codename']] = instance

        for group in groups:
            instance = Group.objects.filter(name=group['name']).first()

            # reset permissions
            if instance:
                instance.permissions.clear()

            else:
                instance = Group(name=group['name'])
                instance.save()

            for permission in group['permissions']:
                instance.permissions.add(permission_instances[permission])
