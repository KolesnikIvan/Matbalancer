from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import SeparationObjectCreateForm

from infr_app.models import FloodingObject, Pad, Prognose, SeparationObject, Well
from infr_app.consts import InfraObjKind

# Create your views here.

def index(request: HttpRequest):
    return HttpResponse('Hello world')

def main_menu(request: HttpRequest):
    template = loader.get_template('infr_app\list_kns.html')
    context = {}
    return HttpResponse(template.render(context, request))

def list_objects_nominal_parameters(
        request, #: HttpRequest,
        obj_,#: InfraObjKind | str,
        ):
    # import pdb; pdb.set_trace()
    match obj_:
        case 'dns': #InfraObjKind.SEPARATION_OBJECT.value: # 'dns':     
            obj = 'dns' # TODO: add sort by DO or by field
            objs = SeparationObject.objects.all()
        case 'kns': #InfraObjKind.FLOODING_OBJECT: # 'kns':     
            obj = 'kns'
            objs = FloodingObject.objects.all()
        # case InfraObjKind.TRANSFORMER_SUBSTATION.value:
        #     obj = 'ps'
        #     objs = Tra.objects.all()
        case 'pad': #InfraObjKind.WELL_PAD.value: # 'pad':     
            obj = 'pad'
            objs = Pad.objects.all()
        case 'well':    #InfraObjKind.WELL.value: # 'well':    #
            obj = 'well'
            objs = Well.objects.all()
        case 'prognose':
            obj = 'prognose'
            objs = Prognose.objects.all()
        case _:
            return HttpResponse(f'<h1>HttpException the url submitted does not exist; wrong {obj_}</h1>')
    template = loader.get_template('infr_app\list.html')
    context = {'obj': obj, 'objs': objs}
    return HttpResponse(template.render(context, request))

class SeparationObjectCreateView(CreateView):
    template_name = 'infr_app\create_sep_obj.html'
    form_class = SeparationObjectCreateForm
    success_url = '/dns/'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['SeparationObject'] = SeparationObject.objects.all()
    #     context['SeparationObject'] = SeparationObject()
