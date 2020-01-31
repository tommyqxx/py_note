{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "first_module.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMHiM3mE/LLcgRFmxot4QMo",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/tommyqxx/py_note/blob/master/first_module_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AM2ZhMNhdkv4",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# 模块  就是一个.py文件\n",
        "\n",
        "__all__=[\"g_num\",\"show\"]\n",
        "\n",
        "# 全局变量\n",
        "g_num = 10\n",
        "\n",
        "# 定义一个函数\n",
        "def show():\n",
        "  print(\"我是一个函数\")\n",
        "\n",
        "# 定义一个类\n",
        "class Student(object):\n",
        "  def __init__(self,name,age):\n",
        "    self.name=name\n",
        "    self.age=age\n",
        "  def show_msg(self):\n",
        "    print(self.name,self.age)"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}