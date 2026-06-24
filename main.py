import logging

from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star
from astrbot.core.star.filter.event_message_type import EventMessageType
from .states import set_state, get_state, clear_state, set_temp, get_temp, clear_temp


class QiuXian(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    @filter.command("踏上仙途")
    async def createUser(self, event: AstrMessageEvent):
        user_name = event.get_sender_name()
        message_str = event.message_str # 获取消息的纯文本内容
        group_id = event.get_group_id()
        set_state(event.get_sender_id(), "setUserName")
        set_temp(event.get_sender_id(), "group_id", group_id)
        logging.info(f"用户: {user_name}，群组: {group_id}","触发创建角色命令")
        yield event.plain_result(f"玩家: {user_name}，请输入您的角色名称：") # 发送一条纯文本消息

    @filter.event_message_type(EventMessageType.ALL)
    async def  handle_user_messages(self, event: AstrMessageEvent):
        if get_state(event.get_sender_id()) == "setUserName":
            clear_state(event.get_sender_id())
            yield event.plain_result(f"玩家: {event.get_sender_name()}，角色名称: {event.message_str}，请输入您的性别：")
