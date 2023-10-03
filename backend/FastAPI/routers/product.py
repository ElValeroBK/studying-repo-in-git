from fastapi import APIRouter

router= APIRouter(prefix="/product",
                  tags=["product"],
                  responses={404: {"message": "No se ha encontrado el producto"}})

product_list= ["product_1","product_2",
                "product_3", "product_4", "product_5"]


@router.get("/")

async def product():
    return product_list


@router.get("/{id}")

async def product(id:int):
    return product_list[id]