from django.contrib.auth.mixins import UserPassesTestMixin


class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().author == self.request.user
