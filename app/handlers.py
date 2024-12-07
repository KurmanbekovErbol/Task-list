
from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from aiogram import Router
from app.db import *

router=Router()

@router.message(CommandStart())
async def command_start(message: types.Message):
    register(message.from_user.id, message.from_user.full_name)
    await message.answer(f'Привет {message.from_user.first_name}', reply_markup=keyboard)

class TASK(StatesGroup):
      Task_Add = State()

@router.message(F.text=='Добавить задачу')
async def task_add(message: types.Message, state: FSMContext):
    await message.reply('Введите содержание задачи:')
    await state.set_state(TASK.Task_Add)

@router.message(TASK.Task_Add)
async def save_task(message: types.Message, state: FSMContext):
        await state.update_data(Task_Add = message.text)
        data = await state.get_data()
        Task_Add = data['Task_Add']
        add_task(message.from_user.id, Task_Add)
        await state.clear()
        await message.answer("Задача добавлена!", reply_markup=keyboard)

@router.message(F.text=="Показать задачи")
async def show_tasks(message: types.Message):
        tasks = get_tasks(message.from_user.id)
        if tasks:
            await message.answer("Ваши задачи:", reply_markup=await tasks_buttons(message.from_user.id))
            await message.answer("Выберите кнопку", reply_markup=keyboard)
        else:
            await message.answer("Список задач пуст.", reply_markup=keyboard)


@router.message(F.text=="Очистить список")
async def confirm_clear_list(message: types.Message):
        await message.answer("Вы уверены?", reply_markup=inline_keyboard)

@router.callback_query(F.data=="confirm_clear")
async def clear_tasks(callback: types.CallbackQuery):
        delete_all_tasks(callback.from_user.id)
        await callback.message.answer("Список задач очищен.", reply_markup=keyboard)

@router.callback_query(F.data=="cancel_clear")
async def cancel_clear(callback: types.CallbackQuery):
        await callback.message.answer("Очистка отменена.", reply_markup=keyboard)