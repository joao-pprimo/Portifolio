{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6f23488b",
   "metadata": {},
   "source": [
    "# Trabalhando com Dicionários"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c9ae6794",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Isso é uma lista\n",
    "estudantes_lst = ['Pedro', 24, 'Ana', 22, 'Ronaldo', 26, \"Janaina\", 25]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2583ab39",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Pedro', 24, 'Ana', 22, 'Ronaldo', 26, 'Janaina', 25]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estudantes_lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4a87d3e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(estudantes_lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ef751581",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Isso é um dicionário\n",
    "estudantes_dict = {'Pedro':24, 'Ana':22, 'Ronaldo':26, 'Janaina':25}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c8226202",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Pedro': 24, 'Ana': 22, 'Ronaldo': 26, 'Janaina': 25}"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estudantes_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3c173c4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(estudantes_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b042bf61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estudantes_dict ['Pedro']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c4f3e199",
   "metadata": {},
   "outputs": [],
   "source": [
    "estudantes_dict ['Marcelo'] = 23"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "56f98f19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "23"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estudantes_dict ['Marcelo']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "de38b000",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Pedro': 24, 'Ana': 22, 'Ronaldo': 26, 'Janaina': 25, 'Marcelo': 23}"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estudantes_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f9e2cec5",
   "metadata": {},
   "outputs": [],
   "source": [
    "estudantes_dict.clear()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a6954f92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estudantes_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "dd6350a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "del estudantes_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "bb52b9e5",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'estudantes_dict' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_12948\\1634695477.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mestudantes_dict\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'estudantes_dict' is not defined"
     ]
    }
   ],
   "source": [
    "estudantes_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "e79421a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "estudantes = {'Pedro':24, 'Ana':22, 'Ronaldo':26, 'Janaina':25}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f08d088",
   "metadata": {},
   "outputs": [],
   "source": [
    "estudantes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "858203ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Pedro': 24, 'Ana': 22, 'Ronaldo': 26, 'Janaina': 25}"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estudantes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5fe91b30",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(estudantes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c071151b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['Pedro', 'Ana', 'Ronaldo', 'Janaina'])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estudantes.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "651b03da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values([24, 22, 26, 25])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estudantes.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "cd587ded",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_items([('Pedro', 24), ('Ana', 22), ('Ronaldo', 26), ('Janaina', 25)])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estudantes.items()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "18c394fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "estudantes2 = {'Camila':27, 'Adriana':28, 'Roberta':26}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "3b403981",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Camila': 27, 'Adriana': 28, 'Roberta': 26}"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estudantes2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5095be21",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'dict' object has no attribute 'uptade'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_12948\\4200313175.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mestudantes\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0muptade\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mestudantes2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m: 'dict' object has no attribute 'uptade'"
     ]
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "29259278",
   "metadata": {},
   "outputs": [],
   "source": [
    "estudantes.update(estudantes2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "71381eb9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Pedro': 24,\n",
       " 'Ana': 22,\n",
       " 'Ronaldo': 26,\n",
       " 'Janaina': 25,\n",
       " 'Camila': 27,\n",
       " 'Adriana': 28,\n",
       " 'Roberta': 26}"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estudantes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "9a50de4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "9b68d06e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{}"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "db6152c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict['chave_um'] = 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "906c424a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'chave_um': 2}\n"
     ]
    }
   ],
   "source": [
    "print(dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "e2aa89e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict[10] = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "e1d8f72f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'chave_um': 2, 10: 5}"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "32d69c39",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict[9.3] = 'Python'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "e2370cae",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict[\"teste\"] = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "9c1678da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'chave_um': 2, 10: 5, 9.3: 'Python', 'teste': 5}"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "57bd3854",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict1 = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "1bc73f99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{}"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "abc2b71f",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict1['teste'] = 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "94f18df5",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict1['key'] = \"teste\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "762d1c0a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'teste': 10, 'key': 'teste'}"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Atenção, pois chave e valor podem ser iguais, mas representam coisas diferentes.\n",
    "dict1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "0fa1d56f",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict2 = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "7d984f07",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict2['key1'] = \"Data Science\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "3bfbebda",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict2['key2'] = 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "166f3529",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict2['key3'] = 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "edd614c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'key1': 'Data Science', 'key2': 10, 'key3': 100}"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "89c212ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = dict2['key1']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "13cfce90",
   "metadata": {},
   "outputs": [],
   "source": [
    "b = dict2['key2']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "0ec3bc98",
   "metadata": {},
   "outputs": [],
   "source": [
    "c = dict2['key3']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "eaa2a284",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('Data Science', 10, 100)"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a, b, c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "666aa127",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dicionário de listas\n",
    "dict3 = {'chave1':1230, 'chave2':[22,453,73.4], 'chave3':['picanha', 'fraldinha', 'alcatra']}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "8c9bfeb9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'chave1': 1230,\n",
       " 'chave2': [22, 453, 73.4],\n",
       " 'chave3': ['picanha', 'fraldinha', 'alcatra']}"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "ed11de12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[22, 453, 73.4]"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict3[\"chave2\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "243d3750",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'PICANHA'"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Acessando um item de lista, dentro do dicionário\n",
    "dict3['chave3'][0].upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "767fd092",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Operações com itens da lista, dentro do dicionário\n",
    "var1 = dict3['chave2'][0] - 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "b5d9e362",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "var1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "a8e1e08c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Duas operações no mesmo comando, para atualizar um item dentro da lista\n",
    "dict3['chave2'][0] -=2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "12ce0870",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'chave1': 1230,\n",
       " 'chave2': [20, 453, 73.4],\n",
       " 'chave3': ['picanha', 'fraldinha', 'alcatra']}"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict3"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "02acc452",
   "metadata": {},
   "source": [
    "# Criando Dicionários Aninhandos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "f62e3ba6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Criando dicionários aninhados\n",
    "dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em Python'}}}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "eabb215c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'key1': {'key2_aninhada': {'key3_aninhada': 'Dict aninhado em Python'}}}"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict_aninhado"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "a6c8a701",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Dict aninhado em Python'"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict_aninhado['key1']['key2_aninhada']['key3_aninhada']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b367e4ad",
   "metadata": {},
   "source": [
    "# Fim"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
