// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from arm_interfaces:msg/LiveTune.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "arm_interfaces/msg/detail/live_tune__rosidl_typesupport_introspection_c.h"
#include "arm_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "arm_interfaces/msg/detail/live_tune__functions.h"
#include "arm_interfaces/msg/detail/live_tune__struct.h"


// Include directives for member types
// Member `command`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void LiveTune__rosidl_typesupport_introspection_c__LiveTune_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  arm_interfaces__msg__LiveTune__init(message_memory);
}

void LiveTune__rosidl_typesupport_introspection_c__LiveTune_fini_function(void * message_memory)
{
  arm_interfaces__msg__LiveTune__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember LiveTune__rosidl_typesupport_introspection_c__LiveTune_message_member_array[3] = {
  {
    "arm_motor_number",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(arm_interfaces__msg__LiveTune, arm_motor_number),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "command",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(arm_interfaces__msg__LiveTune, command),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "value",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(arm_interfaces__msg__LiveTune, value),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers LiveTune__rosidl_typesupport_introspection_c__LiveTune_message_members = {
  "arm_interfaces__msg",  // message namespace
  "LiveTune",  // message name
  3,  // number of fields
  sizeof(arm_interfaces__msg__LiveTune),
  LiveTune__rosidl_typesupport_introspection_c__LiveTune_message_member_array,  // message members
  LiveTune__rosidl_typesupport_introspection_c__LiveTune_init_function,  // function to initialize message memory (memory has to be allocated)
  LiveTune__rosidl_typesupport_introspection_c__LiveTune_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t LiveTune__rosidl_typesupport_introspection_c__LiveTune_message_type_support_handle = {
  0,
  &LiveTune__rosidl_typesupport_introspection_c__LiveTune_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_arm_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, arm_interfaces, msg, LiveTune)() {
  if (!LiveTune__rosidl_typesupport_introspection_c__LiveTune_message_type_support_handle.typesupport_identifier) {
    LiveTune__rosidl_typesupport_introspection_c__LiveTune_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &LiveTune__rosidl_typesupport_introspection_c__LiveTune_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
