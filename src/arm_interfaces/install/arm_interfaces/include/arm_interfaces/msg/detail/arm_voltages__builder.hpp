// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from arm_interfaces:msg/ArmVoltages.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__ARM_VOLTAGES__BUILDER_HPP_
#define ARM_INTERFACES__MSG__DETAIL__ARM_VOLTAGES__BUILDER_HPP_

#include "arm_interfaces/msg/detail/arm_voltages__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace arm_interfaces
{

namespace msg
{

namespace builder
{

class Init_ArmVoltages_m5
{
public:
  explicit Init_ArmVoltages_m5(::arm_interfaces::msg::ArmVoltages & msg)
  : msg_(msg)
  {}
  ::arm_interfaces::msg::ArmVoltages m5(::arm_interfaces::msg::ArmVoltages::_m5_type arg)
  {
    msg_.m5 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interfaces::msg::ArmVoltages msg_;
};

class Init_ArmVoltages_m4
{
public:
  explicit Init_ArmVoltages_m4(::arm_interfaces::msg::ArmVoltages & msg)
  : msg_(msg)
  {}
  Init_ArmVoltages_m5 m4(::arm_interfaces::msg::ArmVoltages::_m4_type arg)
  {
    msg_.m4 = std::move(arg);
    return Init_ArmVoltages_m5(msg_);
  }

private:
  ::arm_interfaces::msg::ArmVoltages msg_;
};

class Init_ArmVoltages_m3
{
public:
  explicit Init_ArmVoltages_m3(::arm_interfaces::msg::ArmVoltages & msg)
  : msg_(msg)
  {}
  Init_ArmVoltages_m4 m3(::arm_interfaces::msg::ArmVoltages::_m3_type arg)
  {
    msg_.m3 = std::move(arg);
    return Init_ArmVoltages_m4(msg_);
  }

private:
  ::arm_interfaces::msg::ArmVoltages msg_;
};

class Init_ArmVoltages_m2
{
public:
  explicit Init_ArmVoltages_m2(::arm_interfaces::msg::ArmVoltages & msg)
  : msg_(msg)
  {}
  Init_ArmVoltages_m3 m2(::arm_interfaces::msg::ArmVoltages::_m2_type arg)
  {
    msg_.m2 = std::move(arg);
    return Init_ArmVoltages_m3(msg_);
  }

private:
  ::arm_interfaces::msg::ArmVoltages msg_;
};

class Init_ArmVoltages_m1
{
public:
  explicit Init_ArmVoltages_m1(::arm_interfaces::msg::ArmVoltages & msg)
  : msg_(msg)
  {}
  Init_ArmVoltages_m2 m1(::arm_interfaces::msg::ArmVoltages::_m1_type arg)
  {
    msg_.m1 = std::move(arg);
    return Init_ArmVoltages_m2(msg_);
  }

private:
  ::arm_interfaces::msg::ArmVoltages msg_;
};

class Init_ArmVoltages_m0
{
public:
  Init_ArmVoltages_m0()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ArmVoltages_m1 m0(::arm_interfaces::msg::ArmVoltages::_m0_type arg)
  {
    msg_.m0 = std::move(arg);
    return Init_ArmVoltages_m1(msg_);
  }

private:
  ::arm_interfaces::msg::ArmVoltages msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interfaces::msg::ArmVoltages>()
{
  return arm_interfaces::msg::builder::Init_ArmVoltages_m0();
}

}  // namespace arm_interfaces

#endif  // ARM_INTERFACES__MSG__DETAIL__ARM_VOLTAGES__BUILDER_HPP_
