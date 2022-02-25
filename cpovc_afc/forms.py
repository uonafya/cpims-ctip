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
domain_list = get_list('olmis_domain_id', 'Please Select')


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

    AFC_FM_Q1 = forms.MultipleChoiceField(
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

    qf1A2_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A2',
               'data-parsley-required': "false"}))

    qf1A3_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A3',
               'data-parsley-required': "false"}))

    qf1A4_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A4',
               'data-parsley-required': "false"}))

    qf1A5_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A5',
               'data-parsley-required': "false"}))

    qf1A6_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A6',
               'data-parsley-required': "false"}))

    qf1A7_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A7',
               'data-parsley-required': "false"}))

    qf1A8_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A8',
               'data-parsley-required': "false"}))

    qf1A10_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'has_disability',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A2_rdo_error"}))

    qf1A11_sdd = forms.ChoiceField(
        choices=disability_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'disability_type'}))

    qf1A12_sdd = forms.ChoiceField(
        choices=severity_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'disability_severity'}))

    qf1A13_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A13',
               'data-parsley-required': "false"}))

    qf1A14_sdd = forms.ChoiceField(
        choices=(),
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'qf1A14_sdd'}))

    qf1A15_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A15_rdo_error"}))

    qf1A16_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A17_txt = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control event_date',
               'data-parsley-required': "false"}))

    qf1A20_sdd = forms.ChoiceField(
        choices=(),
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf1A21_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A21A_sdd = forms.ChoiceField(
        choices=(),
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf1A22_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A22_rdo_error"}))

    qf1A23_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A23_rdo_error"}))

    qf1A24_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A24_rdo_error"}))

    qf1A25_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A25_rdo_error"}))

    qf1A25A_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A25B_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A26_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A26_rdo_error"}))

    qf1A27_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A27_rdo_error"}))

    qf1A27A_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A28_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A28_rdo_error"}))


class AFCForm1B(forms.Form):
    """AFC Form 1B."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf1B1B___txt = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    qf1B1A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B1A_rdo_error"}))

    qf1B1B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B2A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B2A_rdo_error"}))

    qf1B2B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B3A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B3A_rdo_error"}))

    qf1B3B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B4A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B4A_rdo_error"}))

    qf1B4B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B5A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B5A_rdo_error"}))

    qf1B5B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B6A_sdd = forms.ChoiceField(
        choices=immunization_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'immunization'}))

    qf1B6B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('If not fully, reason'),
               'class': 'form-control', 'rows': '2'}))

    qf1B7A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B7A_rdo_error"}))

    qf1B7B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B8_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    # School details

    qf1B9A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B9A_rdo_error"}))

    qf1B9B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('If yes, name'),
               'class': 'form-control', 'rows': '2'}))

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

    qf1B10_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B10_rdo_error"}))

    qf1B11_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B11_rdo_error"}))

    qf1B12_rdo = forms.ChoiceField(
        choices=(),
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B12_rdo_error"}))

    qf1B13_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Other details'),
               'class': 'form-control', 'rows': '2'}))

    # PSS

    qf1B14A_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B14B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B14C_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B15_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B16_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B17_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B18A_rdo = forms.ChoiceField(
        choices=(),
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B18A_rdo_error"}))

    qf1B18B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B19A_rdo = forms.ChoiceField(
        choices=(),
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B19A_rdo_error"}))

    qf1B19B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B20 = forms.MultipleChoiceField(
        choices=(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'data-parsley-required': 'true'}))

    qf1B21_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B22_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B23_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B24_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B25_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B26_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    # Child perspective
    qf1B27A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B27A_rdo_error"}))

    qf1B28A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B28A_rdo_error"}))

    qf1B28B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('If yes, explain'),
               'class': 'form-control', 'rows': '2'}))

    # Assessment conclusions

    qf1B30_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B31_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B32_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B33_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))


class AFCForm2A(forms.Form):
    """AFC Form 2A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf2A1_txt = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    qf2A2_sdd = forms.ChoiceField(
        choices=(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true"}))

    qf2A3_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf2A4_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf2A5_sdd = forms.ChoiceField(
        choices=(),
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf2A6_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf2A7_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf2A8_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf2A9_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf2A10_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf2A11_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf2A12_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf2A13_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf2A14_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A14_rdo_error"}))

    qf2A15_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A15_rdo_error"}))

    qf2A16A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A16A_rdo_error"}))

    qf2A16B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('If yes, who, and what type'),
               'class': 'form-control', 'rows': '2'}))

    qf2A17A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A17A_rdo_error"}))

    qf2A17B_txt = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'How many'}))

    qf2A18A = forms.MultipleChoiceField(
        choices=(('', 'Please Select'),),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'form-control'}))

    qf2A18B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Other, details'),
               'class': 'form-control', 'rows': '2'}))

    qf2A19A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A19A_rdo_error"}))

    qf2A19B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Explain'),
               'class': 'form-control', 'rows': '2'}))

    qf2A20 = forms.MultipleChoiceField(
        choices=(('', 'Please Select'),),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'form-control'}))

    qf2A21_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A21_rdo_error"}))

    qf2A22_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A22_rdo_error"}))

    qf2A23A_txt = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    qf2A23B_txt = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    qf2A23C_txt = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    qf2A23D_txt = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    qf2A25A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A25A_rdo_error"}))

    qf2A25B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _("If no, describe child's unmet needs"),
               'class': 'form-control', 'rows': '2'}))


class AFCForm4A(forms.Form):
    """AFC Form 4A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf4A1 = forms.ChoiceField(
        choices=domain_list,
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'qf4A1',
                   'data-parsley-required': "true"}))

    qf4A2 = forms.ChoiceField(
        choices=(),
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'qf4A2',
                   'data-parsley-required': "true"}))

    qf4A3 = forms.ChoiceField(
        choices=(),
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'qf4A3',
                   'data-parsley-required': "true"}))

    qf4A4 = forms.ChoiceField(
        choices=(),
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'qf4A4',
                   'data-parsley-required': "true"}))

    qf4A7_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf4A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf4A7_rdo_error"}))


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


class AFCForm10A(forms.Form):
    """AFC Form 10A."""

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


class AFCForm12A(forms.Form):
    """AFC Form 12A."""

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


class AFCForm14A(forms.Form):
    """AFC Form 14A."""

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
