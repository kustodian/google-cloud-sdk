"""Generated client library for appengine version v1beta4."""
# NOTE: This file is autogenerated and should not be edited by hand.
from googlecloudsdk.third_party.apitools.base.py import base_api
from googlecloudsdk.third_party.apis.appengine.v1beta4 import appengine_v1beta4_messages as messages


class AppengineV1beta4(base_api.BaseApiClient):
  """Generated client library for service appengine version v1beta4."""

  MESSAGES_MODULE = messages

  _PACKAGE = u'appengine'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1beta4'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'AppengineV1beta4'
  _URL_VERSION = u'v1beta4'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new appengine handle."""
    url = url or u'https://appengine.googleapis.com/'
    super(AppengineV1beta4, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.apps_modules_versions = self.AppsModulesVersionsService(self)
    self.apps_modules = self.AppsModulesService(self)
    self.apps_operations = self.AppsOperationsService(self)
    self.apps = self.AppsService(self)

  class AppsModulesVersionsService(base_api.BaseApiService):
    """Service class for the apps_modules_versions resource."""

    _NAME = u'apps_modules_versions'

    def __init__(self, client):
      super(AppengineV1beta4.AppsModulesVersionsService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'appengine.apps.modules.versions.create',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1beta4/{+name}/versions',
              request_field=u'version',
              request_type_name=u'AppengineAppsModulesVersionsCreateRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'appengine.apps.modules.versions.delete',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1beta4/{+name}',
              request_field='',
              request_type_name=u'AppengineAppsModulesVersionsDeleteRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'appengine.apps.modules.versions.get',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[u'view'],
              relative_path=u'v1beta4/{+name}',
              request_field='',
              request_type_name=u'AppengineAppsModulesVersionsGetRequest',
              response_type_name=u'Version',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'appengine.apps.modules.versions.list',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[u'pageSize', u'pageToken', u'view'],
              relative_path=u'v1beta4/{+name}/versions',
              request_field='',
              request_type_name=u'AppengineAppsModulesVersionsListRequest',
              response_type_name=u'ListVersionsResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Deploys new code and resource files to a version.

      Args:
        request: (AppengineAppsModulesVersionsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes an existing version.

      Args:
        request: (AppengineAppsModulesVersionsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets application deployment information.

      Args:
        request: (AppengineAppsModulesVersionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Version) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists the versions of a module.

      Args:
        request: (AppengineAppsModulesVersionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListVersionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class AppsModulesService(base_api.BaseApiService):
    """Service class for the apps_modules resource."""

    _NAME = u'apps_modules'

    def __init__(self, client):
      super(AppengineV1beta4.AppsModulesService, self).__init__(client)
      self._method_configs = {
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'appengine.apps.modules.delete',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1beta4/{+name}',
              request_field='',
              request_type_name=u'AppengineAppsModulesDeleteRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'appengine.apps.modules.get',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1beta4/{+name}',
              request_field='',
              request_type_name=u'AppengineAppsModulesGetRequest',
              response_type_name=u'Module',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'appengine.apps.modules.list',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[u'pageSize', u'pageToken'],
              relative_path=u'v1beta4/{+name}/modules',
              request_field='',
              request_type_name=u'AppengineAppsModulesListRequest',
              response_type_name=u'ListModulesResponse',
              supports_download=False,
          ),
          'Patch': base_api.ApiMethodInfo(
              http_method=u'PATCH',
              method_id=u'appengine.apps.modules.patch',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[u'mask', u'migrateTraffic'],
              relative_path=u'v1beta4/{+name}',
              request_field=u'module',
              request_type_name=u'AppengineAppsModulesPatchRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Deletes a module and all enclosed versions.

      Args:
        request: (AppengineAppsModulesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets the current configuration of the module.

      Args:
        request: (AppengineAppsModulesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Module) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists all the modules in the application.

      Args:
        request: (AppengineAppsModulesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListModulesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Patch(self, request, global_params=None):
      """Updates the configuration of the specified module.

      Args:
        request: (AppengineAppsModulesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

  class AppsOperationsService(base_api.BaseApiService):
    """Service class for the apps_operations resource."""

    _NAME = u'apps_operations'

    def __init__(self, client):
      super(AppengineV1beta4.AppsOperationsService, self).__init__(client)
      self._method_configs = {
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'appengine.apps.operations.get',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1beta4/{+name}',
              request_field='',
              request_type_name=u'AppengineAppsOperationsGetRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'appengine.apps.operations.list',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[u'filter', u'pageSize', u'pageToken'],
              relative_path=u'v1beta4/{+name}/operations',
              request_field='',
              request_type_name=u'AppengineAppsOperationsListRequest',
              response_type_name=u'ListOperationsResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (AppengineAppsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding below allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`.

      Args:
        request: (AppengineAppsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class AppsService(base_api.BaseApiService):
    """Service class for the apps resource."""

    _NAME = u'apps'

    def __init__(self, client):
      super(AppengineV1beta4.AppsService, self).__init__(client)
      self._method_configs = {
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'appengine.apps.get',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[u'ensureResourcesExist'],
              relative_path=u'v1beta4/{+name}',
              request_field='',
              request_type_name=u'AppengineAppsGetRequest',
              response_type_name=u'Application',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Gets information about an application.

      Args:
        request: (AppengineAppsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Application) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)
