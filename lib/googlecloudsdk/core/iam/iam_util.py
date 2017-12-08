# Copyright 2015 Google Inc. All Rights Reserved.
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
"""General IAM utilities used by the Cloud SDK."""

from googlecloudsdk.core import exceptions
from googlecloudsdk.third_party.apitools.base.protorpclite.messages import DecodeError
from googlecloudsdk.third_party.apitools.base.py import encoding


def AddArgsForAddIamPolicyBinding(parser):
  """Adds the IAM policy binding arguments for role and members.

  Args:
    parser: An argparse.ArgumentParser-like object to which we add the argss.

  Raises:
    ArgumentError if one of the arguments is already defined in the parser.
  """
  parser.add_argument(
      '--role', required=True,
      help='Define the role of the member.')
  parser.add_argument(
      '--member', required=True,
      help='The member to add to the binding.')

def AddArgsForRemoveIamPolicyBinding(parser):
  """Adds the IAM policy binding arguments for role and members.

  Args:
    parser: An argparse.ArgumentParser-like object to which we add the argss.

  Raises:
    ArgumentError if one of the arguments is already defined in the parser.
  """
  parser.add_argument(
      '--role', required=True,
      help='The role to remove the member from.')
  parser.add_argument(
      '--member', required=True,
      help='The member to remove from the binding.')


def AddBindingToIamPolicy(messages, policy, args):
  """Given an IAM policy, add new bindings as specified by args.

  An IAM binding is a pair of role and member. Check if the arguments passed
  define both the role and member attribute, create a binding out of their
  values, and append it to the policy.

  Args:
    messages: ToolResults API message classes generated by apitools.
        Required to create new bindings of the proper type.
    policy: IAM policy to which we want to add the bindings.
    args: argparse.Namespace, An object that contains the values for the
        arguments of a Cloud SDK command, including the arguments added by
        AddArgsForAddIamPolicyBinding.
  """
  if not hasattr(args, 'role') or not hasattr(args, 'member'):
    return

  # First check all bindings to see if the member is already in a binding with
  # the same role.
  # A policy can have multiple bindings with the same role. This is why we need
  # to explicitly do this as a separate, first, step and check all bindings.
  for binding in policy.bindings:
    if binding.role == args.role:
      if args.member in binding.members:
        return  # Nothing to do. Member already has the role.

  # Second step: check to see if a binding already exists with the same role and
  # add the member to this binding. This is to not create new bindings with
  # the same role.
  for binding in policy.bindings:
    if binding.role == args.role:
      binding.members.append(args.member)
      return

  # Third step: no binding was found that has the same role. Create a new one.
  policy.bindings.append(messages.Binding(
      members=[args.member], role='{0}'.format(args.role)))


def RemoveBindingFromIamPolicy(policy, args):
  """Given an IAM policy, add remove bindings as specified by the args.

  An IAM binding is a pair of role and member. Check if the arguments passed
  define both the role and member attribute, search the policy for a binding
  that contains this role and member, and remove it from the policy.

  Args:
    policy: IAM policy from which we want to remove bindings.
    args: Arguments from the command line that contain possible values for
        keys added by AddArgsForAddIamPolicyBinding. This is what defines what
        bindings we remove.
  """
  if not hasattr(args, 'role') or not hasattr(args, 'member'):
    return

  # First, remove the member from any binding that has the given role.
  # A server policy can have duplicates.
  for binding in policy.bindings:
    if binding.role == args.role and args.member in binding.members:
      binding.members.remove(args.member)

  # Second, remove any empty bindings.
  policy.bindings[:] = [b for b in policy.bindings if b.members]


def ParseJsonPolicyFile(policy_file_path, policy_message_type):
  """Construct an IAM Policy protorpc.Message from a JSON formated file.

  Args:
    policy_file_path: Path to the JSON IAM policy file.
    policy_message_type: Policy message type to convert JSON to.
  Returns:
    a protorpc.Message of type policy_message_type filled in from the JSON
    policy file.
  Raises:
    BadFileException if the JSON file is malformed or does not exist.
  """
  try:
    with open(policy_file_path) as policy_file:
      policy_json = policy_file.read()
  except EnvironmentError:
    # EnvironmnetError is parent of IOError, OSError and WindowsError.
    # Raised when file does not exist or can't be opened/read.
    raise exceptions.Error(
        'Unable to read policy file {0}'.format(policy_file_path))

  try:
    policy = encoding.JsonToMessage(policy_message_type, policy_json)
  except (ValueError, DecodeError) as e:
    # ValueError is raised when JSON is badly formatted
    # DecodeError is raised when etag is badly formatted (not proper Base64)
    raise exceptions.Error(
        'Policy file {0} is not a properly formatted JSON policy file. {1}'
        .format(policy_file_path, str(e)))
  return policy

def GetDetailedHelpForSetIamPolicy(collection, example_id):
  """Returns a detailed_help for a set-iam-policy command

  Args:
    collection: Name of the command collection (ex: "project", "dataset")
    example_id: Collection identifier to display in a sample command
        (ex: "my-project", '1234')
  Returns:
    a dict with boilerplate help text for the set-iam-policy command
  """
  return {
      'brief': 'Set IAM policy for a {0}.'.format(collection),
      'DESCRIPTION': '{description}',
      'EXAMPLES': """\
          The following command will read an IAM policy defined in a JSON file
          'policy.json' and set it for a {0} with identifier '{1}'

            $ {{command}} {1} policy.json

          See https://cloud.google.com/iam/docs/managing-policies for details
          of the policy file format and contents.
          """.format(collection, example_id)
  }


def GetDetailedHelpForAddIamPolicyBinding(collection, example_id):
  """Returns a detailed_help for an add-iam-policy-binding command

  Args:
    collection: Name of the command collection (ex: "project", "dataset")
    example_id: Collection identifier to display in a sample command
        (ex: "my-project", '1234')
  Returns:
    a dict with boilerplate help text for the add-iam-policy-binding command
  """
  return {
      'brief': 'Add IAM policy binding for a {0}.'.format(collection),
      'DESCRIPTION': '{description}',
      'EXAMPLES': """\
          The following command will add an IAM policy binding for the role
          of 'roles/editor' for the user 'test-user@gmail.com' on a {0} with
          identifier '{1}'

            $ {{command}} {1} --member='user:test-user@gmail.com'
            --role='roles/editor'

          See https://cloud.google.com/iam/docs/managing-policies for details
          of policy role and member types.
          """.format(collection, example_id)
  }

def GetDetailedHelpForRemoveIamPolicyBinding(collection, example_id):
  """Returns a detailed_help for a remove-iam-policy-binding command

  Args:
    collection: Name of the command collection (ex: "project", "dataset")
    example_id: Collection identifier to display in a sample command
        (ex: "my-project", '1234')
  Returns:
    a dict with boilerplate help text for the remove-iam-policy-binding command
  """
  return {
      'brief': 'Remove IAM policy binding for a {0}.'.format(collection),
      'DESCRIPTION': '{description}',
      'EXAMPLES': """\
          The following command will remove a IAM policy binding for the role
          of 'roles/editor' for the user 'test-user@gmail.com' on {0} with
          identifier '{1}'

            $ {{command}} {1} --member='user:test-user@gmail.com'
            --role='roles/editor'

          See https://cloud.google.com/iam/docs/managing-policies for details
          of policy role and member types.
          """.format(collection, example_id)
  }
