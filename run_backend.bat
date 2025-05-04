@echo off
cd /d E:\GF_AI_Advanced_Prompt_Engine\grafix_app
set PYTHONPATH=.
uvicorn backend.main:app --reload
pause
