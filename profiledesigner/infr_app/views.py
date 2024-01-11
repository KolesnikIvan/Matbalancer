from django.http import HttpRequest, HttpResponse
from django.template import loader

from infr_app.models import FloodingObject, Pad, Prognose, SeparationObject, Well
from infr_app.consts import InfraObjKind

# Create your views here.

def index(request: HttpRequest):
    return HttpResponse('Hello world')

def list_dns(request: HttpRequest):
    # dns = str()
    # dns = 'Список площадочных объектов сбора и подготовки\n\n'
    # for ns in SeparationObject.objects.order_by('name'):
    #     dns += ','.join((str(ns.name), 
    #                      str(ns.liq_sep_pwr),
    #                      str(ns.oil_sep_pwr),
    #                      str(ns.wat_sep_pwr),
    #                      str(ns.liq_pmp_pwr),
    #                      str(ns.oil_pmp_pwr),
    #                      str(ns.wat_pmp_pwr),
    #                      )) + '\n\n'
    # return HttpResponse(dns, content_type="text/plain; charset=utf-8")
    #_____________________________________________________
    template = loader.get_template('infr_app\list.html')
    dnss = SeparationObject.objects.order_by('name')
    context={'obj':'dns', 'objs':dnss}
    return HttpResponse(template.render(context, request))

def list_kns(request: HttpRequest):
    # kns = str()
    # kns = 'Список площадочных объектов закачки воды\n\n'
    # for ns in FloodingObject.objects.order_by('name'):
    #     kns += ','.join((str(ns.name), 
    #                      str(ns.obj_type),
    #                      str(ns.wat_pmp_pwr),
    #                      str(ns.wat_src_dbt),
    #                      str(ns.field),
    #                      )) + '\n\n'
    # return HttpResponse(kns, content_type="text/plain; charset=utf-8")
    template = loader.get_template('infr_app\list.html')
    knss = FloodingObject.objects.order_by('name')
    # import pdb; pdb.set_trace()
    context = {'obj': 'kns', 'objs': knss}
    return HttpResponse(template.render(context, request))

def list_wells(request: HttpRequest):
    wells = Well.objects.order_by('name')
    template = loader.get_template('infr_app\list.html')
    context = {'obj': 'well', 'objs': wells}
    return HttpResponse(template.render(context, request))

def list_pads(request: HttpRequest):
    pads = Pad.objects.order_by('name')
    template = loader.get_template('infr_app\list.html')
    context = {'obj': 'pad', 'objs': pads}
    return HttpResponse(template.render(context, request))

def show_prognose(request: HttpRequest):
    prognose = Prognose.objects.all()
    template = loader.get_template('infr_app\list.html')
    context = {'obj': 'prognose', 'objs': prognose}
    return HttpResponse(template.render(context, request))

def main_menu(request: HttpRequest):
    template = loader.get_template('infr_app\list_kns.html')
    context = {}
    return HttpResponse(template.render(context, request))

def list_objects_nominal_parameters(
        obj: InfraObjKind | str,
        request: HttpRequest):
    match obj:
        case InfraObjKind.SEPARATION_OBJECT.value:
            obj = 'dns' # TODO: add sort by DO or by field
            objs = SeparationObject.objects.all()
        case InfraObjKind.FLOODING_OBJECT:
            obj = 'kns'
            objs = FloodingObject.objects.all()
        # case InfraObjKind.TRANSFORMER_SUBSTATION.value:
        #     obj = 'ps'
        #     objs = Tra.objects.all()
        case InfraObjKind.WELL_PAD.value:
            obj = 'pad'
            objs = Pad.objects.all()
        case InfraObjKind.WELL.value:
            obj = 'well'
            objs = Well.objects.all()
        case 'prognose':
            obj = 'prognose'
            objs = Prognose.objs.all()
        case _:
            return 'HttpException the url submitted does not exist'
    template = loader.get_template('infr_app\list.html')
    context = {'obj': obj, 'objs': objs}
    return HttpResponse(template.render(context, request))

# def list_objects_nominal_parameters(
#         request,
#         obj_):
#     # import pdb; pdb.set_trace()
#     match obj_:
#         case 'dns':
#             obj = 'dns'
#             objs = SeparationObject.objects.all()
#         case 'kns':
#             obj = 'kns'
#             objs = FloodingObject.objects.all()
#         # case InfraObjKind.TRANSFORMER_SUBSTATION.value:
#         #     obj = 'ps'
#         #     objs = Tra.objects.all()
#         case 'pad':
#             obj = 'pad'
#             objs = Pad.objects.all()
#         case 'well':
#             obj = 'well'
#             objs = Well.objects.all()
#     template = loader.get_template('infr_app\list.html')
#     context = {'obj': obj, 'objs': objs}
#     return HttpResponse(template.render(context, request))
#     # TODO: test this function
