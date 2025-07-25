
import streamlit as st
import functions

todos = functions.get_tasks()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_tasks(todos)


st.title("My Todo App")

st.subheader("Keep your shit together!")

for index, task in enumerate(todos):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        todos.pop(index)
        functions.write_tasks(todos)
        del st.session_state[task]
        st.rerun()
    
st.text_input(label="", placeholder="Add a Todo..", on_change=add_todo, key='new_todo')

# st.session_state