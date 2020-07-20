import datetime
import decimal
import json
import tarfile
import re
import io

import shortuuid
from flask import jsonify


def utcnow():
    return datetime.datetime.utcnow()


def now():
    return datetime.datetime.now()


def parse_constant(v):
    '''replace nan into None when using json.load/loads '''
    if v in ['NaN', '-Infinity', 'Infinity']:
        return None
    return v


def ok_jsonify(data=None):
    return jsonify({'ok': True, 'data': data or {}})


def fail_jsonify(reason, data=None):
    return jsonify({'ok': False, 'data': data or {}, 'reason': reason})


def validate_email(address):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", address) is not None


def safe_int(v, default=0):
    try:
        return int(v)
    except (TypeError, ValueError) as e:
        return default


def camelcase_to_underscore(s):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def random_string(length=10):
    return shortuuid.random(length)


def decompress_file(fname):
    '''解压缩文件'''
    if fname.endswith("tar.gz"):
        tar = tarfile.open(fname, "r:gz")
        tar.extractall()
        tar.close()
    elif fname.endswith("tar"):
        tar = tarfile.open(fname, "r:")
        tar.extractall()
        tar.close()


def compress_file(uncompress_path, compress_path):
    '''压缩文件'''
    tar = tarfile.open(compress_path, "w:gz")
    tar.add(uncompress_path)
    tar.close()


def create_csv_file(df):
    '''将DataFrame转换为file-object 对象'''
    buf = io.StringIO()
    df.to_csv(buf)
    buf.seek(0)
    return buf


def check_file_suffix(fname, accept_suffix=['.csv', '.xls', '.xlsx']):
    '''检查文件 格式是否符合要求'''
    for item in accept_suffix:
        if fname.endswith(item):
            return True
    return False
