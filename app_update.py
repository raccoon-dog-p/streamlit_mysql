import mysql.connector
import streamlit as st
from mysql.connector.errors import Error
from mysql_connection import get_connection
# 1. db에 연결
def run_update_app():
    st.subheader('아이디로,나이를 업데이트')
    id=st.number_input('아이디입력',min_value=0)
    age = st.number_input('나이입력',min_value=0)
    if st.button('저장하기'):
        try :
            connection = get_connection()
            
            query = ''' update test_user
                        set age = %s
                        where id = %s;
            '''
            # 파이썬에서 튜플만들때 데이터가 1개인 경우는 , 를 넣고 써주자
            record =(age,id) 


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