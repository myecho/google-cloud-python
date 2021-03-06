# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Client library for Google Cloud Natural Language API."""


from pkg_resources import get_distribution
__version__ = get_distribution('google-cloud-language').version

from google.cloud.language.client import Client
from google.cloud.language.document import Document
from google.cloud.language.document import Encoding

__all__ = ['Client', 'Document', 'Encoding', '__version__']
