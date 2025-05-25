from django.http import JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def create_session(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        session = ApplicationSession.objects.create()
        session.carriers.set(Carrier.objects.filter(id__in=data['carriers']))
        session.coverages.set(CoverageLine.objects.filter(id__in=data['coverages']))
        session.save()
        return JsonResponse({'token': str(session.token)}, status=201)
    
def get_sessions(request):
    sessions = ApplicationSession.objects.all()
    return JsonResponse({
        'sessions': [{'token': str(s.token), 'status': s.status} for s in sessions]
    })

def fill_session(request, token):
    try:
        session = ApplicationSession.objects.get(token=token)
        carrier_ids = session.carriers.values_list('id', flat=True)
        coverage_ids = session.coverages.values_list('id', flat=True)
        
        # Questions matching selected carriers and coverages
        specific_questions = Question.objects.filter(
            carriers__id__in=carrier_ids,
            coverages__id__in=coverage_ids
        )

        # Questions with no carriers (global to all carriers)
        global_carrier_questions = Question.objects.filter(carriers__isnull=True)

        # Questions with no coverages (global to all coverages)
        global_coverage_questions = Question.objects.filter(coverages__isnull=True)

        # Combine all and remove duplicates
        questions = (specific_questions | global_carrier_questions | global_coverage_questions).distinct()

        return JsonResponse({
            'questions': [{'id': q.id, 'text': q.text} for q in questions]
        })

    except ApplicationSession.DoesNotExist:
        return JsonResponse({'error': 'Invalid token'}, status=404)

@csrf_exempt
def submit_form(request, token):
    try:
        session = ApplicationSession.objects.get(token=token)
        if session.status == 'complete':
            return JsonResponse({'error': 'Already submitted'}, status=400)
        data = json.loads(request.body)
        Submission.objects.create(session=session, answers=data['answers'])
        session.status = 'complete'
        session.save()
        return JsonResponse({'status': 'submitted'})
    except ApplicationSession.DoesNotExist:
        return JsonResponse({'error': 'Invalid token'}, status=404)

def get_status(request, token):
    try:
        session = ApplicationSession.objects.get(token=token)
        if session.status == 'complete':
            submission = Submission.objects.get(session=session)
            return JsonResponse({
                'status': 'complete',
                'answers': submission.answers
            })
        else:
            return JsonResponse({'status': session.status})
    except ApplicationSession.DoesNotExist:
        return JsonResponse({'error': 'Invalid token'}, status=404)
    
def get_carriers(request):
    carriers = Carrier.objects.all()
    return JsonResponse({
        'carriers': [{'id': c.id, 'name': c.name} for c in carriers]
    })

def get_coverages(request):
    coverages = CoverageLine.objects.all()
    return JsonResponse({
        'coverages': [{'id': c.id, 'name': c.name} for c in coverages]
    })

def get_questions(request):
    questions = Question.objects.all()
    return JsonResponse({
        'questions': [{'id': q.id, 'text': q.text} for q in questions]
    })

@csrf_exempt
@require_POST
def preview_questions(request):
    data = json.loads(request.body)
    carrier_ids = data.get('carriers', [])
    coverage_ids = data.get('coverages', [])

    specific_questions = Question.objects.filter(
        carriers__id__in=carrier_ids,
        coverages__id__in=coverage_ids
    )
    global_carrier_questions = Question.objects.filter(carriers__isnull=True)
    global_coverage_questions = Question.objects.filter(coverages__isnull=True)

    questions = (specific_questions | global_carrier_questions | global_coverage_questions).distinct()

    return JsonResponse({
        'questions': [{'id': q.id, 'text': q.text} for q in questions]
    })