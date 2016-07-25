
import copy
import datetime
from SwaggerBaseConfig import config as base

class SwaggerGenerator:

    def __init__(self, **kw):
        self.project = kw['project']

    def generate(self):
        swagger = base.copy()
        swagger['basePath'] = self.project.base_path
        swagger['paths'] = self.render_paths()
        swagger['info'] = {
            'version' : datetime.datetime.now().isoformat(),
            'title'   : self.project.name
        }

        return swagger


    def render_paths(self):
        paths = {}
        functions = self.project.functions
        for func_name, func_def in functions.iteritems():
            if 'x-api-gateway' in func_def.keys():
                conf = func_def['x-api-gateway']
                if paths.has_key( conf['path']):
                    paths[conf['path']][conf['method']] = self.render_method(func_name=func_name, func_def=func_def)
                else:
                    paths[conf['path']] = {
                        conf['method']: self.render_method(func_name=func_name, func_def=func_def)
                    }

        return paths

    def render_method(self, func_name, func_def):
        func_name = self.project.name + '_' + func_name
        conf = copy.deepcopy(self.project.swagger_func_template)

        # set method
        conf['x-amazon-apigateway-integration']['httpMethod'] = 'post'

        # set lambda uri
        uri = conf['x-amazon-apigateway-integration']['uri'].replace('{{functionName}}', func_name)
        conf['x-amazon-apigateway-integration']['uri'] = uri
        conf['description'] = func_def['description']

        # set params
        if func_def['x-api-gateway'].has_key('parameters'):
            conf['parameters'] = func_def['x-api-gateway']['parameters']

        return conf
