# states.py
user_states = {}
creation_temp = {}
# 添加状态
def set_state(user_id: str, state: str):
    user_states[user_id] = state
# 获取状态
def get_state(user_id: str):
    return user_states.get(user_id)
# 删除状态
def clear_state(user_id: str):
    user_states.pop(user_id, None)
    creation_temp.pop(user_id, None)
# 临时数据
def set_temp(user_id: str, key: str, value):
    if user_id not in creation_temp:
        creation_temp[user_id] = {}
    creation_temp[user_id][key] = value
# 获取临时数据
def get_temp(user_id: str, key: str, default=None):
    return creation_temp.get(user_id, {}).get(key, default)
# 删除临时数据
def clear_temp(user_id: str):
    creation_temp.pop(user_id, None)