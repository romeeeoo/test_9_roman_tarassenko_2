from django.urls import reverse


class SuccessUrlMixin:
    def get_success_url(self):
        self.next_url = self.request.GET.get('next')
        print("1", self.next_url)
        if not self.next_url:
            self.next_url = self.request.POST.get('next')
            print("2")
        if not self.next_url:
            self.next_url = reverse('index')
            print("3", self.next_url)
        return self.next_url