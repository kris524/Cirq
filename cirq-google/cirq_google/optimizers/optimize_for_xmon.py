# Copyright 2018 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A combination of several optimizations targeting XmonDevice."""
from typing import Callable, cast, TYPE_CHECKING

import cirq
from cirq import _compat
from cirq_google.optimizers import optimized_for_sycamore

if TYPE_CHECKING:
    import cirq_google


@_compat.deprecated(
    deadline='v0.16',
    # pylint: disable=line-too-long
    fix='Use cirq.optimize_for_target_gateset(circuit, gateset=cirq.CZTargetGateset(atol=tolerance, allow_partial_czs=allow_partial_czs)).',
)
def optimized_for_xmon(
    circuit: cirq.Circuit,
    qubit_map: Callable[[cirq.Qid], cirq.GridQubit] = lambda e: cast(cirq.GridQubit, e),
    allow_partial_czs: bool = False,
) -> cirq.Circuit:
    optimizer_type = 'xmon_partial_cz' if allow_partial_czs else 'xmon'
    ret = optimized_for_sycamore(circuit, qubit_map=qubit_map, optimizer_type=optimizer_type)
    return ret
