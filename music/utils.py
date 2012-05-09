import settings, os
from django.template.defaultfilters import slugify

def get_file_upload_path(instance, filename):
    if settings.MUSIC_ENCODE_FILENAMES:
        # generate encoded path and filename
        pass

    ext = filename.split('.')[-1]
    original_filename = filename.replace('.'+ext, '')

    return os.path.join('files/', "%s.%s" % (slugify(original_filename), ext.lower())) 

def get_cover_upload_path(instance, filename):
    return ''