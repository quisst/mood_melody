from django import forms

class MoodForm(forms.Form):
    diary_entry = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '오늘 있었던 일을 적어보세요...'}), required=True)
    genre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '선호하는 장르 (예: Pop, Rock)'}), required=False)
    duration = forms.ChoiceField(choices=[('short', '짧음(~3분)'), ('medium', '보통(3분~5분)'), ('long', '김(5분~)')], required=False)
    year_range = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '예: 2000~2010'}), required=False)
    mood = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '듣고 싶은 분위기'}), required=True)