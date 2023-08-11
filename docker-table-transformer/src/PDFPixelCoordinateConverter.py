from math import floor, ceil


def convert_pdf_coordinates_to_pixel(image, start_x, end_x, start_y, end_y, origin_x=0, origin_y=0, origin_type='pdf', conversion_ratio=2):
    """

    @param image: Bytes representation of an image
    @param start_x: x-Coordinate of left bottom corner of textbox with (0, 0) as left bottom corner of the image
    @param end_x: x-Coordinate of right upper corner of textbox with (0, 0) as left bottom corner of the image
    @param start_y: y-Coordinate of left bottom corner of textbox with (0, 0) as left bottom corner of the image
    @param end_y: y-Coordinate of right upper corner of textbox with (0, 0) as left bottom corner of the image
    @param origin_x: Top left (x, y) to perform coordinates conversion
    @param origin_y: Top left (x, y) to perform coordinates conversion
    @param origin_type: Either pdf or pixel, indicate which coordinate system origin is using
    @param conversion_ratio:
    @return: Adjusted coordinates based on numpy order ((0, 0) as left upper corner of the image in order to match
    the exact pixels)

        This function re-calculate the coordinates with below 2 steps
        1. Shift (0, 0) from left bottom corner to left upper corner to match the pixels ordering
        2. Enlarge coordinate by image conversion ratio to match the pixels location

    """
    width, height = image.size
    if origin_type == 'pdf':
        adjusted_start_x = (start_x - origin_x) * conversion_ratio
        adjusted_end_x = (end_x - origin_x) * conversion_ratio
        adjusted_start_y = height - ((end_y - origin_y) * conversion_ratio)
        adjusted_end_y = height - ((start_y - origin_y) * conversion_ratio)
    else:
        raise NotImplementedError('Only pdf origin type is allowed !')
    return floor(adjusted_start_x), ceil(adjusted_end_x), floor(adjusted_start_y), ceil(adjusted_end_y)


def convert_pixel_to_pdf_coordinates(image, start_x, end_x, start_y, end_y, pdf_origin_coordinates,
                                     border_size, conversion_ratio=2):
    """

    @param image: Bytes representation of an image
    @param start_x: x-Coordinate of left bottom corner of textbox with (0, 0) as left top corner of the image
    @param end_x: x-Coordinate of right upper corner of textbox with (0, 0) as left top corner of the image
    @param start_y: y-Coordinate of left bottom corner of textbox with (0, 0) as left top corner of the image
    @param end_y: y-Coordinate of right upper corner of textbox with (0, 0) as left top corner of the image
    @param pdf_origin_coordinates: Original bottom left (x, y) of pdf to perform coordinates conversion
    @param image_origin_coordinates: Top left (x, y) of converted image to perform coordinates conversion
    @param border_size: Pixels appended outside the image to facilitate the table struction recognition process
    @param conversion_ratio: 2 (as configured in PDFConverterServer)
    @return: Adjusted coordinates based on numpy order ((0, 0) as left bottom corner of the image in order to match
    the exact pixels)

        This function re-calculate the coordinates with below 2 steps
        1. Shift (0, 0) from left top corner to left bottom corner to match the pixels ordering
        2. Shrink coordinate by image conversion ratio to match the coordinates location

    """
    width, height = image.size
    adjusted_start_x = (start_x - border_size) / conversion_ratio + pdf_origin_coordinates[0]
    adjusted_end_x = (end_x - border_size) / conversion_ratio + pdf_origin_coordinates[0]
    adjusted_start_y = ((height - border_size*2) - (end_y - border_size)) / conversion_ratio + pdf_origin_coordinates[1]
    adjusted_end_y = ((height - border_size*2) - (start_y - border_size)) / conversion_ratio + pdf_origin_coordinates[1]
    return floor(adjusted_start_x), ceil(adjusted_end_x), floor(adjusted_start_y), ceil(adjusted_end_y)
