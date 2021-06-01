from DB_functions import *
from string import Template
import cgi

Part_Template_1 = """
    <tr>
        <th scope="row">$num</th>
        <td>$name</td>
        <td>$code</td>
        <td>$category</td>
        <td>$price</td>
        <td>
            <form method="POST" action="/?$additional_info">
                <input type="number" min=1 name="amount_$id" value=$value>
                <input type="submit" value="Add">
            </form>
        </td>
    </tr>
"""

Part_Template_2 = """
    <tr>
        <th scope="row">$num</th>
        <td>$name</td>
        <td>$code</td>
        <td>$category</td>
        <td>$price</td>
        <td>
            <form method="POST" action="/order">
                <input type="number" min=1 name="amount_$id" value=$value>
                <input type="submit" value="Edit">
            </form>
        </td>
        <td>
            <form method="POST" action="/order?del=$id">
                <input type="submit" value="Delete">
            </form>
        </td>
    </tr>
"""

Car_Template_1 = """
    <tr>
        <th scope="row">$num</th>
        <td>$brand</td>
        <td>$model</td>
        <td>$year</td>
        <td>
            <form method="POST" action="/">
                <button class="btn btn-outline-success" type="submit">Add part</button>
            </form>
        </td>
        <td>
            <form method="POST" action="/">
                <button class="btn btn-outline-success" type="submit">Edit</button>
            </form>
        </td>
        <td>
            <form method="POST" action="/">
                <button class="btn btn-outline-success" type="submit">Delete</button>
            </form>
        </td>
    </tr>
"""


in_order = {}
bill_id_0 = 0


class Shop:
    def __init__(self, db_name):
        self.db = db_name

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "").lstrip("/")
        status = "200 OK"
        headers = [("Content-Type", "text/html; charset=utf-8")]
        global in_order
        global bill_id_0

        # http://127.0.0.1:8000/
        if path == "":
            form = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)
            #  print(form)
            cat_search, nam_search = form.getfirst("cat_search"), form.getfirst("name_search")
            if cat_search:
                on_main_page = category_search(cat_search)
            elif nam_search:
                on_main_page = name_search(nam_search)
            else:
                on_main_page = category_search("")

            all_data = category_search("")
            for part in all_data:
                temp_id = part[0]
                temp_amount = form.getfirst("amount_" + str(temp_id))
                if temp_amount:
                    additional_id = temp_id
                    additional_amount = temp_amount
                    in_order[additional_id] = int(additional_amount)
                    #  print(in_order)
                    break

            html = "templates/main_page.html"
            params = {"on_main_page_html": "", "search_value_cat": "", "search_value_nam": ""}
            ans = ""

            a, b, c = "", "", ""
            if cat_search:
                a = "cat_search=" + cat_search
                b = cat_search
            elif nam_search:
                a = "name_search=" + nam_search
                c = nam_search

            counter = 0
            for item in on_main_page:
                counter += 1

                ans += Template(Part_Template_1).substitute(num=counter, name=item[4],
                                                            id=item[0], code=item[1],
                                                            category=item[3], price=item[5],
                                                            additional_info=a,
                                                            value=(in_order[item[0]]
                                                                   if item[0] in in_order.keys() else ""))
            params["on_main_page_html"] = ans
            params["search_value_cat"] = b
            params["search_value_nam"] = c

        # http://127.0.0.1:8000/order
        elif path == "order":
            form = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)

            delete_id = form.getfirst("del")
            if delete_id:
                #  print(in_order)
                in_order.pop(int(delete_id))

            all_data = category_search("")
            for part in all_data:
                temp_id = part[0]
                temp_amount = form.getfirst("amount_" + str(temp_id))
                if temp_amount:
                    edit_id = temp_id
                    edit_amount = temp_amount
                    in_order[edit_id] = int(edit_amount)
                    #  print(in_order)
                    break

            html = "templates/order_page.html"
            params = {"on_order_page_html": ""}
            ans = ""
            counter = 0
            for key, value in in_order.items():
                counter += 1
                item = print_part(key)
                ans += Template(Part_Template_2).substitute(num=counter, name=item[4], id=item[0], code=item[1],
                                                            category=item[3], price=item[5], value=value)
            params["on_order_page_html"] = ans

        # http://127.0.0.1:8000/order/result
        elif path == "order/result":
            params = {"status": ""}
            form = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)
            date, phone = str(form.getfirst("date")), form.getfirst("phone")

            if date and phone and len(in_order.keys()) != 0:
                bill_id_0 = add_bill(date, phone, in_order)
                in_order = {}
                params["status"] = "Order has been added to the DataBase"
            else:
                status = "303 SEE OTHER"
                headers.append(("Location", "/order"))
            html = "templates/status.html"

        # http://127.0.0.1:8000/order/result/json
        elif path == "order/result/json":
            params = {"status": ""}

            try:
                page = bill_json(bill_id_0)
                headers[0] = ("Content-Type", "text/json; charset=utf-8")
                start_response(status, headers)
                return [bytes(page, encoding="utf-8")]
            except:
                status = "303 SEE OTHER"
                headers.append(("Location", "/order"))
            html = "templates/status.html"

        #

        #

        #

        #

        #

        # http://127.0.0.1:8000/edit_db/cars
        elif path == "edit_db/cars":
            params = {}
            html = "templates/DB_pages/cars_page.html"

        # http://127.0.0.1:8000/edit_db/cars/add_car
        elif path == "edit_db/cars/add_car":
            params = {}
            html = "templates/DB_pages/add_car_page.html"

        # http://127.0.0.1:8000/edit_db/cars/add_part
        elif path == "edit_db/cars/add_part":
            params = {}
            html = "templates/DB_pages/add_part_page.html"

        # http://127.0.0.1:8000/edit_db/cars/edit_car
        elif path == "edit_db/cars/edit_car":
            params = {}
            html = "templates/DB_pages/edit_car_page.html"

        # http://127.0.0.1:8000/edit_db/cars/delete_car
        elif path == "edit_db/cars/delete_car":
            params = {}
            html = "templates/DB_pages/delete_car_page.html"

        # http://127.0.0.1:8000/edit_db/parts
        elif path == "edit_db/parts":
            params = {}
            html = "templates/DB_pages/parts_page.html"

        # http://127.0.0.1:8000/edit_db/parts/edit_part
        elif path == "edit_db/parts/edit_part":
            params = {}
            html = "templates/DB_pages/edit_part_page.html"

        # http://127.0.0.1:8000/edit_db/parts/delete_part
        elif path == "edit_db/parts/delete_part":
            params = {}
            html = "templates/DB_pages/delete_part_page.html"

        # http://127.0.0.1:8000/edit_db/parts/delete_part
        elif path == "edit_db/":
            params = {}
            html = "templates/DB_pages/delete_part_page.html"

        #

        #

        #

        #

        #

        # any other link
        else:
            status = "404 NOT FOUND"
            params = {}
            html = "templates/error_404.html"

        start_response(status, headers)
        with open(html, encoding="utf-8") as f:
            page = Template(f.read()).substitute(params)
        return [bytes(page, encoding="utf-8")]


HOST = ""
PORT = 8000

if __name__ == '__main__':
    app = Shop(db_filename)
    from wsgiref.simple_server import make_server

    print(" === Local webserver === ")
    make_server(HOST, PORT, app).serve_forever()
