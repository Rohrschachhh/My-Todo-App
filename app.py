
import streamlit as st
import functions

todos = functions.get_tasks()

def add_todo():
    todo = st.session_state["new_todo"].strip()             
    if todo:
        todos.append(todo + "\n")
        functions.write_tasks(todos)
        # Clear the input
        st.session_state["new_todo"] = ""  

def finish_todo():
    tasks_to_keep = []
    
    for task in todos:
        key = f"checkbox_{task}"
        
        if not st.session_state.get(key, False):
            tasks_to_keep.append(task)
    
    functions.write_tasks(tasks_to_keep)
    
    """ Set a flag to trigger rerun outside the callback """
    st.session_state["tasks_updated"] = True
    st.rerun()

st.title("My Todo App")

st.subheader("Keep your shit together!")

# Add Todo Section 
st.text_input(label="", placeholder="Add a Todo..", key="new_todo")
st.button("Add to the queue", on_click=add_todo)

st.write("")

# Show Todos as checkboxes 
if todos:
    st.markdown("#### Please finish this first!")
    
    for task in todos:
        st.checkbox(task, key=f"checkbox_{task}")
    
    st.button("Finish Selected Task", on_click=finish_todo)
  
else:
    st.write("✅ All tasks are complete!")  

