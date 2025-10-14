from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class ReviewThrottle(UserRateThrottle):
    scope = "review_user"