"""Generated client library for logging version v2beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from googlecloudsdk.third_party.apitools.base.py import base_api
from googlecloudsdk.third_party.apis.logging.v2beta1 import logging_v2beta1_messages as messages


class LoggingV2beta1(base_api.BaseApiClient):
  """Generated client library for service logging version v2beta1."""

  MESSAGES_MODULE = messages

  _PACKAGE = u'logging'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-platform.read-only', u'https://www.googleapis.com/auth/logging.admin', u'https://www.googleapis.com/auth/logging.read', u'https://www.googleapis.com/auth/logging.write']
  _VERSION = u'v2beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'LoggingV2beta1'
  _URL_VERSION = u'v2beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new logging handle."""
    url = url or u'https://logging.googleapis.com/'
    super(LoggingV2beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.entries = self.EntriesService(self)
    self.monitoredResourceDescriptors = self.MonitoredResourceDescriptorsService(self)
    self.projects_logs = self.ProjectsLogsService(self)
    self.projects_metrics = self.ProjectsMetricsService(self)
    self.projects_sinks = self.ProjectsSinksService(self)
    self.projects = self.ProjectsService(self)

  class EntriesService(base_api.BaseApiService):
    """Service class for the entries resource."""

    _NAME = u'entries'

    def __init__(self, client):
      super(LoggingV2beta1.EntriesService, self).__init__(client)
      self._method_configs = {
          'List': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'logging.entries.list',
              ordered_params=[],
              path_params=[],
              query_params=[],
              relative_path=u'v2beta1/entries:list',
              request_field='<request>',
              request_type_name=u'ListLogEntriesRequest',
              response_type_name=u'ListLogEntriesResponse',
              supports_download=False,
          ),
          'Read': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'logging.entries.read',
              ordered_params=[],
              path_params=[],
              query_params=[],
              relative_path=u'v2beta1/entries:read',
              request_field='<request>',
              request_type_name=u'ReadLogEntriesRequest',
              response_type_name=u'ReadLogEntriesResponse',
              supports_download=False,
          ),
          'Write': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'logging.entries.write',
              ordered_params=[],
              path_params=[],
              query_params=[],
              relative_path=u'v2beta1/entries:write',
              request_field='<request>',
              request_type_name=u'WriteLogEntriesRequest',
              response_type_name=u'WriteLogEntriesResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists log entries.  Use this method to retrieve log entries from Cloud.
