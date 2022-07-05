#import json



from jinja2 import Environment, FileSystemLoader, select_autoescape

#with open("example.json", "r", encoding="utf-8") as fh:
    #data = json.load(fh)

env = Environment( #
    loader=FileSystemLoader('.'), # тут говорится о том, что файл шаблона template.html нужно искать в том же каталоге, где лежит скрипт main.py.
    autoescape=select_autoescape(['html', 'xml']) # это стандартные настройки для работы с HTML.
)

template = env.get_template('sko_result.html') # в переменную template загружается шаблон из файла template.html.


results = {
  "atthenuator": {
    "10": {
      "IF": {
        "300": {
          "trace": {
            "absolute": {
              "max_value": 3.14121e-05,
              "T11": 1.90724e-05,
              "R11": 1.09096e-05,
              "T22": 3.14121e-05,
              "R22": 1.06336e-05,
              "T33": 1.74005e-05,
              "R33": 1.06695e-05,
              "T44": 1.89555e-05,
              "R44": 1.08017e-05,
              "T55": 1.53274e-05,
              "R55": 1.10745e-05,
              "T66": 2.9731e-05
            },
            "otnosit": {
              "max_value": 3.26458e-05,
              "S11": 2.20791e-05,
              "S22": 3.26458e-05,
              "S33": 2.05612e-05,
              "S44": 2.24158e-05,
              "S55": 1.88255e-05
            }
          }
        },
        "30": {
          "trace": {
            "absolute": {
              "max_value": 3.14121e-05,
              "T11": 1.90724e-05,
              "R11": 1.09096e-05,
              "T22": 3.14121e-05,
              "R22": 1.06336e-05,
              "T33": 1.74005e-05,
              "R33": 1.06695e-05,
              "T44": 1.89555e-05,
              "R44": 1.08017e-05,
              "T55": 1.53274e-05,
              "R55": 1.10745e-05,
              "T66": 2.9731e-05
            },
            "otnosit": {
              "max_value": 3.26458e-05,
              "S11": 2.20791e-05,
              "S22": 3.26458e-05,
              "S33": 2.05612e-05,
              "S44": 2.24158e-05,
              "S55": 1.88255e-05
            }
          }
        }
      }
    },
    "30": {
      "IF": {
        "300": {
          "trace": {
            "absolute": {
              "max_value": 3.14121e-05,
              "T11": 1.90724e-05,
              "R11": 1.09096e-05,
              "T22": 3.14121e-05,
              "R22": 1.06336e-05,
              "T33": 1.74005e-05,
              "R33": 1.06695e-05,
              "T44": 1.89555e-05,
              "R44": 1.08017e-05,
              "T55": 1.53274e-05,
              "R55": 1.10745e-05,
              "T66": 2.9731e-05
            },
            "otnosit": {
              "max_value": 3.26458e-05,
              "S11": 2.20791e-05,
              "S22": 3.26458e-05,
              "S33": 2.05612e-05,
              "S44": 2.24158e-05,
              "S55": 1.88255e-05
            }
          }
        },
        "30": {
          "trace": {
            "absolute": {
              "max_value": 3.14121e-05,
              "T11": 1.90724e-05,
              "R11": 1.09096e-05,
              "T22": 3.14121e-05,
              "R22": 1.06336e-05,
              "T33": 1.74005e-05,
              "R33": 1.06695e-05,
              "T44": 1.89555e-05,
              "R44": 1.08017e-05,
              "T55": 1.53274e-05,
              "R55": 1.10745e-05,
              "T66": 2.9731e-05
            },
            "otnosit": {
              "max_value": 3.26458e-05,
              "S11": 2.20791e-05,
              "S22": 3.26458e-05,
              "S33": 2.05612e-05,
              "S44": 2.24158e-05,
              "S55": 1.88255e-05
            }
          }
        }
      }
    },
    "50": {
      "IF": {
        "300": {
          "trace": {
            "absolute": {
              "max_value": 3.14121e-05,
              "T11": 1.90724e-05,
              "R11": 1.09096e-05,
              "T22": 3.14121e-05,
              "R22": 1.06336e-05,
              "T33": 1.74005e-05,
              "R33": 1.06695e-05,
              "T44": 1.89555e-05,
              "R44": 1.08017e-05,
              "T55": 1.53274e-05,
              "R55": 1.10745e-05,
              "T66": 2.9731e-05
            },
            "otnosit": {
              "max_value": 3.26458e-05,
              "S11": 2.20791e-05,
              "S22": 3.26458e-05,
              "S33": 2.05612e-05,
              "S44": 2.24158e-05,
              "S55": 1.88255e-05
            }
          }
        },
        "30": {
          "trace": {
            "absolute": {
              "max_value": 3.14121e-05,
              "T11": 1.90724e-05,
              "R11": 1.09096e-05,
              "T22": 3.14121e-05,
              "R22": 1.06336e-05,
              "T33": 1.74005e-05,
              "R33": 1.06695e-05,
              "T44": 1.89555e-05,
              "R44": 1.08017e-05,
              "T55": 1.53274e-05,
              "R55": 1.10745e-05,
              "T66": 2.9731e-05
            },
            "otnosit": {
              "max_value": 3.26458e-05,
              "S11": 2.20791e-05,
              "S22": 3.26458e-05,
              "S33": 2.05612e-05,
              "S44": 2.24158e-05,
              "S55": 1.88255e-05
            }
          }
        }
      }
    }
  }
}



rendered_page = template.render(results=results)


#и не забыть что если значение больше допуска, то ячейка помечается желтым цветом
# <td style = "background-color: #ffff00">
with open('index4.html', 'w', encoding="utf8") as file: # Далее строка с HTML сохраняется в файл с именем index.html:
    file.write(rendered_page)
