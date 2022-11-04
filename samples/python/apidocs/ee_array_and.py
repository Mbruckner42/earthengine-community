# Copyright 2021 The Google Earth Engine Community Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START earthengine__apidocs__ee_array_and]
# Element-wise boolean "and" operator.
# Both arrays must be the same dimensions.
arrayNeither = ee.Array([0, 0])
arrayFirst = ee.Array([1, 0])
arraySecond = ee.Array([0, 1])
arrayBoth = ee.Array([1, 1])
# Any non-zero value is true.
arrayLarger = ee.Array([-2, 2])

print(arrayBoth.And(arrayLarger).getInfo())  # [1, 1]
print(arrayBoth.And(arrayNeither).getInfo())  # [0, 0]

print(arrayFirst.And(arraySecond).getInfo())  # [0, 0]
print(arraySecond.And(arrayFirst).getInfo())  # [0, 0]

print(arrayBoth.And(arrayFirst).getInfo())  # [1, 0]
print(arrayBoth.And(arraySecond).getInfo())  # [0, 1]

print(arrayNeither.And(arrayFirst).getInfo())  # [0, 0]
print(arrayNeither.And(arraySecond).getInfo())  # [0, 0]

# Works the same for all PixelTypes.
arrayDouble = ee.Array([0.0, 2.0], ee.PixelType.double())
print(arrayBoth.And(arrayDouble).getInfo())  # [0, 1]
# [END earthengine__apidocs__ee_array_and]
