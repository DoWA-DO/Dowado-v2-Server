"""
생명주기 이벤트 확장 모듈
"""
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.database.session import rdb
from src.config import load_model
import logging


_logger = logging.getLogger(__name__)



def use(app: FastAPI):
    """ 이벤트 확장 모듈 """
    
    @app.on_event("startup")
    async def startup_event():
        '''
        서버 시작 이벤트 처리 함수
        '''
        _logger.info('=>> 서버 시작 이벤트 호출')
        await rdb.create_tables()
        load_model()
        
    
    @app.on_event("shutdown")
    async def shutdown_event():
        '''
        서버 종료 이벤트 처리 함수
        '''
        _logger.info('=>> 서버 종료 이벤트 실행')
        await rdb.dispose_engine()
        