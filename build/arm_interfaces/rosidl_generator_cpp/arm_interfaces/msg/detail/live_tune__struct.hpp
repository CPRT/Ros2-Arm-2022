// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from arm_interfaces:msg/LiveTune.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__LIVE_TUNE__STRUCT_HPP_
#define ARM_INTERFACES__MSG__DETAIL__LIVE_TUNE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__arm_interfaces__msg__LiveTune __attribute__((deprecated))
#else
# define DEPRECATED__arm_interfaces__msg__LiveTune __declspec(deprecated)
#endif

namespace arm_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LiveTune_
{
  using Type = LiveTune_<ContainerAllocator>;

  explicit LiveTune_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->arm_motor_number = 0;
      this->command = "";
      this->value = 0.0f;
    }
  }

  explicit LiveTune_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : command(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->arm_motor_number = 0;
      this->command = "";
      this->value = 0.0f;
    }
  }

  // field types and members
  using _arm_motor_number_type =
    int8_t;
  _arm_motor_number_type arm_motor_number;
  using _command_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _command_type command;
  using _value_type =
    float;
  _value_type value;

  // setters for named parameter idiom
  Type & set__arm_motor_number(
    const int8_t & _arg)
  {
    this->arm_motor_number = _arg;
    return *this;
  }
  Type & set__command(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->command = _arg;
    return *this;
  }
  Type & set__value(
    const float & _arg)
  {
    this->value = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    arm_interfaces::msg::LiveTune_<ContainerAllocator> *;
  using ConstRawPtr =
    const arm_interfaces::msg::LiveTune_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<arm_interfaces::msg::LiveTune_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<arm_interfaces::msg::LiveTune_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      arm_interfaces::msg::LiveTune_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<arm_interfaces::msg::LiveTune_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      arm_interfaces::msg::LiveTune_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<arm_interfaces::msg::LiveTune_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<arm_interfaces::msg::LiveTune_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<arm_interfaces::msg::LiveTune_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__arm_interfaces__msg__LiveTune
    std::shared_ptr<arm_interfaces::msg::LiveTune_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__arm_interfaces__msg__LiveTune
    std::shared_ptr<arm_interfaces::msg::LiveTune_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LiveTune_ & other) const
  {
    if (this->arm_motor_number != other.arm_motor_number) {
      return false;
    }
    if (this->command != other.command) {
      return false;
    }
    if (this->value != other.value) {
      return false;
    }
    return true;
  }
  bool operator!=(const LiveTune_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LiveTune_

// alias to use template instance with default allocator
using LiveTune =
  arm_interfaces::msg::LiveTune_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace arm_interfaces

#endif  // ARM_INTERFACES__MSG__DETAIL__LIVE_TUNE__STRUCT_HPP_
