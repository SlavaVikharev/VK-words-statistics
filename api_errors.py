class ApiError(Exception): pass
class UnknownApiError(ApiError): pass
class DisabledAppError(ApiError): pass
class UnknownMethodError(ApiError): pass
class IncorrectSignatureError(ApiError): pass
class AuthFailedError(ApiError): pass
class TooManyRequestsError(ApiError): pass
class PermissionDeniedError(ApiError): pass
class InvalidRequestError(ApiError): pass
class FloodControlError(ApiError): pass
class InternalServerError(ApiError): pass
class TestModeError(ApiError): pass
class CaptchaNeededError(ApiError): pass
class AccessDeniedError(ApiError): pass
class HTTPAuthError(ApiError): pass
class ValidationRequiredError(ApiError): pass
class PermissionDeniedForNonStandaloneError(ApiError): pass
class PermissionAllowedForStandaloneError(ApiError): pass
class DisabledMethodError(ApiError): pass
class ConfirmationRequiredError(ApiError): pass
class InvalidParameterError(ApiError): pass
class InvalidAppAPIIDError(ApiError): pass
class InvalidUserIdError(ApiError): pass
class InvalidTimestamp(ApiError): pass
class AccessToAlbumDeniedError(ApiError): pass
class AccessToAudioDeniedError(ApiError): pass
class AccessToGroupDeniedError(ApiError): pass
class AlbumIsFullError(ApiError): pass
class EnableVotesError(ApiError): pass
class NoAccessError(ApiError): pass
class SomeAddsError(ApiError): pass


ERR_CODES = {
    1: UnknownApiError,
    2: DisabledAppError,
    3: UnknownMethodError,
    4: IncorrectSignatureError,
    5: AuthFailedError,
    6: TooManyRequestsError,
    7: PermissionDeniedError,
    8: InvalidRequestError,
    9: FloodControlError,
    10: InternalServerError,
    11: TestModeError,
    14: CaptchaNeededError,
    15: AccessDeniedError,
    16: HTTPAuthError,
    17: ValidationRequiredError,
    20: PermissionDeniedForNonStandaloneError,
    21: PermissionAllowedForStandaloneError,
    23: DisabledMethodError,
    24: ConfirmationRequiredError,
    100: InvalidParameterError,
    101: InvalidAppAPIIDError,
    113: InvalidUserIdError,
    150: InvalidTimestamp,
    200: AccessToAlbumDeniedError,
    201: AccessToAudioDeniedError,
    203: AccessToGroupDeniedError,
    300: AlbumIsFullError,
    500: EnableVotesError,
    600: NoAccessError,
    603: SomeAddsError
}
