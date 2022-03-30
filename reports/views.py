from django.http import HttpRequest, JsonResponse
from reports.models import UserReport


def get_unresolved_reports(request: HttpRequest) -> JsonResponse:
    """Returns a list of all reports which have the 'resolved' status set to False."""

    reports = UserReport.objects.filter(is_resolved=False).values()

    return JsonResponse(list(reports), safe=False)


def create_report(request: HttpRequest, text, email=None) -> JsonResponse:
    """Create a new UserReport with content text and an optional contact email."""

    report = UserReport()

    report.text = text
    report.user_email = email
    report.save()

    # It seems like `save()` doesn't return anything and can't raise exceptions, so we can always return success

    return JsonResponse({"success": True})


def resolve_report(request: HttpRequest, report_id) -> JsonResponse:
    """Set the UserReport with the given ID to 'resolved' if it exists."""

    try:
        report = UserReport.objects.get(id=report_id)
        report.is_resolved = True
        report.save()

        return JsonResponse({"success": True})
    except UserReport.DoesNotExist:
        return JsonResponse({"success": False})
