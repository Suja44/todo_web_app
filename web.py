import streamlit as st
import func

todos=func.get_todos()


def add_todo():
    todo=st.session_state['new_todo']
    todos.append(todo+'\n')
    func.write_todos(todos)
    st.session_state['new_todo']=''
    # st.write(todo)


st.title("my todo app")
st.subheader("This app is to increase your productivity")

st.text_input(label="Enter",placeholder="Add new todo",key='new_todo',on_change=add_todo)
st.write("Todos:")


for index,todo in enumerate(todos):

   checkbox= st.checkbox(todo,key=todo)
   if checkbox==True:
       todos.pop(index)
       func.write_todos(todos)
       del st.session_state[todo]
       st.experimental_rerun()

# st.session_state