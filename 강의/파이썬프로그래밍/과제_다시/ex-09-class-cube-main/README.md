# Exercise 09. 클래스 작성 - 정육면체

이번 과제는 정육면체 인스턴스를 만들기 위한 틀, 즉 클래스 `Cube`를 작성하는 것입니다.

- 작성된 클래스를 이용하여 특정한 변의 길이를 가지는 직육면체 인스턴스를 아래와 같이 생성할 수 있어야 합니다. `Cube` 클래스의 초기화 함수 `__init__`은 변의 길이 `edge_length`만을 인자로 받습니다.
  ```python
  >>> cube1 = Cube(edge_length=4)
  ```

- 생성된 직육면체 인스턴스는 아래와 같은 예시를 통해 그 부피를 알 수 있습니다. `volumn`의 호출 방식을 보면 함수라는 것을 알 수 있습니다.
  ```python
  >>> print(cube1.volume())
  64
  ```
- 또한, 생성된 인스턴스를 `print` 함수에 넘겨주면 아래와 같은 정보가 출력됩니다.
  ```python
  >>> print(cube1)
  Edge Length: 4, Volume: 64
  ```
위와 같은 방식으로 활용할 수 있는 `Cube` 클래스를 작성하는 것이 이번 과제입니다. 클래스가 필요로 하는 속성, 함수들을 스스로 정의해서 구현해보기 바랍니다.

추가적인 활용 예시는 아래와 같습니다.
```python
>>> small_cube = Cube(2)
>>> print(small_cube)
Edge Length: 2, Volume: 8
>>> print(small_cube.volume())
8
>>> big_cube = Cube(10)
>>> print(big_cube.volume())
1000
>>> print(big_cube)
Edge Length: 10, Volume: 1000
```