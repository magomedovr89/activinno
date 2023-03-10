from aiogram import types, Bot, executor, Dispatcher
from aiogram.types import ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
from database import *
import os
import functions
import Buttons

bot = Bot(token=os.environ['Spaceship_Telegram'])
storage = MemoryStorage()  # Хранилище
dp = Dispatcher(
    bot,
    storage=storage
)


"""Это код телеграм-бота для решения задачи про космический корабль"""


# Класс состояний
class ClientStatesGroup(StatesGroup):
    phase1 = State()
    phase2 = State()
    phase3 = State()
    phase4 = State()
    phase5 = State()
    phase6 = State()


@dp.message_handler(commands=['start'], state='*')  # Обработка команды старт
async def cmd_start(message: types.Message, state: FSMContext):
    sql.execute("SELECT id FROM base")  # Выбор id в базе данных
    await state.set_state(None)  # Установка состояния на None
    if message.from_user.id not in [user[0] for user in sql.fetchall()]:  # Проверка id в базе данных
        await bot.send_message(
            message.from_user.id,
            text=f'''Привет <strong>{message.from_user.first_name}</strong>!
Я -  программа, помогающая учёным рассчитывать значения, необходимые для посадки космического корабля на любую планету.
Для примера я могу показать значения для посадки корабля, массой 20тыс. кг., на луну, при начальной скорости - 20м/с и
конечной - 0.5м/с, находящегося на высоте 100м.

Для этого нажмите на кнопку <strong>"Стандартные значения"</strong>!
Для того что бы задать значения самому, нажмите на кнопку <strong>"Ввести значения"</strong>!''',
            parse_mode=ParseMode.HTML,
            reply_markup=Buttons.main())
        sql.execute("INSERT INTO base VALUES (?,?)", (message.from_user.id, message.from_user.username))
        db.commit()
    else:
        await bot.send_message(
            message.from_user.id,
            text=f'''Привет <strong>{message.from_user.first_name}</strong>!
Вижу что ты здесь не впервые!
Нажми на кнопку на кнопку <strong>"Стандартные значения"</strong> для решения со стандартными значениями!
Для того что бы задать значения самому, нажми на кнопку <strong>"Ввести значения"</strong>"!''',
            parse_mode=ParseMode.HTML,
            reply_markup=Buttons.main())


