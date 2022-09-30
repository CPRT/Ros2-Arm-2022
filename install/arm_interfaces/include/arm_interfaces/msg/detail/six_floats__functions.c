// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from arm_interfaces:msg/SixFloats.idl
// generated code does not contain a copyright notice
#include "arm_interfaces/msg/detail/six_floats__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
arm_interfaces__msg__SixFloats__init(arm_interfaces__msg__SixFloats * msg)
{
  if (!msg) {
    return false;
  }
  // m0
  // m1
  // m2
  // m3
  // m4
  // m5
  return true;
}

void
arm_interfaces__msg__SixFloats__fini(arm_interfaces__msg__SixFloats * msg)
{
  if (!msg) {
    return;
  }
  // m0
  // m1
  // m2
  // m3
  // m4
  // m5
}

bool
arm_interfaces__msg__SixFloats__are_equal(const arm_interfaces__msg__SixFloats * lhs, const arm_interfaces__msg__SixFloats * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // m0
  if (lhs->m0 != rhs->m0) {
    return false;
  }
  // m1
  if (lhs->m1 != rhs->m1) {
    return false;
  }
  // m2
  if (lhs->m2 != rhs->m2) {
    return false;
  }
  // m3
  if (lhs->m3 != rhs->m3) {
    return false;
  }
  // m4
  if (lhs->m4 != rhs->m4) {
    return false;
  }
  // m5
  if (lhs->m5 != rhs->m5) {
    return false;
  }
  return true;
}

bool
arm_interfaces__msg__SixFloats__copy(
  const arm_interfaces__msg__SixFloats * input,
  arm_interfaces__msg__SixFloats * output)
{
  if (!input || !output) {
    return false;
  }
  // m0
  output->m0 = input->m0;
  // m1
  output->m1 = input->m1;
  // m2
  output->m2 = input->m2;
  // m3
  output->m3 = input->m3;
  // m4
  output->m4 = input->m4;
  // m5
  output->m5 = input->m5;
  return true;
}

arm_interfaces__msg__SixFloats *
arm_interfaces__msg__SixFloats__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__msg__SixFloats * msg = (arm_interfaces__msg__SixFloats *)allocator.allocate(sizeof(arm_interfaces__msg__SixFloats), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(arm_interfaces__msg__SixFloats));
  bool success = arm_interfaces__msg__SixFloats__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
arm_interfaces__msg__SixFloats__destroy(arm_interfaces__msg__SixFloats * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    arm_interfaces__msg__SixFloats__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
arm_interfaces__msg__SixFloats__Sequence__init(arm_interfaces__msg__SixFloats__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__msg__SixFloats * data = NULL;

  if (size) {
    data = (arm_interfaces__msg__SixFloats *)allocator.zero_allocate(size, sizeof(arm_interfaces__msg__SixFloats), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = arm_interfaces__msg__SixFloats__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        arm_interfaces__msg__SixFloats__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
arm_interfaces__msg__SixFloats__Sequence__fini(arm_interfaces__msg__SixFloats__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      arm_interfaces__msg__SixFloats__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

arm_interfaces__msg__SixFloats__Sequence *
arm_interfaces__msg__SixFloats__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__msg__SixFloats__Sequence * array = (arm_interfaces__msg__SixFloats__Sequence *)allocator.allocate(sizeof(arm_interfaces__msg__SixFloats__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = arm_interfaces__msg__SixFloats__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
arm_interfaces__msg__SixFloats__Sequence__destroy(arm_interfaces__msg__SixFloats__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    arm_interfaces__msg__SixFloats__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
arm_interfaces__msg__SixFloats__Sequence__are_equal(const arm_interfaces__msg__SixFloats__Sequence * lhs, const arm_interfaces__msg__SixFloats__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!arm_interfaces__msg__SixFloats__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
arm_interfaces__msg__SixFloats__Sequence__copy(
  const arm_interfaces__msg__SixFloats__Sequence * input,
  arm_interfaces__msg__SixFloats__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(arm_interfaces__msg__SixFloats);
    arm_interfaces__msg__SixFloats * data =
      (arm_interfaces__msg__SixFloats *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!arm_interfaces__msg__SixFloats__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          arm_interfaces__msg__SixFloats__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!arm_interfaces__msg__SixFloats__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
