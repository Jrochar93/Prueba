from odoo import models, fields

class Task(models.Model):
    _name = 'task.management'
    _description = 'Task Management'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    is_completed = fields.Boolean(string='Completed', default=False)
    date_deadline = fields.Date(string='Deadline')

    def mark_as_completed(self):
        """Mark task as completed"""
        for record in self:
            record.is_completed = True
