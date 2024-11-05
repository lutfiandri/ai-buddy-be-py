from langchain_core.messages import SystemMessage, AIMessage, HumanMessage, BaseMessage
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_postgres import PostgresChatMessageHistory
from psycopg import Connection


def chat_to_ai(conn: Connection, model: BaseChatModel, session_id: str, chat: str) -> BaseMessage:
    history = PostgresChatMessageHistory(
        "chat_history",
        session_id,
        sync_connection=conn
    )

    history.add_message(HumanMessage(chat))
    ai_chat = model.invoke(history.get_messages())

    history.add_message(ai_chat)

    return ai_chat