Logging.  For ways to export log entries, see
[Exporting Logs](/logging/docs/export).

      Args:
        request: (ListLogEntriesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLogEntriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Read(self, request, global_params=None):
      """Streaming read of log entries.  Similar to `List`, this method is intended.
for a large volume of log entries.

      Args:
        request: (ReadLogEntriesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ReadLogEntriesResponse) The response message.
      """
      config = self.GetMethodConfig('Read')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Write(self, request, global_params=None):
      """Writes log entries to Cloud Logging.
All log entries in Cloud Logging are written by this method.

      Args:
        request: (WriteLogEntriesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (WriteLogEntriesResponse) The response message.
      """
      config = self.GetMethodConfig('Write')
      return self._RunMethod(
          config, request, global_params=global_params)

  class MonitoredResourceDescriptorsService(base_api.BaseApiService):
    """Service class for the monitoredResourceDescriptors resource."""

    _NAME = u'monitoredResourceDescriptors'

    def __init__(self, client):
      super(LoggingV2beta1.MonitoredResourceDescriptorsService, self).__init__(client)
      self._method_configs = {
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.monitoredResourceDescriptors.list',
              ordered_params=[],
              path_params=[],
              query_params=[u'pageSize', u'pageToken'],
              relative_path=u'v2beta1/monitoredResourceDescriptors',
              request_field='',
              request_type_name=u'LoggingMonitoredResourceDescriptorsListRequest',
              response_type_name=u'ListMonitoredResourceDescriptorsResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists monitored resource descriptors that are used by Cloud Logging.

      Args:
        request: (LoggingMonitoredResourceDescriptorsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListMonitoredResourceDescriptorsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsLogsService(base_api.BaseApiService):
    """Service class for the projects_logs resource."""

    _NAME = u'projects_logs'

    def __init__(self, client):
      super(LoggingV2beta1.ProjectsLogsService, self).__init__(client)
      self._method_configs = {
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'logging.projects.logs.delete',
              ordered_params=[u'projectsId', u'logsId'],
              path_params=[u'logsId', u'projectsId'],
              query_params=[],
              relative_path=u'v2beta1/projects/{projectsId}/logs/{logsId}',
              request_field='',
              request_type_name=u'LoggingProjectsLogsDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Deletes a log and all its log entries.
The log will reappear if it receives new entries.

      Args:
        request: (LoggingProjectsLogsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsMetricsService(base_api.BaseApiService):
    """Service class for the projects_metrics resource."""

    _NAME = u'projects_metrics'

    def __init__(self, client):
      super(LoggingV2beta1.ProjectsMetricsService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'logging.projects.metrics.create',
              ordered_params=[u'projectsId'],
              path_params=[u'projectsId'],
              query_params=[],
              relative_path=u'v2beta1/projects/{projectsId}/metrics',
              request_field=u'logMetric',
              request_type_name=u'LoggingProjectsMetricsCreateRequest',
              response_type_name=u'LogMetric',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'logging.projects.metrics.delete',
              ordered_params=[u'projectsId', u'metricsId'],
              path_params=[u'metricsId', u'projectsId'],
              query_params=[],
              relative_path=u'v2beta1/projects/{projectsId}/metrics/{metricsId}',
              request_field='',
              request_type_name=u'LoggingProjectsMetricsDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.metrics.get',
              ordered_params=[u'projectsId', u'metricsId'],
              path_params=[u'metricsId', u'projectsId'],
              query_params=[],
              relative_path=u'v2beta1/projects/{projectsId}/metrics/{metricsId}',
              request_field='',
              request_type_name=u'LoggingProjectsMetricsGetRequest',
              response_type_name=u'LogMetric',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.metrics.list',
              ordered_params=[u'projectsId'],
              path_params=[u'projectsId'],
              query_params=[u'pageSize', u'pageToken'],
              relative_path=u'v2beta1/projects/{projectsId}/metrics',
              request_field='',
              request_type_name=u'LoggingProjectsMetricsListRequest',
              response_type_name=u'ListLogMetricsResponse',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'logging.projects.metrics.update',
              ordered_params=[u'projectsId', u'metricsId'],
              path_params=[u'metricsId', u'projectsId'],
              query_params=[],
              relative_path=u'v2beta1/projects/{projectsId}/metrics/{metricsId}',
              request_field=u'logMetric',
              request_type_name=u'LoggingProjectsMetricsUpdateRequest',
              response_type_name=u'LogMetric',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a logs-based metric.

      Args:
        request: (LoggingProjectsMetricsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogMetric) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes a logs-based metric.

      Args:
        request: (LoggingProjectsMetricsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets a logs-based metric.

      Args:
        request: (LoggingProjectsMetricsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogMetric) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists logs-based metrics.

      Args:
        request: (LoggingProjectsMetricsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLogMetricsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Creates or updates a logs-based metric.

      Args:
        request: (LoggingProjectsMetricsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogMetric) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsSinksService(base_api.BaseApiService):
    """Service class for the projects_sinks resource."""

    _NAME = u'projects_sinks'

    def __init__(self, client):
      super(LoggingV2beta1.ProjectsSinksService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'logging.projects.sinks.create',
              ordered_params=[u'projectsId'],
              path_params=[u'projectsId'],
              query_params=[],
              relative_path=u'v2beta1/projects/{projectsId}/sinks',
              request_field=u'logSink',
              request_type_name=u'LoggingProjectsSinksCreateRequest',
              response_type_name=u'LogSink',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'logging.projects.sinks.delete',
              ordered_params=[u'projectsId', u'sinksId'],
              path_params=[u'projectsId', u'sinksId'],
              query_params=[],
              relative_path=u'v2beta1/projects/{projectsId}/sinks/{sinksId}',
              request_field='',
              request_type_name=u'LoggingProjectsSinksDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.sinks.get',
              ordered_params=[u'projectsId', u'sinksId'],
              path_params=[u'projectsId', u'sinksId'],
              query_params=[],
              relative_path=u'v2beta1/projects/{projectsId}/sinks/{sinksId}',
              request_field='',
              request_type_name=u'LoggingProjectsSinksGetRequest',
              response_type_name=u'LogSink',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.sinks.list',
              ordered_params=[u'projectsId'],
              path_params=[u'projectsId'],
              query_params=[u'pageSize', u'pageToken'],
              relative_path=u'v2beta1/projects/{projectsId}/sinks',
              request_field='',
              request_type_name=u'LoggingProjectsSinksListRequest',
              response_type_name=u'ListSinksResponse',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'logging.projects.sinks.update',
              ordered_params=[u'projectsId', u'sinksId'],
              path_params=[u'projectsId', u'sinksId'],
              query_params=[],
              relative_path=u'v2beta1/projects/{projectsId}/sinks/{sinksId}',
              request_field=u'logSink',
              request_type_name=u'LoggingProjectsSinksUpdateRequest',
              response_type_name=u'LogSink',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a sink.

      Args:
        request: (LoggingProjectsSinksCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogSink) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes a sink.

      Args:
        request: (LoggingProjectsSinksDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets a sink.

      Args:
        request: (LoggingProjectsSinksGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogSink) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists sinks.

      Args:
        request: (LoggingProjectsSinksListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListSinksResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Creates or updates a sink.

      Args:
        request: (LoggingProjectsSinksUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogSink) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(LoggingV2beta1.ProjectsService, self).__init__(client)
      self._method_configs = {
          }

      self._upload_configs = {
          }
