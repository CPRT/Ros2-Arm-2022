// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from arm_interfaces:msg/ArmVoltages.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__ARM_VOLTAGES__STRUCT_HPP_
#define ARM_INTERFACES__MSG__DETAIL__ARM_VOLTAGES__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__arm_interfaces__msg__ArmVoltages __attribute__((deprecated))
#else
# define DEPRECATED__arm_interfaces__msg__ArmVoltages __declspec(deprecated)
#endif

namespace arm_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ArmVoltages_
{
  using Type = ArmVoltages_<ContainerAllocator>;

  explicit ArmVoltages_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->m0 = 0.0f;
      this->m1 = 0.0f;
      this->m2 = 0.0f;
      this->m3 = 0.0f;
      this->m4 = 0.0f;
      this->m5 = 0.0f;
    }
  }

  explicit ArmVoltages_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->m0 = 0.0f;
      this->m1 = 0.0f;
      this->m2 = 0.0f;
      this->m3 = 0.0f;
      this->m4 = 0.0f;
      this->m5 = 0.0f;
    }
  }

  // field types and members
  using _m0_type =
    float;
  _m0_type m0;
  using _m1_type =
    float;
  _m1_type m1;
  using _m2_type =
    float;
  _m2_type m2;
  using _m3_type =
    float;
  _m3_type m3;
  using _m4_type =
    float;
  _m4_type m4;
  using _m5_type =
    float;
  _m5_type m5;

  // setters for named parameter idiom
  Type & set__m0(
    const float & _arg)
  {
    this->m0 = _arg;
    return *this;
  }
  Type & set__m1(
    const float & _arg)
  {
    this->m1 = _arg;
    return *this;
  }
  Type & set__m2(
    const float & _arg)
  {
    this->m2 = _arg;
    return *this;
  }
  Type & set__m3(
    const float & _arg)
  {
    this->m3 = _arg;
    return *this;
  }
  Type & set__m4(
    const float & _arg)
  {
    this->m4 = _arg;
    return *this;
  }
  Type & set__m5(
    const float & _arg)
  {
    this->m5 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    arm_interfaces::msg::ArmVoltages_<ContainerAllocator> *;
  using ConstRawPtr =
    const arm_interfaces::msg::ArmVoltages_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<arm_interfaces::msg::ArmVoltages_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<arm_interfaces::msg::ArmVoltages_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      arm_interfaces::msg::ArmVoltages_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<arm_interfaces::msg::ArmVoltages_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      arm_interfaces::msg::ArmVoltages_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<arm_interfaces::msg::ArmVoltages_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<arm_interfaces::msg::ArmVoltages_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<arm_interfaces::msg::ArmVoltages_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__arm_interfaces__msg__ArmVoltages
    std::shared_ptr<arm_interfaces::msg::ArmVoltages_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__arm_interfaces__msg__ArmVoltages
    std::shared_ptr<arm_interfaces::msg::ArmVoltages_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ArmVoltages_ & other) const
  {
    if (this->m0 != other.m0) {
      return false;
    }
    if (this->m1 != other.m1) {
      return false;
    }
    if (this->m2 != other.m2) {
      return false;
    }
    if (this->m3 != other.m3) {
      return false;
    }
    if (this->m4 != other.m4) {
      return false;
    }
    if (this->m5 != other.m5) {
      return false;
    }
    return true;
  }
  bool operator!=(const ArmVoltages_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ArmVoltages_

// alias to use template instance with default allocator
using ArmVoltages =
  arm_interfaces::msg::ArmVoltages_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace arm_interfaces

#endif  // ARM_INTERFACES__MSG__DETAIL__ARM_VOLTAGES__STRUCT_HPP_
