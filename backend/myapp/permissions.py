from rest_framework import permissions

class IsCustomer(permissions.BasePermission):
    """
    Custom permission to only allow customers to access the view.
    """

    def has_permission(self, request, view):
        # Check if the user is a customer
        return request.user.user_type == 1  # Assuming 1 is the ID for 'customer' in your model

class IsSeller(permissions.BasePermission):
    """
    Custom permission to only allow sellers to access the view.
    """

    def has_permission(self, request, view):
        # Check if the user is a seller
        return request.user.user_type == 2  # Assuming 2 is the ID for 'seller' in your model
