# Copyright 2018 The Fuego Authors.
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
# ==============================================================================
"""

Test always and never policies

"""

import sys
from pathlib import Path

fuegoRoot = Path(__file__).parent.parent  # get the firecam directory
sys.path.insert(0, str(fuegoRoot / 'detection_policies'))  # add detection_policies directory to the path

import detect_never, detect_always


def testNever():
    neverPol = detect_never.DetectNever(None, None, None, None, None, None, None, None)
    result = neverPol.detect(None)
    assert not result['fireSegment']


def testAlways():
    alwaysPol = detect_always.DetectAlways(None, None, None, None, None, None, None, None)
    result = alwaysPol.detect(None)
    assert result['fireSegment']
    assert result['fireSegment']['score']