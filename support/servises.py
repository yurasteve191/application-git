from django.core.exceptions import ObjectDoesNotExist
from .models import ShelvesRentedDates, CanvasRentedDates

def get_reserved_canvas(canvas_id):
    try:
        reserved_shelves = CanvasRentedDates.objects.filter(canvas_id=canvas_id)
        reserved_dates = [(r.date_from, r.date_to) for r in reserved_shelves]
        return reserved_dates
    except ObjectDoesNotExist:
        # Якщо полотна не знайдено в базі даних
        return []

def get_reserved_shelves(shelves_id):
    print(shelves_id)
    try:
        reserved_shelves = ShelvesRentedDates.objects.filter(shelves_id=shelves_id)
        reserved_dates = [(r.date_from, r.date_to) for r in reserved_shelves]
        return reserved_dates
    except ObjectDoesNotExist:
        # Якщо стелаж не знайдено в базі даних
        return []