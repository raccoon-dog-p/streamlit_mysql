import streamlit as st
from app_delete import run_delete_app
from app_insert import run_insert_app

from app_selcet import run_app_selcet
from app_update import run_update_app

def main():
    # CRUD 라고 한다
    # Create, Read , Update , Delete
    menu = ['insert','select','update','delete']
    choice = st.sidebar.selectbox('회원가입',menu)
    if choice == 'insert':
        run_insert_app()
    elif choice == 'select':
        run_app_selcet()
    elif choice == 'update':
        run_update_app()
    elif choice == 'delete':
        run_delete_app()
if __name__ == '__main__' :
    main()