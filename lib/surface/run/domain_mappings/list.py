# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Surface for listing all domain mappings."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.run import commands
from googlecloudsdk.command_lib.run import connection_context
from googlecloudsdk.command_lib.run import flags
from googlecloudsdk.command_lib.run import pretty_print
from googlecloudsdk.command_lib.run import resource_args
from googlecloudsdk.command_lib.run import serverless_operations
from googlecloudsdk.command_lib.util.concepts import concept_parsers
from googlecloudsdk.command_lib.util.concepts import presentation_specs


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class List(commands.List):
  """Lists domain mappings."""

  detailed_help = {
      'DESCRIPTION':
          '{description}',
      'EXAMPLES':
          """\
          To list all Cloud Run domain mappings, run:

              $ {command}
          """,
  }

  @classmethod
  def CommonArgs(cls, parser):
    flags.AddRegionArgWithDefault(parser)
    namespace_presentation = presentation_specs.ResourcePresentationSpec(
        '--namespace',
        resource_args.GetNamespaceResourceSpec(),
        'Namespace to list domain mappings in.',
        required=True,
        prefixes=False)
    concept_parsers.ConceptParser([
        resource_args.CLUSTER_PRESENTATION,
        namespace_presentation]).AddToParser(parser)
    parser.display_info.AddFormat(
        """table(
        {ready_column},
        metadata.name:label=DOMAIN,
        route_name:label=SERVICE,
        region:label=REGION)""".format(ready_column=pretty_print.READY_COLUMN))
    parser.display_info.AddUriFunc(cls._GetResourceUri)

  @classmethod
  def Args(cls, parser):
    cls.CommonArgs(parser)
    flags.AddPlatformArg(parser)

  def Run(self, args):
    """List available domain mappings."""
    conn_context = connection_context.GetConnectionContext(args)
    namespace_ref = args.CONCEPTS.namespace.Parse()
    with serverless_operations.Connect(conn_context) as client:
      self.SetCompleteApiEndpoint(conn_context.endpoint)
      return commands.SortByName(client.ListDomainMappings(namespace_ref))


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class AlphaList(List):

  @classmethod
  def Args(cls, parser):
    cls.CommonArgs(parser)
    flags.AddAlphaPlatformArg(parser)
    flags.AddKubeconfigFlags(parser)

AlphaList.__doc__ = List.__doc__
