import streamlit as st
import todo_functions


todos = todo_functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    todo_functions.write_todos(todos)


st.title("Simple Todo App")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        todo_functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a Todo", placeholder="Add a Todo here..",
              on_change=add_todo, key= 'new_todo')


