import 'package:flutter/material.dart';
import 'statPage.dart';
import 'keyPage.dart';
import 'loginPage.dart';

void main() {
  runApp(const homePage());
}

class homePage extends StatelessWidget {
  const homePage({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
          backgroundColor: Colors.black,
          appBar: AppBar(
            backgroundColor: Colors.deepOrange,
            title: Center(
              child: Text(
                'MeowMania',
                style: TextStyle(
                  fontFamily: 'Pacifico',
                  fontSize: 30.0,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
            ),
          ),
          body: bodyOfHomePage()),
    );
  }
}

class bodyOfHomePage extends StatefulWidget {
  const bodyOfHomePage({super.key});
  @override
  State<bodyOfHomePage> createState() => _bodyOfHomePageState();
}

class _bodyOfHomePageState extends State<bodyOfHomePage> {
  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      children: [
        Center(
          child: Column(
            children: [
              Image.asset('images/cat_icon.png',
              color: Colors.deepOrange),
              Text('Homepage',
                style: TextStyle(
                  fontFamily: 'Pacifico',
                  fontWeight: FontWeight.bold,
                  fontSize: 25.0,
                  color: Colors.deepOrange,
                ),)
            ],
          ),

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
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => keyPage()),
                        );
                      },
                      child: Column(
                        children: [
                          Icon(
                            Icons.cloudy_snowing,
                            size: 50.0,
                            color: Colors.white,
                          ),
                          Text(
                            'Weather',
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
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => statPage()),
                        );
                      },
                      child: Column(
                        children: [
                          Icon(
                            Icons.add_chart,
                            size: 50.0,
                            color: Colors.white,
                          ),
                          Text(
                            'Statistics',
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
            ],
          ),
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
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => keyPage()),
                        );
                      },
                      child: Column(
                        children: [
                          Icon(
                            Icons.lock_clock,
                            size: 50.0,
                            color: Colors.white,
                          ),
                          Text(
                            'Lock',
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
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => statPage()),
                        );
                      },
                      child: Column(
                        children: [
                          Icon(
                            Icons.notification_important_rounded,
                            size: 50.0,
                            color: Colors.white,
                          ),
                          Text(
                            'Notifications',
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
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => loginPage()),
                        );
                      },
                      child: Column(
                        children: [
                          Icon(
                            Icons.logout_sharp,
                            size: 50.0,
                            color: Colors.white,
                          ),
                          Text(
                            'Login',
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

