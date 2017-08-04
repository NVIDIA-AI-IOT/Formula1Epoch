;; Auto-generated. Do not edit!


(when (boundp 'vesc_msgs::VescState)
  (if (not (find-package "VESC_MSGS"))
    (make-package "VESC_MSGS"))
  (shadow 'VescState (find-package "VESC_MSGS")))
(unless (find-package "VESC_MSGS::VESCSTATE")
  (make-package "VESC_MSGS::VESCSTATE"))

(in-package "ROS")
;;//! \htmlinclude VescState.msg.html


(intern "*FAULT_CODE_NONE*" (find-package "VESC_MSGS::VESCSTATE"))
(shadow '*FAULT_CODE_NONE* (find-package "VESC_MSGS::VESCSTATE"))
(defconstant vesc_msgs::VescState::*FAULT_CODE_NONE* 0)
(intern "*FAULT_CODE_OVER_VOLTAGE*" (find-package "VESC_MSGS::VESCSTATE"))
(shadow '*FAULT_CODE_OVER_VOLTAGE* (find-package "VESC_MSGS::VESCSTATE"))
(defconstant vesc_msgs::VescState::*FAULT_CODE_OVER_VOLTAGE* 1)
(intern "*FAULT_CODE_UNDER_VOLTAGE*" (find-package "VESC_MSGS::VESCSTATE"))
(shadow '*FAULT_CODE_UNDER_VOLTAGE* (find-package "VESC_MSGS::VESCSTATE"))
(defconstant vesc_msgs::VescState::*FAULT_CODE_UNDER_VOLTAGE* 2)
(intern "*FAULT_CODE_DRV8302*" (find-package "VESC_MSGS::VESCSTATE"))
(shadow '*FAULT_CODE_DRV8302* (find-package "VESC_MSGS::VESCSTATE"))
(defconstant vesc_msgs::VescState::*FAULT_CODE_DRV8302* 3)
(intern "*FAULT_CODE_ABS_OVER_CURRENT*" (find-package "VESC_MSGS::VESCSTATE"))
(shadow '*FAULT_CODE_ABS_OVER_CURRENT* (find-package "VESC_MSGS::VESCSTATE"))
(defconstant vesc_msgs::VescState::*FAULT_CODE_ABS_OVER_CURRENT* 4)
(intern "*FAULT_CODE_OVER_TEMP_FET*" (find-package "VESC_MSGS::VESCSTATE"))
(shadow '*FAULT_CODE_OVER_TEMP_FET* (find-package "VESC_MSGS::VESCSTATE"))
(defconstant vesc_msgs::VescState::*FAULT_CODE_OVER_TEMP_FET* 5)
(intern "*FAULT_CODE_OVER_TEMP_MOTOR*" (find-package "VESC_MSGS::VESCSTATE"))
(shadow '*FAULT_CODE_OVER_TEMP_MOTOR* (find-package "VESC_MSGS::VESCSTATE"))
(defconstant vesc_msgs::VescState::*FAULT_CODE_OVER_TEMP_MOTOR* 6)
(defclass vesc_msgs::VescState
  :super ros::object
  :slots (_voltage_input _temperature_pcb _current_motor _current_input _speed _duty_cycle _charge_drawn _charge_regen _energy_drawn _energy_regen _displacement _distance_traveled _fault_code ))

(defmethod vesc_msgs::VescState
  (:init
   (&key
    ((:voltage_input __voltage_input) 0.0)
    ((:temperature_pcb __temperature_pcb) 0.0)
    ((:current_motor __current_motor) 0.0)
    ((:current_input __current_input) 0.0)
    ((:speed __speed) 0.0)
    ((:duty_cycle __duty_cycle) 0.0)
    ((:charge_drawn __charge_drawn) 0.0)
    ((:charge_regen __charge_regen) 0.0)
    ((:energy_drawn __energy_drawn) 0.0)
    ((:energy_regen __energy_regen) 0.0)
    ((:displacement __displacement) 0.0)
    ((:distance_traveled __distance_traveled) 0.0)
    ((:fault_code __fault_code) 0)
    )
   (send-super :init)
   (setq _voltage_input (float __voltage_input))
   (setq _temperature_pcb (float __temperature_pcb))
   (setq _current_motor (float __current_motor))
   (setq _current_input (float __current_input))
   (setq _speed (float __speed))
   (setq _duty_cycle (float __duty_cycle))
   (setq _charge_drawn (float __charge_drawn))
   (setq _charge_regen (float __charge_regen))
   (setq _energy_drawn (float __energy_drawn))
   (setq _energy_regen (float __energy_regen))
   (setq _displacement (float __displacement))
   (setq _distance_traveled (float __distance_traveled))
   (setq _fault_code (round __fault_code))
   self)
  (:voltage_input
   (&optional __voltage_input)
   (if __voltage_input (setq _voltage_input __voltage_input)) _voltage_input)
  (:temperature_pcb
   (&optional __temperature_pcb)
   (if __temperature_pcb (setq _temperature_pcb __temperature_pcb)) _temperature_pcb)
  (:current_motor
   (&optional __current_motor)
   (if __current_motor (setq _current_motor __current_motor)) _current_motor)
  (:current_input
   (&optional __current_input)
   (if __current_input (setq _current_input __current_input)) _current_input)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:duty_cycle
   (&optional __duty_cycle)
   (if __duty_cycle (setq _duty_cycle __duty_cycle)) _duty_cycle)
  (:charge_drawn
   (&optional __charge_drawn)
   (if __charge_drawn (setq _charge_drawn __charge_drawn)) _charge_drawn)
  (:charge_regen
   (&optional __charge_regen)
   (if __charge_regen (setq _charge_regen __charge_regen)) _charge_regen)
  (:energy_drawn
   (&optional __energy_drawn)
   (if __energy_drawn (setq _energy_drawn __energy_drawn)) _energy_drawn)
  (:energy_regen
   (&optional __energy_regen)
   (if __energy_regen (setq _energy_regen __energy_regen)) _energy_regen)
  (:displacement
   (&optional __displacement)
   (if __displacement (setq _displacement __displacement)) _displacement)
  (:distance_traveled
   (&optional __distance_traveled)
   (if __distance_traveled (setq _distance_traveled __distance_traveled)) _distance_traveled)
  (:fault_code
   (&optional __fault_code)
   (if __fault_code (setq _fault_code __fault_code)) _fault_code)
  (:serialization-length
   ()
   (+
    ;; float64 _voltage_input
    8
    ;; float64 _temperature_pcb
    8
    ;; float64 _current_motor
    8
    ;; float64 _current_input
    8
    ;; float64 _speed
    8
    ;; float64 _duty_cycle
    8
    ;; float64 _charge_drawn
    8
    ;; float64 _charge_regen
    8
    ;; float64 _energy_drawn
    8
    ;; float64 _energy_regen
    8
    ;; float64 _displacement
    8
    ;; float64 _distance_traveled
    8
    ;; int32 _fault_code
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _voltage_input
       (sys::poke _voltage_input (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _temperature_pcb
       (sys::poke _temperature_pcb (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _current_motor
       (sys::poke _current_motor (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _current_input
       (sys::poke _current_input (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _duty_cycle
       (sys::poke _duty_cycle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _charge_drawn
       (sys::poke _charge_drawn (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _charge_regen
       (sys::poke _charge_regen (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _energy_drawn
       (sys::poke _energy_drawn (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _energy_regen
       (sys::poke _energy_regen (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _displacement
       (sys::poke _displacement (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _distance_traveled
       (sys::poke _distance_traveled (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int32 _fault_code
       (write-long _fault_code s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _voltage_input
     (setq _voltage_input (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _temperature_pcb
     (setq _temperature_pcb (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _current_motor
     (setq _current_motor (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _current_input
     (setq _current_input (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _speed
     (setq _speed (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _duty_cycle
     (setq _duty_cycle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _charge_drawn
     (setq _charge_drawn (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _charge_regen
     (setq _charge_regen (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _energy_drawn
     (setq _energy_drawn (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _energy_regen
     (setq _energy_regen (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _displacement
     (setq _displacement (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _distance_traveled
     (setq _distance_traveled (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int32 _fault_code
     (setq _fault_code (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get vesc_msgs::VescState :md5sum-) "81214bb4c1945e7c159bd76ec397ac04")
(setf (get vesc_msgs::VescState :datatype-) "vesc_msgs/VescState")
(setf (get vesc_msgs::VescState :definition-)
      "# Vedder VESC open source motor controller state (telemetry)

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

")



(provide :vesc_msgs/VescState "81214bb4c1945e7c159bd76ec397ac04")


