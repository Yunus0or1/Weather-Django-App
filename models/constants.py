from django.conf import settings


class ServerEnum:
    # Response CONSTANTS
    RESPONSE_CONNECTION_ERROR = "CONNECTION_ERROR"
    RESPONSE_SUCCESS = "SUCCESS"
    RESPONSE_DATABASE_CONNECTION_ERROR = "DATABASE_CONNECTION_ERROR"
    RESPONSE_PASSWORD_MISMATCH = "PASSWORD_MISMATCH"
    RESPONSE_EMAIL_MISMATCH = "EMAIL_MISMATCH"
    RESPONSE_EMAIL_TAKEN = "EMAIL_TAKEN"
    RESPONSE_PHONE_TAKEN = "PHONE_TAKEN"
    RESPONSE_INVALID_JWT_TOKEN = "INVALID_JWT_TOKEN"
    RESPONSE_INVALID_GOOGLE_TOKEN = "INVALID_GOOGLE_TOKEN"
    RESPONSE_INVALID_PHONE_TOKEN = "INVALID_PHONE_TOKEN"
    RESPONSE_WAIT_CUSTOMER_TRIP_ERROR = "PLEASE WAIT FOR CUSTOMER TO END TRIP"
    RESPONSE_CUSTOMER_ALREADY_COMPLETED_TRIP = "YOUR CUSTOMER ALREADY COMPLETED THE TRIP. YOU CAN NOT CANCEL NOW"
    RESPONSE_UPLOAD_CAR_IMAGES = "PLEASE UPLOAD ALL THE CAR IMAGES"
    RESPONSE_BOOKING_CANCELLED_BEFORE = "THE BOOKING IS CANCELLED BY CUSTOMER BEFORE ACCEPTING"
    RESPONSE_NO_AIRPORT = "NO_AIRPORT"
    RESPONSE_VALET_HAS_BOOKING = "VALET HAS BOOKING"
    RESPONSE_DISCOUNT_INVALID = "CODE INVALID"
    RESPONSE_DISCOUNT_LIMIT_CROSS = "CODE ALREADY USED"
    RESPONSE_DISCOUNT_NOT_VALID_AIRPORT = "THIS PROMO IS NOT VALID FOR THIS AIRPORT"
    RESPONSE_DISCOUNT_VALID = "VALID PROMO CODE"
    RESPONSE_DISCOUNT_TAKEN = "DISCOUNT ALREADY TAKEN"



    # SignIn Type
    SIGNIN_GOOGLE = "GOOGLE"
    SIGNIN_PHONE = "PHONE"
    SIGNIN_EMAIL_PASS = "EMAIL_PASS"
    SIGNIN_APPLE = "APPLE"

    # User Type
    USER_SUPER_ADMIN = "SUPER_ADMIN"
    USER_ADMIN = "ADMIN"
    USER_CUSTOMER = "CUSTOMER"
    USER_VALET = "VALET"
    USER_GUEST = "GUEST"

    # App Type
    APP_SUPER_ADMIN = "SUPER_ADMIN"
    APP_ADMIN = "ADMIN"
    APP_GUEST = "GUEST"
    APP_CUSTOMER = "CUSTOMER"
    APP_VALET = "VALET"

    # Update Registration Type
    PROFILE_USER_DETAILS_UPDATE = "PROFILE_USER_DETAILS_UPDATE"
    PROFILE_VALET_REGISTRATION_UPDATE = "PROFILE_VALET_REGISTRATION_UPDATE"
    PROFILE_CUSTOMER_REGISTRATION_UPDATE = "PROFILE_CUSTOMER_REGISTRATION_UPDATE"
    PROFILE_VALET_NORMAL_UPDATE = "PROFILE_VALET_NORMAL_UPDATE"
    PROFILE_CUSTOMER_NORMAL_UPDATE = "PROFILE_CUSTOMER_NORMAL_UPDATE"

    # Customer Booking Priority. Default = Normal
    BOOKING_PRIORITY_HIGH = "HIGH"
    BOOKING_PRIORITY_MODERATE = "MODERATE"
    BOOKING_PRIORITY_NORMAL = "NORMAL"

    # ADMIN Authority on Valet
    ADMIN_AUTORITY_ON_VALET_ALLOWED = "ALLOWED";
    ADMIN_AUTORITY_ON_VALET_BLOCKED = "BLOCKED";
    ADMIN_AUTORITY_ON_VALET_PENALIZED = "PENALIZED";
    ADMIN_AUTORITY_ON_VALET_AIRPORT_STATUTS_ACTIVE = "AIRPORT_STATUTS_ACTIVE";
    ADMIN_AUTORITY_ON_VALET_AIRPORT_STATUTS_INACTIVE = "AIRPORT_STATUTS_INACTIVE";

    # Valet Status
    VALET_STATUS_ACTIVE = "ACTIVE"
    VALET_STATUS_INACTIVE = "INACTIVE"

    VALET_ACCOUNT_STATUS_ACTIVE = 1
    VALET_ACCOUNT_STATUS_INACTIVE = 0

    VALET_MATCHED = 1
    VALET_NOT_MATCHED = 0

    # BOOKING Cancellation
    BOOKING_CANCELLED_BY_SUPER_ADMIN = "SUPER_ADMIN"
    BOOKING_CANCELLED_BY_ADMIN = "ADMIN"
    BOOKING_CANCELLED_BY_CUSTOMER = "CUSTOMER"
    BOOKING_CANCELLED_BY_VALET = "VALET"
    BOOKING_CANCELLED_BY_SYSTEM = "SYSTEM"

    # Booking Status
    BOOKING_STATUS_COMPLETED = "COMPLETED"
    BOOKING_STATUS_ONGOING_TRIP = "ONGOING_TRIP"
    BOOKING_STATUS_CANCELLED = "CANCELLED"
    BOOKING_STATUS_NOT_STARTED = "NOT_STARTED"

    # Trip Status
    TRIP_STATUS_COMPLETED = "COMPLETED"
    TRIP_STATUS_ONGOING = "ONGOING"
    TRIP_STATUS_CANCELLED = "CANCELLED"

    # CAR Trip Status
    CAR_TRIP_STATUS_COMPLETED = "COMPLETED"
    CAR_TRIP_STATUS_ONGOING = "ONGOING"

    BLANK_LIST = []
    YES = "YES"
    NO = "NO"

    DATABASE_INSERT = "INSERT"
    DATABASE_UPDATE = "UPDATE"

    DISCOUNT_METHOD_TYPE_VOUCHER_CODE = "VOUCHER_CODE"
    DISCOUNT_METHOD_TYPE_VISA_CARD = "VISA_CARD"
    DISCOUNT_METHOD_TYPE_MASTER_CARD = "MASTER_CARD"
    DISCOUNT_METHOD_TYPE_AMERICAN_EXPRESS = "AMERICAN_EXPRESS"

    DISCOUNT_AMOUNT_RECEIVE_TYPE_INSTANT_AMOUNT = "INSTANT_AMOUNT"
    DISCOUNT_AMOUNT_RECEIVE_TYPE_PERCENTAGE = "PERCENTAGE"

    PAYMENT_STATUS_TO_VALET_UNPAID = "UNPAID"
    PAYMENT_STATUS_TO_VALET_PAID = "PAID"

    PAYMENT_SERVER_ADDRESS = settings.PAYMENT_SERVER_ADDRESS

    MASTER_ADMIN_EMAIL = "ezeecorporation@gmail.com"
    MASTER_ADMIN_PASS = "TMM@ezeeDrop#111"
