import mysql.connector
import streamlit as st
from mysql.connector.errors import Error
from mysql_connection import get_connection

def run_delete_app():
    st.subheader('유저삭제')
    id= st.number_input('삭제할 id입력',min_value=1)
    if st.button('삭제'):
        try :
            connection = get_connection()

            query = '''delete from test_user
                    where id = %s;
            '''
            # 파이썬에서 튜플만들때 데이터가 1개인 경우는 , 를 넣고 써주자
            record = (id,)


            # 3. 커넥션으로 부터 커서를 가져온다.
            cursor = connection.cursor()

            # 4. 쿼리문을 커서에 넣어서 실행한다.
            cursor.execute(query,record)

            # 5. 커넥션을 커밋한다. db에 영구적으로 반영하라는 뜻
            connection.commit()
        except Error as e:
            print('Error ', e)

        finally :
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")