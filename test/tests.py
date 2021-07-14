import cv2
import unittest
import db_actions
import datetime


def capture_works():  

    cap = cv2.VideoCapture(0)
    is_open = cap.isOpened()
    cap.release()

    print("capture open:", is_open)


def test_local_db():

    print("set up local connection")
    con, cur = db_actions.set_up_local_db()

    print("insert {} {}". format("ok", datetime.datetime.now()))
    db_actions.insert_local(con, cur, "ok", datetime.datetime.now())

    print("print out last element from db")
    data = db_actions.retrieve_db_res(save_as_csv=False)
    print(data[-1])

    print("remove the last element")
    db_actions.remove_last_element_and_close(con)

def test_aws_db():

    print("set up aws connection")
    con, cur = db_actions.set_up_aws_db()

    print("insert {} {}". format("ok", datetime.datetime.now()))
    db_actions.insert_aws(con, cur, "ok", datetime.datetime.now())

    print("print out last element from db")
    data = db_actions.retrieve_db_res(save_as_csv=False, aws=True)
    print(data[-1])

    print("remove the last element")
    db_actions.remove_last_element_and_close(con)