import 'package:flutter/material.dart';

class keyPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.purple,
        appBar: AppBar(
          backgroundColor: Colors.deepOrange,
          title: Center(
            child: Text(
              'KeyControl',
              style: TextStyle(
                fontFamily: 'Pacifico',
                fontSize: 30.0,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
          ),
        ),
        body: keyBody());
  }
}

class keyBody extends StatefulWidget {
  const keyBody({super.key});

  @override
  State<keyBody> createState() => _keyBodyState();
}

class _keyBodyState extends State<keyBody> {
  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      children: [
        Center(
          child:
          Image.asset('images/cat_icon.png',
          color:
          Colors.deepOrange),
              ),
        Center(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              Expanded(
                flex: 1,
                child: Card(
                  color: Colors.deepOrange,
                  child: Padding(
                    padding: EdgeInsets.all(16.0),
                    child: TextButton(
                      onPressed: () {
                        print('Supposed to lock the catdoor from the outside. \n'
                            'Turn off the inside IR sensors.');
                      },
                      child: Column(
                        children: [
                          Icon(
                            Icons.home,
                            size: 50.0,
                            color: Colors.white,
                          ),
                          Text(
                            'Stay Home',
                            style: TextStyle(
                                fontFamily: 'SourceSansPro',
                                fontSize: 10.0,
                                fontWeight: FontWeight.bold,
                                color: Colors.white),
                          )
                        ],
                      ),
                    ),
                  ),
                ),
              ),
              Expanded(
                flex: 1,
                child: Card(
                  color: Colors.deepOrange,
                  child: Padding(
                    padding: EdgeInsets.all(16.0),
                    child: TextButton(
                      onPressed: () {
                        print('Supposed to lock the catdoor from the inside \n'
                            'Turn off the outside IR sensors.');
                      },
                      child: Column(
                        children: [
                          Icon(
                            Icons.sunny,
                            size: 50.0,
                            color: Colors.white,
                          ),
                          Text(
                            'Stay Outside',
                            style: TextStyle(
                              fontFamily: 'SourceSansPro',
                              fontSize: 10.0,
                              fontWeight: FontWeight.bold,
                              color: Colors.white,
                            ),
                          )
                        ],
                      ),
                    ),
                  ),
                ),
              ),
              Expanded(
                flex: 1,
                child: Card(
                  color: Colors.deepOrange,
                  child: Padding(
                    padding: EdgeInsets.all(16.0),
                    child: TextButton(
                      onPressed: () {
                        print('Supposed to lock the catdoor.');
                      },
                      child: Column(
                        children: [
                          Icon(
                            Icons.lock,
                            size: 50.0,
                            color: Colors.white,
                          ),
                          Text(
                            'Lock The Flap',
                            style: TextStyle(
                              fontFamily: 'SourceSansPro',
                              fontWeight: FontWeight.bold,
                              fontSize: 10.0,
                              color: Colors.white,
                            ),
                          )
                        ],
                      ),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}


/*
Center(
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Card(
            color: Colors.deepOrange,
            child: TextButton(
              onPressed: () {
                print('Supposed to lock the catdoor from the outside. \n'
                    'Turn off the inside IR sensors.');
              },
              child: Column(
                children: [
                  Icon(
                    Icons.home_outlined,
                    size: 50.0,
                    color: Colors.white,
                  ),
                  Text('Stay Home',
                    style: TextStyle(
                      fontFamily: 'SourceSansPro',
                      fontSize: 10.0,
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                    ),
                  ),
                ],
              ),
              ),
            ),
          Card(
            color: Colors.deepOrange,
            child: Expanded(
              child: Padding(
                padding: EdgeInsets.all(16.0),
                child: TextButton(
                  onPressed: () {
                    print('Supposed to lock the catdoor from the inside \n'
                        'Turn off the outside IR sensors.');
                  },
                  child: Icon(
                    Icons.sunny,
                    size: 50.0,
                    color: Colors.white,
                  ),
                ),
              ),
            ),
          ),
          Card(
            color: Colors.deepOrange,
            child: Expanded(
              child: Padding(
                padding: EdgeInsets.all(16.0),
                child: TextButton(
                  onPressed: () {
                    print('Supposed to lock the catdoor.');
                  },
                  child: Icon(
                    Icons.lock,
                    size: 50.0,
                    color: Colors.white,
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
 */