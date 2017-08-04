// Auto-generated. Do not edit!

// (in-package vesc_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class VescState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.voltage_input = null;
      this.temperature_pcb = null;
      this.current_motor = null;
      this.current_input = null;
      this.speed = null;
      this.duty_cycle = null;
      this.charge_drawn = null;
      this.charge_regen = null;
      this.energy_drawn = null;
      this.energy_regen = null;
      this.displacement = null;
      this.distance_traveled = null;
      this.fault_code = null;
    }
    else {
      if (initObj.hasOwnProperty('voltage_input')) {
        this.voltage_input = initObj.voltage_input
      }
      else {
        this.voltage_input = 0.0;
      }
      if (initObj.hasOwnProperty('temperature_pcb')) {
        this.temperature_pcb = initObj.temperature_pcb
      }
      else {
        this.temperature_pcb = 0.0;
      }
      if (initObj.hasOwnProperty('current_motor')) {
        this.current_motor = initObj.current_motor
      }
      else {
        this.current_motor = 0.0;
      }
      if (initObj.hasOwnProperty('current_input')) {
        this.current_input = initObj.current_input
      }
      else {
        this.current_input = 0.0;
      }
      if (initObj.hasOwnProperty('speed')) {
        this.speed = initObj.speed
      }
      else {
        this.speed = 0.0;
      }
      if (initObj.hasOwnProperty('duty_cycle')) {
        this.duty_cycle = initObj.duty_cycle
      }
      else {
        this.duty_cycle = 0.0;
      }
      if (initObj.hasOwnProperty('charge_drawn')) {
        this.charge_drawn = initObj.charge_drawn
      }
      else {
        this.charge_drawn = 0.0;
      }
      if (initObj.hasOwnProperty('charge_regen')) {
        this.charge_regen = initObj.charge_regen
      }
      else {
        this.charge_regen = 0.0;
      }
      if (initObj.hasOwnProperty('energy_drawn')) {
        this.energy_drawn = initObj.energy_drawn
      }
      else {
        this.energy_drawn = 0.0;
      }
      if (initObj.hasOwnProperty('energy_regen')) {
        this.energy_regen = initObj.energy_regen
      }
      else {
        this.energy_regen = 0.0;
      }
      if (initObj.hasOwnProperty('displacement')) {
        this.displacement = initObj.displacement
      }
      else {
        this.displacement = 0.0;
      }
      if (initObj.hasOwnProperty('distance_traveled')) {
        this.distance_traveled = initObj.distance_traveled
      }
      else {
        this.distance_traveled = 0.0;
      }
      if (initObj.hasOwnProperty('fault_code')) {
        this.fault_code = initObj.fault_code
      }
      else {
        this.fault_code = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type VescState
    // Serialize message field [voltage_input]
    bufferOffset = _serializer.float64(obj.voltage_input, buffer, bufferOffset);
    // Serialize message field [temperature_pcb]
    bufferOffset = _serializer.float64(obj.temperature_pcb, buffer, bufferOffset);
    // Serialize message field [current_motor]
    bufferOffset = _serializer.float64(obj.current_motor, buffer, bufferOffset);
    // Serialize message field [current_input]
    bufferOffset = _serializer.float64(obj.current_input, buffer, bufferOffset);
    // Serialize message field [speed]
    bufferOffset = _serializer.float64(obj.speed, buffer, bufferOffset);
    // Serialize message field [duty_cycle]
    bufferOffset = _serializer.float64(obj.duty_cycle, buffer, bufferOffset);
    // Serialize message field [charge_drawn]
    bufferOffset = _serializer.float64(obj.charge_drawn, buffer, bufferOffset);
    // Serialize message field [charge_regen]
    bufferOffset = _serializer.float64(obj.charge_regen, buffer, bufferOffset);
    // Serialize message field [energy_drawn]
    bufferOffset = _serializer.float64(obj.energy_drawn, buffer, bufferOffset);
    // Serialize message field [energy_regen]
    bufferOffset = _serializer.float64(obj.energy_regen, buffer, bufferOffset);
    // Serialize message field [displacement]
    bufferOffset = _serializer.float64(obj.displacement, buffer, bufferOffset);
    // Serialize message field [distance_traveled]
    bufferOffset = _serializer.float64(obj.distance_traveled, buffer, bufferOffset);
    // Serialize message field [fault_code]
    bufferOffset = _serializer.int32(obj.fault_code, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type VescState
    let len;
    let data = new VescState(null);
    // Deserialize message field [voltage_input]
    data.voltage_input = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [temperature_pcb]
    data.temperature_pcb = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [current_motor]
    data.current_motor = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [current_input]
    data.current_input = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [speed]
    data.speed = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [duty_cycle]
    data.duty_cycle = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [charge_drawn]
    data.charge_drawn = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [charge_regen]
    data.charge_regen = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [energy_drawn]
    data.energy_drawn = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [energy_regen]
    data.energy_regen = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [displacement]
    data.displacement = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [distance_traveled]
    data.distance_traveled = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [fault_code]
    data.fault_code = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 100;
  }

  static datatype() {
    // Returns string type for a message object
    return 'vesc_msgs/VescState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '81214bb4c1945e7c159bd76ec397ac04';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Vedder VESC open source motor controller state (telemetry)
    
    # fault codes
    int32 FAULT_CODE_NONE=0
    int32 FAULT_CODE_OVER_VOLTAGE=1
    int32 FAULT_CODE_UNDER_VOLTAGE=2
    int32 FAULT_CODE_DRV8302=3
    int32 FAULT_CODE_ABS_OVER_CURRENT=4
    int32 FAULT_CODE_OVER_TEMP_FET=5
    int32 FAULT_CODE_OVER_TEMP_MOTOR=6
    
    float64 voltage_input        # input voltage (volt)
    float64 temperature_pcb      # temperature of printed circuit board (degrees Celsius)
    float64 current_motor        # motor current (ampere)
    float64 current_input        # input current (ampere)
    float64 speed                # motor electrical speed (revolutions per minute) 
    float64 duty_cycle           # duty cycle (0 to 1)
    float64 charge_drawn         # electric charge drawn from input (ampere-hour)
    float64 charge_regen         # electric charge regenerated to input (ampere-hour)
    float64 energy_drawn         # energy drawn from input (watt-hour)
    float64 energy_regen         # energy regenerated to input (watt-hour)
    float64 displacement         # net tachometer (counts)
    float64 distance_traveled    # total tachnometer (counts)
    int32   fault_code
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new VescState(null);
    if (msg.voltage_input !== undefined) {
      resolved.voltage_input = msg.voltage_input;
    }
    else {
      resolved.voltage_input = 0.0
    }

    if (msg.temperature_pcb !== undefined) {
      resolved.temperature_pcb = msg.temperature_pcb;
    }
    else {
      resolved.temperature_pcb = 0.0
    }

    if (msg.current_motor !== undefined) {
      resolved.current_motor = msg.current_motor;
    }
    else {
      resolved.current_motor = 0.0
    }

    if (msg.current_input !== undefined) {
      resolved.current_input = msg.current_input;
    }
    else {
      resolved.current_input = 0.0
    }

    if (msg.speed !== undefined) {
      resolved.speed = msg.speed;
    }
    else {
      resolved.speed = 0.0
    }

    if (msg.duty_cycle !== undefined) {
      resolved.duty_cycle = msg.duty_cycle;
    }
    else {
      resolved.duty_cycle = 0.0
    }

    if (msg.charge_drawn !== undefined) {
      resolved.charge_drawn = msg.charge_drawn;
    }
    else {
      resolved.charge_drawn = 0.0
    }

    if (msg.charge_regen !== undefined) {
      resolved.charge_regen = msg.charge_regen;
    }
    else {
      resolved.charge_regen = 0.0
    }

    if (msg.energy_drawn !== undefined) {
      resolved.energy_drawn = msg.energy_drawn;
    }
    else {
      resolved.energy_drawn = 0.0
    }

    if (msg.energy_regen !== undefined) {
      resolved.energy_regen = msg.energy_regen;
    }
    else {
      resolved.energy_regen = 0.0
    }

    if (msg.displacement !== undefined) {
      resolved.displacement = msg.displacement;
    }
    else {
      resolved.displacement = 0.0
    }

    if (msg.distance_traveled !== undefined) {
      resolved.distance_traveled = msg.distance_traveled;
    }
    else {
      resolved.distance_traveled = 0.0
    }

    if (msg.fault_code !== undefined) {
      resolved.fault_code = msg.fault_code;
    }
    else {
      resolved.fault_code = 0
    }

    return resolved;
    }
};

// Constants for message
VescState.Constants = {
  FAULT_CODE_NONE: 0,
  FAULT_CODE_OVER_VOLTAGE: 1,
  FAULT_CODE_UNDER_VOLTAGE: 2,
  FAULT_CODE_DRV8302: 3,
  FAULT_CODE_ABS_OVER_CURRENT: 4,
  FAULT_CODE_OVER_TEMP_FET: 5,
  FAULT_CODE_OVER_TEMP_MOTOR: 6,
}

module.exports = VescState;
