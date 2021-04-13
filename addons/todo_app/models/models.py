# -*- coding: utf-8 -*-
from odoo import models,fields

class ToDo(models.Model):
    _name = "todo.app" # nombre de la base de datos: todo_app
    _description = "Lista de Tareas"
    _rec_name = "name"

    name = fields.Char(string="Nombre")
    state = fields.Char(string="Estado")
    description = fields.Char(string="Descripción")
    #title = fields.Char(String="titulo")
    #price = fields.Float(string="Precio")