# Обработка callback'а 'cancel'
@dp.callback_query_handler(Text(equals="cancel", ignore_case=True), state='*')
async def call_cancel(call: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    async with state.proxy() as data:
        await bot.delete_message(chat_id=data['chat_id'], message_id=data['message_id'])
    await bot.send_message(chat_id=call.from_user.id, text='Я все отменил, пока!',
                           reply_markup=Buttons.main())
    return await state.finish()


# Обработка callback'а 'start'
@dp.callback_query_handler(Text(equals='start', ignore_case=True), state=None)
async def program_start(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['call'] = call
        data['message_id'] = data['call']['message']["message_id"]
        data['chat_id'] = call.from_user.id
    await ClientStatesGroup.phase1.set()
    await bot.edit_message_text(
        chat_id=data['chat_id'],
        message_id=data['message_id'],
        text=f'Начнем, введите введите высоту',
        reply_markup=Buttons.cancel_inl()
    )


# Обработка кнопки 'отмена', ее уже нет
@dp.message_handler(Text(equals='Отмена', ignore_case=True), state='*')
async def program_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.reply('Я все отменил, пока!',
                        reply_markup=Buttons.main())
    return await state.finish()


# получение h
@dp.message_handler(lambda message: message.text, content_types=['text'], state=ClientStatesGroup.phase1)
async def load_h(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:  # Хранилище для получения и сохранений значений
            data['h'] = float(message.text)
            # Редактирование сообщения
            await bot.edit_message_text(
                chat_id=data['chat_id'],
                message_id=data['message_id'],
                text=f'Высота: <strong>{data["h"]} м</strong>\nОтправь начальную скорость!',
                reply_markup=Buttons.cancel_inl(),
                parse_mode=ParseMode.HTML
            )
        # Удаление сообщения пользователя
        await ClientStatesGroup.next()
    except ValueError:  # Обработка ошибки
        pass
    finally:
        # Удаление сообщения пользователя
        await bot.delete_message(
            chat_id=message.from_user.id,
            message_id=message.message_id
        )


# Получение v1
@dp.message_handler(lambda message: message.text, content_types=['text'], state=ClientStatesGroup.phase2)
async def load_v_1(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['v_1'] = float(message.text)
            await bot.edit_message_text(
                chat_id=data['chat_id'],
                message_id=data['message_id'],
                text=f'Высота: <strong>{data["h"]} м</strong>\n'
                     f'Начальная скорость: <strong>{data["v_1"]} м/c</strong>\n'
                     f'А теперь отправь конечную скорость!',
                reply_markup=Buttons.cancel_inl(),
                parse_mode=ParseMode.HTML
            )
        await ClientStatesGroup.next()
    except ValueError:
        pass
    finally:
        await bot.delete_message(
            chat_id=message.from_user.id,
            message_id=message.message_id
        )


# Получение v2
@dp.message_handler(lambda message: message.text, content_types=['text'], state=ClientStatesGroup.phase3)
async def load_v_2(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['v_2'] = float(message.text)
            await bot.edit_message_text(
                chat_id=data['chat_id'],
                message_id=data['message_id'],
                text=f'Высота: <strong>{data["h"]} м</strong>\n'
                     f'Начальная скорость: <strong>{data["v_1"]} м/c</strong>\n'
                     f'Конечная скорость: <strong>{data["v_2"]} м/c</strong>\n'
                     f'Отправь массу корабля',
                reply_markup=Buttons.cancel_inl(),
                parse_mode=ParseMode.HTML
            )
        await ClientStatesGroup.next()
    except ValueError:
        pass
    finally:
        await bot.delete_message(
            chat_id=message.from_user.id,
            message_id=message.message_id
        )


# Получение m
@dp.message_handler(lambda message: message.text, content_types=['text'], state=ClientStatesGroup.phase4)
async def load_m(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['m'] = float(message.text)
            data['user_id'] = message.from_user.id  # Сохранение id
            await bot.edit_message_text(
                chat_id=data['chat_id'],
                message_id=data['message_id'],
                text=f'Высота: <strong>{data["h"]} м</strong>\n'
                     f'Начальная скорость: <strong>{data["v_1"]} м/c</strong>\n'
                     f'Конечная скорость: <strong>{data["v_2"]} м/c</strong>\n'
                     f'Масса корабля: <strong>{data["m"]} кг</strong>\n'
                     f'Выберете космическое тело',
                reply_markup=Buttons.set_keyboard(),
                parse_mode=ParseMode.HTML
            )
        await ClientStatesGroup.next()
    except ValueError:
        pass
    finally:
        await bot.delete_message(
            chat_id=message.from_user.id,
            message_id=message.message_id
        )


# Удаление сообщений при выборе кнопки
@dp.message_handler(state=ClientStatesGroup.phase5)
async def check_g(message: types.Message):
    return await bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id
    )


# Обработка callback'а "default" - 'Стандартные значения'
@dp.callback_query_handler(Text(equals="default", ignore_case=True))
async def callbacks_for_default(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['call'] = call
        data['message_id'] = data['call']['message']["message_id"]
        data['chat_id'] = call.from_user.id
        await bot.edit_message_text(
            chat_id=data['chat_id'],
            message_id=data['message_id'],
            text=f'''Ответ:
<strong>{functions.plane()} м/с^2</strong> - Ускорение при посадке.
<strong>{functions.time()} с</strong> - Время на изменение скорости.
<strong>{functions.engine()} Н</strong> - Тяга двигателей космического корабля.''',
            parse_mode=ParseMode.HTML,
            reply_markup=Buttons.values()
        )
    await call.answer()


# Обработка callback'а которые начинаются "planet"
@dp.callback_query_handler(Text(startswith="planet", ignore_case=True), state=ClientStatesGroup.phase5)
async def callbacks_planet(call: types.CallbackQuery, state: FSMContext):
    action = call.data[7::]

    if action == "sun":
        async with state.proxy() as data:
            data['g'] = 274

    elif action == "mars":
        async with state.proxy() as data:
            data['g'] = 3.7

    elif action == "Exisize moon-bot":
        async with state.proxy() as data:
            data['g'] = 1.63

    elif action == "mercury":
        async with state.proxy() as data:
            data['g'] = 3.7

    elif action == "earth":
        async with state.proxy() as data:
            data['g'] = 9.8

    elif action == "venus":
        async with state.proxy() as data:
            data['g'] = 8.87

    elif action == "jupiter":
        async with state.proxy() as data:
            data['g'] = 24.8

    elif action == "saturn":
        async with state.proxy() as data:
            data['g'] = 10.4

    elif action == "uranus":
        async with state.proxy() as data:
            data['g'] = 8.87

    elif action == "neptune":
        async with state.proxy() as data:
            data['g'] = 10.15

    elif action == "pluto":
        async with state.proxy() as data:
            data['g'] = 0.66

    await state.finish()
    await call.answer()
    await bot.delete_message(
        chat_id=data['chat_id'],
        message_id=data["message_id"])
    acceleration = functions.plane(
        data["h"],
        data["v_1"],
        data["v_2"]
    )
    await bot.send_message(
        chat_id=data['chat_id'],
        text='Ответ:\n'
        f'<strong>{functions.plane(data["h"], data["v_1"], data["v_2"])} '
        f'м/с^2</strong> - Ускорение при посадке.\n'
        f'<strong>{functions.time(data["v_1"], data["v_2"], acceleration=acceleration)}'
        f' с</strong> - Время на изменение скорости.\n'
        f'<strong>{functions.engine(data["m"], data["g"], acceleration=acceleration)} '
        f'Н</strong>'
        f' - Тяга двигателей космического корабля.',
        parse_mode=ParseMode.HTML,
        reply_markup=Buttons.main()
                           )


# Удаление всех лишних сообщений
@dp.message_handler(content_types=ContentType.ANY, state='*')
async def all_fix(message: types.Message):
    await bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id
    )


if __name__ == "__main__":
    executor.start_polling(dp)
