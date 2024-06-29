''' Test Pretalx '''
import logging

import pytest

from toldwords.pretalx import Pretalx

logging.basicConfig(
    filename='test.log',
    filemode='w',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s: %(message)s',
)


@pytest.fixture
def auth_info():
    ''' Get login info '''
    return Pretalx(domain='pretalx.coscup.org', event='coscup-2024',
                   token='')


class TestPretalx:
    ''' Test Pretalx '''

    @staticmethod
    def test_fetch_all(auth_info):
        ''' Test fetch all '''
        pretalx = auth_info

        datas = list(pretalx.submissions())

        logging.info(datas)
        logging.info(len(datas))

    @staticmethod
    def test_rooms(auth_info):
        ''' Test rooms '''
        pretalx = auth_info

        datas = list(pretalx.rooms())

        logging.info(datas)
        logging.info(len(datas))

    @staticmethod
    def test_speakers(auth_info):
        ''' Test speakers '''
        pretalx = auth_info

        datas = list(pretalx.speakers())

        logging.info(datas)
        logging.info(len(datas))

    @staticmethod
    def test_talks(auth_info):
        ''' Test talks'''
        pretalx = auth_info

        datas = list(pretalx.talks())

        logging.info(datas)
        logging.info(len(datas))
