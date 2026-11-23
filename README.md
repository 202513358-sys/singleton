# singleton
언어 : python

실행 환경 : Windows 11, Github Actions, python 3.14.10

실행 방법 : 저장소에 변경 사항을 커밋하여 Github Actions가 python main.py를 자동으로 실행하고 Github의 Actions 탭에서 성공한 실행을 선택한 뒤 run-singleton의 Run main.py를 열어서 결과를 확인했다.

실행 결과 : 
Python 3.14.10
같은 객체? True
변경 전 b.count: 0
변경 후 b.count: 1

구현 설명 : get_instance()를 처음 호출하면 Counter 객체를 하나 만들고 클래스 변수 _instance에 저장한다. 그다음부터는 새 객체를 만들지 않고 _instance에 저장된 객체를 반환하며 Counter()로 직접 생성하려고 하면 오류가 발생한다. a와 b를 각각 따로 요청한 뒤 a is b가 True인 것을 확인하여 두 변수가 같은 객체를 가리킨다는 것을 알 수 있고 a.count만 1증가시켰는데 b.count도 0에서 1로 바뀐 것을 보아 두 변수가 상태를 공유한다는 것을 알 수 있다.
