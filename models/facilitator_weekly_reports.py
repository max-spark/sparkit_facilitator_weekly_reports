# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import date

class FaciltiatorWeeklyReports(models.Model):
    _name = 'sparkit.facilitator_weekly_reports'
    _inherit = 'mail.thread'

    name = fields.Char(compute='_get_name')
    created_date = fields.Date(string="Created Date", compute='_get_date',
        readonly=True)

    user_id = fields.Many2one('res.users', string="User",
        default=lambda self: self.env.user,
        track_visibility='onchange',
        required=True)
    program_manager_id = fields.Many2one('res.users',
        string="Program Manager",
        required=True,
        track_visibility='onchange')

    highlights = fields.Text(string="Highlights from the Week",
        help="What went well?", required=True,
        track_visibility='onchange')
    challenges = fields.Text(string="Challenges Faced this Week",
        help="Please enter any challenges you faced this week, not necessarily community specific.",
        required=True,
        track_visibility='onchange')
    ideas = fields.Text(string="Ideas for How To Address Challenges?",
        required=True,
        track_visibility='onchange')
    questions = fields.Text(string="Questions/Concerns/Inputs Needed",
        required=True,
        track_visibility='onchange')
    suggestions = fields.Text(string="Suggestions", required=True,
        track_visibility='onchange')
    ideas_team_mtg = fields.Text(string="Ideas for Team Meetings",
        track_visibility='onchange')


    next_steps = fields.Text(string="Program Manager: Next Steps")

    @api.multi
    def _get_name(self):
        for r in self:
            r.name =  r.user_id.name + ": " + r.created_date

    @api.multi
    def _get_date(self):
        for r in self:
            r.created_date = r.create_date