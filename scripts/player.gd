#extends "res://scripts/entity.gd"
extends KinematicBody2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var left = "ui_right"
var right = "ui_right"
var velocity = Vector2()
# Called when the node enters the scene tree for the first time.
func _ready():
	print("Hola mundo!")
	pass # Replace with function body.


func get_input():
	velocity= Vector2()
	if Input.is_action_just_pressed(left):
		velocity.x += 1
	if Input.is_action_just_pressed(right):
		velocity.x -=1


func _physics_process(delta):
	get_input()
	velocity = move_and_slide(velocity)
