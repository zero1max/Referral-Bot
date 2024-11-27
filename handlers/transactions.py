from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from models.user import Transaction
from services.user import get_user,check_address

router = Router()

class SendCoin(StatesGroup):
    address = State()
    amount = State()


@router.message(F.text == "Send Coin")
async def send_coin(message: Message, state: FSMContext):
    await state.set_state(SendCoin.address)
    await message.answer("Referral address")

@router.message(SendCoin.address)
async def get_addr(msg: Message, state: FSMContext):
    await state.update_data(address=msg.text)
    await state.set_state(SendCoin.amount)
    await msg.answer("Jo'natmoqchi bo'lgan coin sonini kiriting: ")

@router.message(SendCoin.amount)
async def get_amount(msg: Message, state: FSMContext):
    await state.update_data(amount=msg.text)

    data = await state.get_data()
    print(data)
    address = data['address']
    amount = data['amount']
    print(address, amount)
    user = await get_user(msg.from_user.id)
    addr = await check_address(address)
    if addr:
        await msg.answer(f'user topildi')
        transaction = await Transaction.create_transaction(sender=user, receiver=addr, amount=int(amount), note="Gift")
    else:
        await msg.answer("Wrong address")
