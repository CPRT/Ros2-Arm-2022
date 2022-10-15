// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from arm_interfaces:msg/LiveTune.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__LIVE_TUNE__BUILDER_HPP_
#define ARM_INTERFACES__MSG__DETAIL__LIVE_TUNE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "arm_interfaces/msg/detail/live_tune__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace arm_interfaces
{

namespace msg
{

namespace builder
{

class Init_LiveTune_value
{
public:
  explicit Init_LiveTune_value(::arm_interfaces::msg::LiveTune & msg)
  : msg_(msg)
  {}
  ::arm_interfaces::msg::LiveTune value(::arm_interfaces::msg::LiveTune::_value_type arg)
  {
    msg_.value = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interfaces::msg::LiveTune msg_;
};

class Init_LiveTune_command
{
public:
  explicit Init_LiveTune_command(::arm_interfaces::msg::LiveTune & msg)
  : msg_(msg)
  {}
  Init_LiveTune_value command(::arm_interfaces::msg::LiveTune::_command_type arg)
  {
    msg_.command = std::move(arg);
    return Init_LiveTune_value(msg_);
  }

private:
  ::arm_interfaces::msg::LiveTune msg_;
};

class Init_LiveTune_arm_motor_number
{
public:
  Init_LiveTune_arm_motor_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LiveTune_command arm_motor_number(::arm_interfaces::msg::LiveTune::_arm_motor_number_type arg)
  {
    msg_.arm_motor_number = std::move(arg);
    return Init_LiveTune_command(msg_);
  }

private:
  ::arm_interfaces::msg::LiveTune msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interfaces::msg::LiveTune>()
{
  return arm_interfaces::msg::builder::Init_LiveTune_arm_motor_number();
}

}  // namespace arm_interfaces

#endif  // ARM_INTERFACES__MSG__DETAIL__LIVE_TUNE__BUILDER_HPP_
