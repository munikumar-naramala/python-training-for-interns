from fastapi import APIRouter, Query
from schemas.request import MenuRequest, MenuUpdateRequest
from schemas.response import response
from models.models import Menu
from db.database import Database
from sqlalchemy import and_, desc
import uuid

router = APIRouter(
    prefix="/menu",
    tags=["Menu"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()


@router.delete("/delete/{menu_id}")
async def delete_menu(menu_id: str):
    session = database.get_db_session(engine)
    try:
        is_menu_updated = session.query(Menu).filter(and_(Menu.menu_id == menu_id)).delete()
        session.flush()
        session.commit()
        response_msg = "Menu deleted successfully"
        response_code = 200
        error = False
        data = {"menu_id": menu_id}
        if is_menu_updated == 0:
            response_msg = "Menu not deleted. No menu found with this id :" + \
                           str(menu_id)
            error = True
            data = None
        return response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error : ", ex)


@router.put("/update_menu/{menu_id}")
async def update_menu(menu_update_req: MenuUpdateRequest, menu_id: str):
    session = database.get_db_session(engine)
    try:
        is_menu_updated = session.query(Menu).filter(Menu.menu_id == menu_id).update({
            Menu.food_name: menu_update_req.food_name,
            Menu.cuisine: menu_update_req.cuisine,
            Menu.amount: menu_update_req.amount,
        }, synchronize_session=False)
        session.flush()
        session.commit()
        response_msg = "Menu updated successfully"
        response_code = 200
        error = False
        if is_menu_updated == 1:
            data = session.query(Menu).filter(
                Menu.menu_id == menu_id).one()

        elif is_menu_updated == 0:
            response_msg = "Menu not updated. No menu found with this id :" + \
                           str(menu_id)
            error = True
            data = None
        return response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error : ", ex)


@router.post("/add_menu", response_description="Add a menu")
async def add_menu(menu_req: MenuRequest):
    new_menu = Menu()
    new_menu.menu_id = str(uuid.uuid4())
    new_menu.restaurant_id = menu_req.restaurant_id
    new_menu.food_name = menu_req.food_name
    new_menu.cuisine = menu_req.cuisine
    new_menu.amount = menu_req.amount
    try:
        session = database.get_db_session(engine)
        session.add(new_menu)
        session.flush()

        session.refresh(new_menu, attribute_names=['menu_id'])
        data = {"menu_id": new_menu.menu_id}
        session.commit()
        session.close()
        return response(data, 200, "Menu added successfully.", False)
    except BaseException as e:
        print("exception in post method is: ", e)


@router.get("/{menu_id}")
async def read_menu(menu_id: str):
    session = database.get_db_session(engine)
    response_message = "Menu retrieved successfully"
    data = None
    try:
        data = session.query(Menu).filter(
            and_(Menu.restaurant_id == menu_id)).one()
    except Exception as ex:
        print("Error", ex)
        response_message = "Menu Not found"
    error = False
    return response(data, 200, response_message, error)


@router.get("/menu/{restaurant_id}")
def search_menu_by_restaurant_id(query: str = Query(..., description="Search restaurant")):
    results = []
    session = database.get_db_session(engine)
    data = session.query(Menu).all()

    for item in data:
        if query.lower() in item.restaurant_id.lower():
            results.append(item)

    return {"results": results}


@router.get("/menu/search")
def search_menu(query: str = Query(..., description="Search query")):
    results = []
    session = database.get_db_session(engine)
    data = session.query(Menu).all()

    for item in data:
        if query.lower() in item.food_name.lower() or query.lower() in item.cuisine.lower():
            results.append(item)

    return {"results": results}


@router.get("/")
async def read_all_menus():
    try:
        session = database.get_db_session(engine)
        data = session.query(Menu).order_by(
            desc(Menu.menu_id)).all()
        return response(data, 200, "Menus retrieved successfully.", False)
    except BaseException as e:
        print("exception is : ", e)
