# -*- coding: utf-8 -*-
from openerp import http

# class SparkitFacilitatorWeeklyReports(http.Controller):
#     @http.route('/sparkit_facilitator_weekly_reports/sparkit_facilitator_weekly_reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sparkit_facilitator_weekly_reports/sparkit_facilitator_weekly_reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sparkit_facilitator_weekly_reports.listing', {
#             'root': '/sparkit_facilitator_weekly_reports/sparkit_facilitator_weekly_reports',
#             'objects': http.request.env['sparkit_facilitator_weekly_reports.sparkit_facilitator_weekly_reports'].search([]),
#         })

#     @http.route('/sparkit_facilitator_weekly_reports/sparkit_facilitator_weekly_reports/objects/<model("sparkit_facilitator_weekly_reports.sparkit_facilitator_weekly_reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sparkit_facilitator_weekly_reports.object', {
#             'object': obj
#         })