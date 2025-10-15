from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class ReviewPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page_Number'
    page_size_query_param = 'page_size'
    max_page_size = 2
    last_page_strings = ('last',"end",)

class ReviewLimitOffsetPagination(LimitOffsetPagination):
    #limit => page_size, Kati ota data euta page ma dekhaune
    #offset => kata bata dekhaune, suppose index 400 bata xa bhane offset le 401 bata data dekhauna thalxa
    default_limit = 1
    limit_query_param = 'size'
    offset_query_param = 'location'
    max_limit = 1

class ReviewCursorPagination(CursorPagination):
    page_size = 1
    ordering = 'created_at'
    cursor_query_param = 'record'


