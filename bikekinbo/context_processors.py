from pages.models import Setting


def setting(request):
    try:
        setting = Setting.get_solo()
    except Setting.DoesNotExist:
        setting = None

    data = {
        "setting": setting,
    }

    return data
