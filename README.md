# Лабораторная работа №1 - Калькулятор M1
Реализация калькулятора математических выражений методом рекурсивного спуска.

## Функциональность
- Базовые операции: `+`, `-`, `*`, `/`
- Специальные операции: `//`, `%`, `**`
- Скобки: `(`, `)`
- Унарные плюс и минус
- Вещественные и целые числа
- Право-ассоциативное возведение в степень
- Обработка ошибок

## Установка и запуск
git clone https://github.com/alexssokolov007-oss/lab1-calculator-m1
cd lab1-calculator-m1

python -m venv .venv
source .venv/bin/activate or for W .venv\Scripts\activate

pip install -r requirements.txt

python main.py

## Структура проекта
├── src                                                                                                                                        
│   ├── init.py                                                                                                                                
│   ├── calculator.py                                                                                                                        
│   ├── constants.py                                                                                                                           
│   └── main.py                                                                                                                                
│                                                                                                                                              
├── tests                                                                                                                                      
│   ├── init.py                                                                                                                                
│   ├── test_calculator.py                                                                                                                     
│   └── test_main.py                                                                                                                           
│                                                                                                                                              
├── .gitignore                                                                                                                                 
├── .pre-commit-config.yaml                                                                                                                    
├── README.md                                                                                                                                  
├── pyproject.toml                                                                                                                             
├── requirements.txt                                                                                                                           
└── uv.lock                                                                                                                                    
