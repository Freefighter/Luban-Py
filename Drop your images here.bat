@echo off
:again
python compress.py "%~1"
shift
REM ��n�����ֵΪ0,1�򲻴����κ�����ѡ�� ��shiftʱ�����ʾ�������ļ����滻��������һ��λ�ã�������滻����½�����ȥ
if "%~1" neq "" goto again
pause