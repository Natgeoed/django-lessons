from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse, Http404
from django.template import RequestContext
import json

from curricula.models import Activity, Lesson, Standard, IdeaCategory
from curricula.utils import activities_info


def activity_detail(request, slug, preview=False, template_name='curricula/activity_detail.html'):
    if preview:
        activity = get_object_or_404(Activity, slug=slug)
    else:
        activity = get_object_or_404(Activity, slug=slug, published=True)

    audience = None
    getvars = request.GET.copy()
    if 'ar_a' in getvars:
        audience = int(getvars['ar_a'])
    resourceitems = activity.resourceitem_set.all()
    # Sort alphabetically
    resourceitems = resourceitems.order_by('resource__resource_category_type')
    if audience:
        resourceitems = [resourceitem for resourceitem in resourceitems
            if audience in resourceitem.resource.appropriate_for_audience_type_pks]

    return render_to_response(template_name, {
        'activity': activity,
        'object': activity,
        'resourceitems': resourceitems,
        'credit_details': activity.get_credit_details(),
        'model_student_work': activity.model_student_work(audience),
        'pictures_of_practice': activity.pictures_of_practice(audience),
        'preview': preview,
    }, context_instance=RequestContext(request))


def activity_list(request, preview=False, template_name='curricula/activity_list.html'):
    if preview:
        activities = Activity.objects.all()
    else:
        activities = Activity.objects.filter(published=True)

    return render_to_response(template_name, {
        'activity_list': activities,
        'object_list': activities,
    }, context_instance=RequestContext(request))


def idea_category(request, slug, preview=False, template_name='curricula/idea_category.html'):
    if preview:
        category = get_object_or_404(IdeaCategory, slug=slug)
    else:
        category = get_object_or_404(IdeaCategory, slug=slug, published=True)

    audience = None
    getvars = request.GET.copy()
    if 'ar_a' in getvars:
        audience = int(getvars['ar_a'])

    credit_details = {}
    if category.credit:
        for detail in category.credit.credit_details.all():
            if detail.credit_category not in credit_details:
                credit_details[detail.credit_category] = []
            credit_details[detail.credit_category].append(detail.entity)

    return render_to_response(template_name, {
        'category': category,
        'object': category,
        'ideas': [ci for ci in category.ideas.all() if audience in ci.appropriate_for.get_set_bits()],
        'credit_details': credit_details,
        'preview': preview,
    }, context_instance=RequestContext(request))


def activity_info(request, ids):
    """
    Return a json serialized datastream of activity infomation based on the
    requested id combination.
    """
    result = json.dumps(activities_info(ids))
    return HttpResponse(result, mimetype="text/javascript")


def background_information(request, id):
    lesson = get_object_or_404(Lesson, id=id)

    context = {'background_information': lesson.get_background_information(), }
    return render_to_response('curricula/fragments/bg_info.html',
                              context,
                              context_instance=RequestContext(request))


def learning_objectives(request, id):
    lesson = get_object_or_404(Lesson, id=id)

    context = {'learning_objectives': lesson.get_learning_objectives(), }
    return render_to_response('curricula/fragments/objectives.html',
                              context,
                              context_instance=RequestContext(request))


def get_breakout_terms(request, id):
    '''
    AJAX response for TinyMCE for Glossification.
    '''
    activity = get_object_or_404(Activity, id=id)
    breakout_terms = activity.vocabulary.all()
    terms = [gt.word_lower for gt in breakout_terms]
    res = json.dumps(terms)
    return HttpResponse(res)


def standard_type_list(request):
    """
    Listing of standard types
    """
    from .settings import STD_TYPE_SLUG_MAP
    context = {'standard_types': STD_TYPE_SLUG_MAP}
    return render_to_response('curricula/standard_type_list.html',
                               context,
                               context_instance=RequestContext(request))


def standard_type_detail(request, standard_type):
    """
    Detail of a standard types
    """
    try:
        from .settings import STD_TYPE_SLUG_MAP
        context = {
            'objects': Standard.objects.filter(
                standard_type=STD_TYPE_SLUG_MAP[standard_type]['key']
            ),
            'standard_type': STD_TYPE_SLUG_MAP[standard_type]['name']
        }
        template = (
            "curricula/%s_detail.html" % standard_type,
            "curricula/standard_type_detail.html"
        )
        return render_to_response(template,
                                  context,
                                  context_instance=RequestContext(request))
    except KeyError:
        raise Http404
