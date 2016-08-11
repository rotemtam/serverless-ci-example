
import re, os
from json import loads

class ApexProject:

    def __init__(self, path):

        self.path = os.path.abspath(path)

        # get project conf
        with open(self.path) as f:
            self._raw = f.read()
            self._parsed = loads(self._raw)
            self.name = self._parsed['name']
            self.description = self._parsed['description']
            self.base_path  = self._parsed['x-api-gateway']['base_path']
            self.stage_name  = self._parsed['x-api-gateway']['stage_name']
            self.rest_api_id = self._parsed['x-api-gateway']['rest-api-id']
            self.swagger_func_template = self._parsed['x-api-gateway']['swagger-func-template']

        # get base dir
        find_dir = re.compile(r"^(.+)[/\\]([^/\\]+)$")
        check = find_dir.match(self.path)
        self.directory = check.group(1)

        # get function defs
        self.functions = self._load_functions()

    def __repr__(self):
        return u'<ApexProject({})>'.format(self.name)


    def _load_functions(self):
        defs = {}
        fullpath = lambda d: os.path.join(self.directory, 'functions', d, 'function.json')
        funcs = [d for d in os.listdir(self.directory + '/functions') if os.path.isfile(fullpath(d))]
        for func in funcs:
            with open(fullpath(func)) as f:
                json = loads(f.read())
                defs[func] = json
        return defs
