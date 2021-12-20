import streamlit as st
import mysql.connector
from mysql.connector.errors import Error

from mysql_connection import get_connection
def run_app_selcet():
        try :
            st.subheader('전체조회')
            connection = get_connection()


            query= ''' select * 
                    from test_user;
            '''

            cursor = connection.cursor(dictionary=True)

            cursor.execute(query)

            # select 문은 아래 내용이 필요하다
            record_list = cursor.fetchall()
            print(record_list)
            for row in record_list:
                st.write(row)
            
            st.subheader('아이디로 조회')
            id = st.number_input('아이디입력',min_value=1)

            query= ''' select * 
                    from test_user
                    where id = %s;
            '''
            record=(id,)

            cursor.execute(query,record)

            record_list = cursor.fetchall()
            print(record_list)
            for row in record_list:
                st.write(row)
            
            # 검색
            st.subheader('검색')
            search_word = '%'+st.text_input('검색어입력')+'%'
            if st.button('검색하기!'):
                query = '''select *
                           from test_user
                           where email like %s ;'''
                record = (search_word,)

                cursor.execute(query,record)

                record_list = cursor.fetchall()
                print(record_list)
                for row in record_list:
                    st.write(row)



        # 위의 코드를 실행하다가, 문제가 생기면, except를 실행하라는 뜻.     
        except Error as e :
            print('Error while connecting to MySQL',e)
        # finally는 try에서 에러가 나든 안나든, 무조건 실행하라는 뜻.
        finally :
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('MySQL connection is closed')
            else :
                print('connection does not exist')


            