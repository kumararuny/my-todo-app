import streamlit as st
import functions1

todos = functions1.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions1.write_todos(todos)
    st.session_state['new_todo'] = ''



todos = [t for t in todos if t != '\n']

len(todos)
st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to imporve your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key= todo)
    if checkbox:
        todos.pop(index)
        functions1.write_todos(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label='', placeholder='Add new todo...',on_change=add_todo,
              key='new_todo')





