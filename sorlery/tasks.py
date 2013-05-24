from celery import task
from sorl.thumbnail import default
from sorl.thumbnail.images import ImageFile


@task
def create_thumbnail(file_, geometry_string, options, name):
    thumbnail = ImageFile(name, default.storage)

    if not thumbnail.exists():
        source = ImageFile(file_)
        source_image = default.engine.get_image(source)
        size = default.engine.get_image_size(source_image)
        source.set_size(size)
        default.backend._create_thumbnail(source_image, geometry_string, options, thumbnail)

        # Need to update both the source and the thumbnail with correct sizing
        # @todo
