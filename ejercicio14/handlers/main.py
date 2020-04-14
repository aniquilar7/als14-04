#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2
from datetime import datetime

class MainHandler(webapp2.RequestHandler):
    def post(self):
        emCif = self.request.get("emCif", "Desconocido")
        if len(emCif.strip()) == 0:
            emCif = "Desconocido"
        emNom = self.request.get("emNom", "Desconocido")
        if len(emNom.strip()) == 0:
            emNom = "Desconocido"
        emDir = self.request.get("emDir", "Desconocido")
        if len(emDir.strip()) == 0:
            emDir = "Desconocido"
        emPob = self.request.get("emPob", "Desconocido")
        if len(emPob.strip()) == 0:
            emPob = "Desconocido"
        emPro = self.request.get("emPro", "Desconocido")
        if len(emPro.strip()) == 0:
            emPro = "Desconocido"
        emCod = self.request.get("emCod", "Desconocido")
        if len(emCod.strip()) == 0:
            emCod = "Desconocido"
        emPais = self.request.get("emPais", "Desconocido")
        if len(emPais.strip()) == 0:
            emPais = "Desconocido"
        emPer = self.request.get("emPer", "Desconocido")
        if len(emPer.strip()) == 0:
            emPer = "Desconocido"
        emEmail = self.request.get("emEmail", "Desconocido")
        if len(emEmail.strip()) == 0:
            emEmail = "Desconocido"
        emTel = self.request.get("emTel", "Desconocido")
        if len(emTel.strip()) == 0:
            emTel = "Desconocido"
        clCif = self.request.get("clCif", "Desconocido")
        if len(clCif.strip()) == 0:
            clCif = "Desconocido"
        clNom = self.request.get("clNom", "Desconocido")
        if len(clNom.strip()) == 0:
            clNom = "Desconocido"
        clDir = self.request.get("clDir", "Desconocido")
        if len(clDir.strip()) == 0:
            clDir = "Desconocido"
        clPob = self.request.get("clPob", "Desconocido")
        if len(clPob.strip()) == 0:
            clPob = "Desconocido"
        clPro = self.request.get("clPro", "Desconocido")
        if len(clPro.strip()) == 0:
            clPro = "Desconocido"
        clCod = self.request.get("clCod", "Desconocido")
        if len(clCod.strip()) == 0:
            clCod = "Desconocido"
        clPais = self.request.get("clPais", "Desconocido")
        if len(clPais.strip()) == 0:
            clPais = "Desconocido"
        clPer = self.request.get("clPer", "Desconocido")
        if len(clPer.strip()) == 0:
            clPer = "Desconocido"
        clEmail = self.request.get("clEmail", "Desconocido")
        if len(clEmail.strip()) == 0:
            clEmail = "Desconocido"
        clTel = self.request.get("clTel", "Desconocido")
        if len(clTel.strip()) == 0:
            clTel = "Desconocido"
        con = self.request.get("con", "Desconocido")
        if len(con.strip()) == 0:
            con = "Desconocido"
        prc = self.request.get("prc", "Desconocido")
        if len(prc.strip()) == 0:
            prc = "Desconocido"
        und = self.request.get("und", "Desconocido")
        if len(und.strip()) == 0:
            und = "Desconocido"
        imp = self.request.get("imp", "Desconocido")
        if len(imp.strip()) == 0:
            imp = "Desconocido"
        iva = self.request.get("iva", "Desconocido")
        if len(iva.strip()) == 0:
            iva = "Desconocido"
        total = self.request.get("total", "Desconocido")
        if len(total.strip()) == 0:
            total = "Desconocido"

        fecha = datetime.now()

        valores_factura = {
            "emCif": emCif,
            "emNom": emNom,
            "emDir": emDir,
            "emPob": emPob,
            "emPro": emPro,
            "emCod": emCod,
            "emPais": emPais,
            "emPer": emPer,
            "emEmail": emEmail,
            "emTel": emTel,
            "clCif": clCif,
            "clNom": clNom,
            "clDir": clDir,
            "clPob": clPob,
            "clPro": clPro,
            "clCod": clCod,
            "clPais": clPais,
            "clPer": clPer,
            "clEmail": clEmail,
            "clTel": clTel,
            "con": con,
            "prc": prc,
            "und": und,
            "imp": imp,
            "iva": iva,
            "total": total,
            "fecha": fecha
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("factura.html", **valores_factura))

app = webapp2.WSGIApplication([
    ('/index', MainHandler)
], debug=True)
