from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import (
    InsuranceType, Carrier, CoverageLine, Question, 
    ApplicationTemplate, TemplateQuestionSnapshot, ApplicationSession
)
from .serializers import ApplicationSessionSerializer
from .permissions import IsAgentUser

@api_view(['GET'])
@permission_classes([IsAgentUser])
def get_carriers_by_coverage(request):
    """
    Get carriers organized by coverage lines for a specific insurance type.
    Query param: insurance_type_id
    """
    insurance_type_id = request.GET.get('insurance_type_id')
    
    if not insurance_type_id:
        return Response({'error': 'insurance_type_id is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        insurance_type = InsuranceType.objects.get(id=insurance_type_id)
    except InsuranceType.DoesNotExist:
        return Response({'error': 'Insurance type not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Get all coverage lines for this insurance type
    coverage_lines = CoverageLine.objects.filter(insurance_types=insurance_type).order_by('name')
    
    result = []
    for coverage in coverage_lines:
        # Get carriers that have questions for this coverage and insurance type
        carriers_for_coverage = Carrier.objects.filter(
            question__coverages=coverage,
            question__insurance_types=insurance_type,
            insurance_types=insurance_type
        ).distinct().order_by('name')
        
        result.append({
            'coverage': {
                'id': coverage.pk,
                'name': coverage.name,
                'abbreviation': coverage.abbreviation
            },
            'carriers': [
                {
                    'id': carrier.pk,
                    'name': carrier.name
                }
                for carrier in carriers_for_coverage
            ]
        })
    
    return Response({
        'insurance_type': {
            'id': insurance_type.pk,
            'key': insurance_type.key,
            'label': insurance_type.label
        },
        'coverage_lines': result
    })

@api_view(['POST'])
@permission_classes([IsAgentUser])
def create_application_session(request):
    """
    Create a new application session with selected carriers and coverages.
    This will automatically create an ApplicationTemplate and then the session.
    
    Expected payload:
    {
        "insurance_type_id": 1,
        "session_name": "Client ABC Application",
        "selections": [
            {
                "coverage_id": 1,
                "carrier_ids": [1, 2, 3]
            },
            {
                "coverage_id": 2, 
                "carrier_ids": [2, 4]
            }
        ]
    }
    """
    insurance_type_id = request.data.get('insurance_type_id')
    session_name = request.data.get('session_name', 'New Application')
    selections = request.data.get('selections', [])
    
    if not insurance_type_id or not selections:
        return Response({
            'error': 'insurance_type_id and selections are required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        insurance_type = InsuranceType.objects.get(id=insurance_type_id)
    except InsuranceType.DoesNotExist:
        return Response({'error': 'Insurance type not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Collect all unique carriers and coverages from selections
    all_carrier_ids = set()
    all_coverage_ids = set()
    
    for selection in selections:
        coverage_id = selection.get('coverage_id')
        carrier_ids = selection.get('carrier_ids', [])
        
        if coverage_id:
            all_coverage_ids.add(coverage_id)
        all_carrier_ids.update(carrier_ids)
    
    try:
        with transaction.atomic():
            # Create ApplicationTemplate
            template = ApplicationTemplate.objects.create(
                name=f"Template for {session_name}",
                agent=request.user,
                insurance_type=insurance_type
            )
            
            # Set carriers and coverages
            template.carriers.set(list(all_carrier_ids))
            template.coverages.set(list(all_coverage_ids))
            
            # Get relevant questions and create snapshots
            questions = Question.objects.filter(
                insurance_types=insurance_type,
                carriers__in=all_carrier_ids,
                coverages__in=all_coverage_ids
            ).distinct()
            
            for question in questions:
                TemplateQuestionSnapshot.objects.create(
                    template=template,
                    original_question=question,
                    question_text=question.text
                )
            
            # Create ApplicationSession
            session = ApplicationSession.objects.create(
                template=template,
                agent=request.user,
                name=session_name,
                status='pending'
            )
            
            serializer = ApplicationSessionSerializer(session)
            
            return Response({
                'session': serializer.data,
                'template_id': template.pk,
                'questions_count': questions.count(),
                'message': f'Application session created successfully with {questions.count()} questions'
            }, status=status.HTTP_201_CREATED)
            
    except Exception as e:
        return Response({
            'error': f'Failed to create application session: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAgentUser])
def preview_questions(request):
    """
    Preview questions that would be included for given selections.
    Query params: insurance_type_id, carrier_ids (comma-separated), coverage_ids (comma-separated)
    """
    insurance_type_id = request.GET.get('insurance_type_id')
    carrier_ids = request.GET.get('carrier_ids', '').split(',')
    coverage_ids = request.GET.get('coverage_ids', '').split(',')
    
    # Filter out empty strings and convert to integers
    carrier_ids = [int(id) for id in carrier_ids if id.strip()]
    coverage_ids = [int(id) for id in coverage_ids if id.strip()]
    
    if not insurance_type_id or not carrier_ids or not coverage_ids:
        return Response({
            'error': 'insurance_type_id, carrier_ids, and coverage_ids are required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        insurance_type = InsuranceType.objects.get(id=insurance_type_id)
        
        questions = Question.objects.filter(
            insurance_types=insurance_type,
            carriers__in=carrier_ids,
            coverages__in=coverage_ids
        ).distinct()
        
        return Response({
            'questions_count': questions.count(),
            'questions': [
                {
                    'id': q.pk,
                    'text': q.text,
                    'carriers': [c.name for c in q.carriers.all()],
                    'coverages': [
                        {'name': c.name, 'abbreviation': c.abbreviation}
                        for c in q.coverages.all()
                    ]
                }
                for q in questions
            ]
        })
        
    except InsuranceType.DoesNotExist:
        return Response({'error': 'Insurance type not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)