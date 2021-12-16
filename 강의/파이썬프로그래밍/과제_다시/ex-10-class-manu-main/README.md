# Exercise 10. 클래스 작성 및 예외처리 - 메뉴

이번 과제는 클래스 `Menu`를 작성하는 것입니다. 이 클래스로 생성한 메뉴 인스턴스는 음식 이름을 추가하고, 현재 메뉴에 등록되어 있는 음식 이름들을 출력하는 등의 기능을 가지고 있습니다. 이와 같은 메뉴의 기능을 수행하기 위해 이 클래스는 아래와 같은 함수들로 구성되어 있습니다.

- `__init__(self)`
  - 클래스를 초기화 하기 위한 함수입니다. 메뉴 인스턴스를 만들면 `self.meals`라는 속성에 빈 리스트를 할당합니다. 이 속성에 음식 이름을 담을 예정입니다.

- `add_meal(self, meal)`
  - 메뉴에 음식 이름을 등록하기 위한 함수입니다. 문자열 형태의 음식 이름은 `meal` 인자로 받습니다. 

- `print_menu(self)`
  - 현재 메뉴에 등록되어 있는 음식 이름들을 하나씩 화면에 출력합니다.

- `get_meal(self, idx)`
  - `idx` 인자는 `integer`입니다. 이 함수는 `idx`를 받아 현재 메뉴에 `list` 형태로 등록되어 있는 음식 이름들 중에서 해당 offset에 위치하는 음식 이름을 화면에 출력합니다.
  -  이 함수는 아래의 예외 상황들을 처리할 수 있도록 구현되어야 합니다.
     -  `idx`가 `integer`가 아닌 `float` 혹은 `str` 등의 잘못된 타입을 가지는 경우는 화면에 `Index should be an integer.`라는 안내 문구를 출력합니다.
     -  `idx`에 해당되는 음식이 존재하지 않는 경우는 화면에 `This meal does not exist.`라는 안내 문구를 화면에 출력합니다.

- `clear_menu(self)`
  - 이 함수는 현재 메뉴에 등록되어 있는 모든 음식 이름들을 지웁니다.

위와 같은 기능을 가지는 `Menu` 클래스를 작성하는 것이 이번 과제의 목표입니다. 제대로 작성된 `Menu` 클래스의 실행 예시들은 아래와 같습니다. 직접 테스트해보기 바랍니다.

```vim
>>> menu = Menu()
>>> menu.add_meal("Burger")
>>> menu.add_meal("Pizza")
>>> menu.add_meal("Chicken")
>>> menu.print_menu()
Burger
Pizza
Chicken
>>> menu.get_meal(1)
Pizza
>>> menu.get_meal("Burger")
Index should be an integer.
>>> menu.get_meal(0.8)
Index should be an integer.
>>> menu.get_meal(5)
This meal does not exist.
>>> menu.clear_menu()
>>> menu.add_meal("Kimchi")
>>> menu.print_menu()
Kimchi
```
