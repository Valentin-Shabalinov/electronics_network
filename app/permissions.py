from rest_framework import permissions


class IsActiveEmployee(permissions.BasePermission):
    """
    Предоставляет доступ только активным сотрудникам.
    """

    def has_permission(self, request, view):
        # Проверка, что пользователь аутентифицирован и является активным
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_active
        )
