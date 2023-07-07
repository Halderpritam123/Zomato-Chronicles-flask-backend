from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dummy data for menu
menu = [
    {"id": 1, "name": "Dish 1", "price": 10, "availability": True},
    {"id": 2, "name": "Dish 2", "price": 15, "availability": True},
    {"id": 3, "name": "Dish 3", "price": 12, "availability": False},
    {"id": 4, "name": "Dish 4", "price": 20, "availability": True},
]

# Dummy data for order
order = []

@app.route('/')
def index():
    return redirect('/menu')

@app.route('/menu')
def show_menu():
    return render_template('menu.html', menu=menu)

@app.route('/menu/add', methods=['POST'])
def add_to_menu():
    dish_id = request.form.get('dish_id')
    dish_name = request.form.get('dish_name')
    dish_price = float(request.form.get('dish_price'))
    dish_availability = bool(request.form.get('dish_availability'))
    
    new_dish = {
        'id': dish_id,
        'name': dish_name,
        'price': dish_price,
        'availability': dish_availability
    }
    menu.append(new_dish)
    
    return redirect('/menu')

@app.route('/menu/remove/<int:dish_id>', methods=['POST'])
def remove_from_menu(dish_id):
    global menu
    menu = [dish for dish in menu if dish['id'] != dish_id]
    
    return redirect('/menu')

@app.route('/menu/update/<int:dish_id>', methods=['POST'])
def update_availability(dish_id):
    global menu
    
    for dish in menu:
        if dish['id'] == dish_id:
            dish['availability'] = not dish['availability']
            break
    
    return redirect('/menu')

@app.route('/order')
def show_order():
    return render_template('order.html', order=order)

@app.route('/order/add/<int:dish_id>', methods=['POST'])
def add_to_order(dish_id):
    global menu, order
    
    for dish in menu:
        if dish['id'] == dish_id:
            order.append(dish)
            break
    
    return redirect('/order')

@app.route('/order/remove/<int:dish_id>', methods=['POST'])
def remove_from_order(dish_id):
    global order
    order = [dish for dish in order if dish['id'] != dish_id]
    
    return redirect('/order')

@app.route('/order/update/<int:dish_id>', methods=['POST'])
def update_status(dish_id):
    global order
    dish_status = request.form.get('dish_status')
    
    for dish in order:
        if dish['id'] == dish_id:
            dish['status'] = dish_status
            break
    
    return redirect('/order')

if __name__ == '__main__':
    app.run(debug=True)
