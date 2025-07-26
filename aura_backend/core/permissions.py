#
# Aura Insurance Engine – Proprietary Software
#
# Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
#
# This software was developed solely by Jose Reyes – full-stack engineer and designer.
# Jacob Powers contributed as the licensed insurance agent for the project.
# It is a modern insurance submission platform built to streamline the intake
# and processing of insurance applications.
#
# This code is proprietary and confidential. Unauthorized use, reproduction,
# distribution, or modification is strictly prohibited.
#
# Project repository: https://github.com/reyesjl/aura-insurance-engine
# DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
#

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