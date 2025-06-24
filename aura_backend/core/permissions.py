from rest_framework import permissions
    
class IsAgentUser(permissions.BasePermission):
    """
    Custom permission to only allow agent members to access the view.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_agent
    
# Example permission functions:
# class IsAuthenticated(BasePermission):
#     """
#     Allows access only to authenticated users.
#     """

#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_authenticated)


# class IsAdminUser(BasePermission):
#     """
#     Allows access only to admin users.
#     """

#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_staff)