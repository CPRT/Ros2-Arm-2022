// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from arm_interfaces:msg/LiveTune.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__LIVE_TUNE__STRUCT_H_
#define ARM_INTERFACES__MSG__DETAIL__LIVE_TUNE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'command'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/LiveTune in the package arm_interfaces.
typedef struct arm_interfaces__msg__LiveTune
{
  int8_t arm_motor_number;
  rosidl_runtime_c__String command;
  float value;
} arm_interfaces__msg__LiveTune;

// Struct for a sequence of arm_interfaces__msg__LiveTune.
typedef struct arm_interfaces__msg__LiveTune__Sequence
{
  arm_interfaces__msg__LiveTune * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} arm_interfaces__msg__LiveTune__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ARM_INTERFACES__MSG__DETAIL__LIVE_TUNE__STRUCT_H_
