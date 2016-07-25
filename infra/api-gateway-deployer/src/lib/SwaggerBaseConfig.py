config = {
  "swagger": "2.0",
  "info": {
    "version": "{{buildTimestamp}}",
    "title": "{{projectName}}"
  },
  "host": "config.atom-data.io",
  "basePath": "{{projectBase}}",
  "schemes": [
    "https"
  ],
  "paths": {},
  "securityDefinitions": {
    "api_key": {
      "type": "apiKey",
      "name": "x-api-key",
      "in": "header"
    }
  },
  "definitions": {
    "Empty": {
      "type": "object"
    }
  }
}
