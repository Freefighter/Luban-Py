@echo off
:again
python compress.py "%~1"
shift
REM 当n赋予的值为0,1或不带有任何命令选项 的shift时，则表示批处理文件中替换参数左移一个位置，后面的替换参数陆续填补上去
if "%~1" neq "" goto again
pause