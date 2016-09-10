## How to continuously deploy a serverless app (WIP)

This repo comes along with a triology of blog posts about serverless ci/cd __"Serverless Applications: continuous delivery with AWS Lambda and API Gateway__:

- [Part 1: Unit tests](https://medium.com/@rotemtam/serverless-applications-continuous-delivery-with-aws-lambda-and-api-gateway-part-1-unit-tests-e517aa1cd09e#.pel2h58f2)
- [Part 2: Deploying Lambda](https://medium.com/@rotemtam/serverless-applications-continuous-delivery-with-aws-lambda-and-api-gateway-part-2-deploying-87e3a95236f8#.cpj7vj7eo)
- Part 3: Coming soon

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
