// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from arm_interfaces:msg/ArmVoltages.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__ARM_VOLTAGES__STRUCT_H_
#define ARM_INTERFACES__MSG__DETAIL__ARM_VOLTAGES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/ArmVoltages in the package arm_interfaces.
typedef struct arm_interfaces__msg__ArmVoltages
{
  float m0;
  float m1;
  float m2;
  float m3;
  float m4;
  float m5;
} arm_interfaces__msg__ArmVoltages;

// Struct for a sequence of arm_interfaces__msg__ArmVoltages.
typedef struct arm_interfaces__msg__ArmVoltages__Sequence
{
  arm_interfaces__msg__ArmVoltages * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} arm_interfaces__msg__ArmVoltages__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ARM_INTERFACES__MSG__DETAIL__ARM_VOLTAGES__STRUCT_H_
