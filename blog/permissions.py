from rest_framework import permissions

class CanAccessByRole(permissions.BasePermission):
    EDIT_METHODS = ('POST', 'PATCH', 'PUT', 'DELETE')
    def has_permission(self, request, view):
        # import pdb; pdb.set_trace()
        #if is guest or get content
        if request.user.is_anonymous() or request.method == 'GET':
            return True

        role = self.get_role(request.user)

        if role and role.name == 'admin':
            return True

        if role and role.name == 'editor':
            return True

        if role and role.name == 'blogger':
            return True

        return super().has_permission(request, view)

    @staticmethod
    def get_role(user):
        if user.role.count() > 0:
            return user.role.name
        else:
            return None