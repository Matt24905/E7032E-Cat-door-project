import 'package:flutter/material.dart';

class statPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.deepOrange,
        title: Center(
          child: Text(
            'Coming & Goings...',
            style: TextStyle(
                fontFamily: 'Pacifico',
                fontWeight: FontWeight.bold,
                fontSize: 30.0),
          ),
        ),
      ),
      body: statBody(),
    );
  }
}

class statBody extends StatefulWidget {
  const statBody({super.key});

  @override
  State<statBody> createState() => _statBodyState();
}

class _statBodyState extends State<statBody> {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Center(
            child: Image.asset('images/cat_icon.png',
                color: Colors.deepOrange),
          ),
          Row(
            children: [
              Expanded(
                child: Card(
                  child: ListTile(
                    leading: Icon(
                      Icons.access_time,
                      color: Colors.teal,
                      size: 70.0,
                    ),
                    title: Text('How long has your cat been outside today: ',
                    style: TextStyle(
                      fontFamily: 'SourceSansPro',
                      fontSize: 20.0,
                      fontWeight: FontWeight.bold,
                    ),
                    ),
                    subtitle: Text('3h 30min',
                    style: TextStyle(
                      fontSize: 30.0,
                    ),),

                  ),
                ),
              ),
            ],
          ),
          Row(
            children: [
              Expanded(
                child: Card(
                  child: ListTile(
                    leading: Icon(
                      Icons.access_time,
                      color: Colors.teal,
                      size: 70.0,
                    ),
                    title: Text('How long has your cat been outside this week: ',
                      style: TextStyle(
                        fontFamily: 'SourceSansPro',
                        fontSize: 20.0,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    subtitle: Text('9h 30min',
                      style: TextStyle(
                        fontSize: 30.0,
                      ),),

                  ),
                ),
              ),
            ],
          ),
          Row(
            children: [
              Expanded(
                child: Card(
                  child: ListTile(
                    leading: Icon(
                      Icons.access_time,
                      color: Colors.teal,
                      size: 70.0,
                    ),
                    title: Text('How long has your cat been inside this week: ',
                      style: TextStyle(
                        fontFamily: 'SourceSansPro',
                        fontSize: 20.0,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    subtitle: Text('45h 30min',
                      style: TextStyle(
                        fontSize: 30.0,
                      ),),

                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
