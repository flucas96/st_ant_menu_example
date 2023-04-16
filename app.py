import streamlit  as st

from st_ant_menu import st_ant_menu


st.set_page_config(layout="wide")


#Das parsen von der Menüstruktur funktioniert noch nicht  - es wird das beispiel direkt aus der .tsx Datei genommen
MenuItems = [
  {
    "label": "Navigation One",
    "key": "sub1",
    "icon": "FastBackwardOutlined",
    "type": "group",
    "children": [
      {
        "label": "Option 1",
        "key": "1"
      },
      {
        "label": "Option 2",
        "key": "2"
      },
      {
        "label": "Option 3",
        "key": "3"
      },
      {
        "label": "Option 4",
        "key": "4"
      }
    ]
  },
  {
    "label": "Navigation Two",
    "key": "sub2",
    "icon": "AppstoreOutlined",
    "type": "group",
    "children": [
      {
        "label": "Option 5",
        "key": "5"
      },
      {
        "label": "Option 6",
        "key": "6"
      },
    ]
  },
  {
    "label": "Navigation Three",
    "key": "sub4",
    "icon": "SettingOutlined",
    "type": "group",
    "children": [
      {
        "label": "Option 9",
        "key": "9"
      },
      {
        "label": "Option 10",
        "key": "10"
      },
      {
        "label": "Option 11",
        "key": "11"
      },
      {
        "label": "Option 12",
        "key": "12"
      }
    ]
  }
]



with st.sidebar:
  st.write("Test")
  selected = st_ant_menu(menu_data=MenuItems,multiple=False)

  st.write("Test")

st.write("Selected: ", selected)


st.code("""

MenuItems = [
  {
    "label": "Navigation One",
    "key": "sub1",
    "icon": "FastBackwardOutlined",
    "type": "group",
    "children": [
      {
        "label": "Option 1",
        "key": "1"
      },
      {
        "label": "Option 2",
        "key": "2"
      },
      {
        "label": "Option 3",
        "key": "3"
      },
      {
        "label": "Option 4",
        "key": "4"
      }
    ]
  },
  {
    "label": "Navigation Two",
    "key": "sub2",
    "icon": "AppstoreOutlined",
    "type": "group",
    "children": [
      {
        "label": "Option 5",
        "key": "5"
      },
      {
        "label": "Option 6",
        "key": "6"
      },
    ]
  },
  {
    "label": "Navigation Three",
    "key": "sub4",
    "icon": "SettingOutlined",
    "type": "group",
    "children": [
      {
        "label": "Option 9",
        "key": "9"
      },
      {
        "label": "Option 10",
        "key": "10"
      },
      {
        "label": "Option 11",
        "key": "11"
      },
      {
        "label": "Option 12",
        "key": "12"
      }
    ]
  }
]



with st.sidebar:
  st.write("Test")
  selected = st_ant_menu(menu_data=MenuItems,multiple=False)

  st.write("Test")

st.write("Selected: ", selected)
""", language="python")