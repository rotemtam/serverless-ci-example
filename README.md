## How to continuously deploy a serverless app (WIP)

__Blog post coming soon!__

Using:
- AWS API Gateway
- AWS Lambda
- Apex
- Swagger

### To run unit tests

```bash
mocha 'src/**/**.spec.js'
```

### To deploy functions to AWS Lambda

```bash
cd src && apex deploy
```

### To build a swagger file and deploy to API Gateway

```bash
python infra/api-gateway-deployer/src/__init__.py src/project.json
```
