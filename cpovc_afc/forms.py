from django import forms
from django.forms.widgets import RadioFieldRenderer
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from cpovc_main.functions import get_list
immunization_list = get_list('immunization_status_id', 'Please Select')

person_type_list = get_list('person_type_id', 'Please Select Type')
school_level_list = get_list('school_level_id', 'Please Select Level')
admission_list = get_list('school_type_id', 'Please Select one')
disability_list = get_list('disability_type_id', 'Please Select one')
severity_list = get_list('severity_level_id', 'Please Select one')
admission_type_list = get_list('admission_type_id', 'Please Select')
admission_reason_list = get_list('care_admission_reason_id')

YESNO_CHOICES = get_list('yesno_id')
care_option_list = get_list(
    'alternative_family_care_type_id', 'Please Select Care')


class RadioCustomRenderer(RadioFieldRenderer):
    """Custom radio button renderer class."""

    def render(self):
        """Renderer override method."""
        return mark_safe(u'%s' % u'\n'.join(

            [u'%s' % force_unicode(w) for w in self]))


class AltCareForm(forms.Form):
    """AFC form."""

    has_consent = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'has_consent',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#has_consent_error"}))

    care_option = forms.ChoiceField(
        choices=care_option_list,
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'care_option',
                   'data-parsley-required': "true"}))

    case_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Care initiation Date'),
               'class': 'form-control',
               'id': 'case_date',
               'data-parsley-required': "true"
               }))

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf1A1 = forms.MultipleChoiceField(
        choices=admission_reason_list,
        widget=forms.CheckboxSelectMultiple(
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#id_qf1A1"}))

    qf3A1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf3A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf3A1_rdo_error"}))

    qf3B1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf3B1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf3B1_rdo_error"}))


class AFCForm1A(forms.Form):
    """AFC Form 1A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf1A1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'has_bcert',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A1_rdo_error"}))

    qf1A2_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'has_disability',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A2_rdo_error"}))

    qf1A3_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'in_school',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A3_rdo_error"}))

    qf1A4_sdd = forms.ChoiceField(
        choices=immunization_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'immunization'}))

    qf1A5_sdd = forms.ChoiceField(
        choices=disability_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'disability_type'}))

    qf1A6_sdd = forms.ChoiceField(
        choices=severity_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'disability_severity'}))

    school_level = forms.ChoiceField(
        choices=school_level_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'school_level'}))

    school_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Start typing then select',
               'id': 'school_name'}))

    school = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'readonly': 'readonly',
               'id': 'school_id'}))

    admission_type = forms.ChoiceField(
        choices=admission_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'admission_type'}))

    school_class = forms.ChoiceField(
        choices=(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'school_class'}))


class AFCForm1B(forms.Form):
    """AFC Form 1B."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf1B1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf1B1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B1_rdo_error"}))


class AFCForm2A(forms.Form):
    """AFC Form 2A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf2A1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf2A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A1_rdo_error"}))


class AFCForm4A(forms.Form):
    """AFC Form 4A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf4A1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf4A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf4A1_rdo_error"}))


class AFCForm5A(forms.Form):
    """AFC Form 5A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf5A1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf5A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf5A1_rdo_error"}))


class AFCForm6A(forms.Form):
    """AFC Form 6A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf6A1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf6A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf6A1_rdo_error"}))


class AFCForm7A(forms.Form):
    """AFC Form 7A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf7A1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf7A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf7A1_rdo_error"}))


class AFCForm8A(forms.Form):
    """AFC Form 8A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf8A1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf8A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf8A1_rdo_error"}))


class AFCForm9A(forms.Form):
    """AFC Form 9A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf9A1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf9A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf9A1_rdo_error"}))

    qf9A2_txt = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control event_date',
               'id': 'qf9A2_txt',
               'data-parsley-required': "true"
               }))
