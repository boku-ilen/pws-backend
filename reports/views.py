from django.http import HttpRequest, JsonResponse
from reports.models import UserReport


def get_unresolved_reports(request: HttpRequest) -> JsonResponse:
    """Returns a list of all reports which have the 'resolved' status set to False."""

    reports = UserReport.objects.filter(is_resolved=False).values()

    return JsonResponse(list(reports), safe=False)


def create_report(request: HttpRequest, text, email=None) -> JsonResponse:
    report = UserReport()

    report.text = text
    report.user_email = email
    report.save()

    # TODO: Can this fail?

    return JsonResponse({"success": True})


def resolve_report(request: HttpRequest, report_id) -> JsonResponse:
    report = UserReport.objects.get(id=report_id)
    report.is_resolved = True
    report.save()

    # TODO: Return error if there is no report with that ID

    return JsonResponse({"success": True})
