import 'package:flutter/material.dart';
import 'package:audioplayers/audioplayers.dart';

import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

// import 'new_page_model.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => AudioPlayerPage();
}

/*
class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }
}
*/
class AudioPlayerPage extends State<MyHomePage> {
  AudioCache audioCache = AudioCache();

  void playSound(String soundFileName) {
    audioCache.play(soundFileName);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      /*
      appBar: AppBar(
        title: Text('Audio Player'),
      ),*/
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('RoboDog',
                style: TextStyle(
                  fontSize: 50,
                  fontFamily: GoogleFonts.getFont('Outfit').fontFamily,
                  color: Colors.black, // Assuming you want black color
                  fontWeight: FontWeight.w600,
                )),
            Text('Assistant',
                style: TextStyle(
                  fontSize: 50,
                  fontFamily: GoogleFonts.getFont('Outfit').fontFamily,
                  color: Colors.black, // Assuming you want black color
                  fontWeight: FontWeight.w600,
                )),
            Container(
              padding: EdgeInsets.symmetric(vertical: 30),
            ),
            SizedBox(
              width: 200,
              child: ElevatedButton(
                onPressed: () {
                  playSound("audio1.mp3");
                },
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all<Color>(
                    Color(
                        0xFF9c27b0), // Adjust color to your desired shade of purple
                  ),
                  elevation: MaterialStateProperty.all<double>(
                      4), // Adjust elevation as needed
                  textStyle: MaterialStateProperty.all<TextStyle>(
                    TextStyle(
                      fontSize: 16, // Adjust font size as needed
                      fontWeight: FontWeight.bold,
                      color: Colors.white, // Adjust text color as needed
                    ),
                  ),
                  padding: MaterialStateProperty.all<EdgeInsetsGeometry>(
                    EdgeInsets.symmetric(
                        vertical: 16,
                        horizontal: 24), // Adjust padding as needed
                  ),
                  shape: MaterialStateProperty.all<OutlinedBorder>(
                    RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(
                          8), // Adjust border radius as needed
                    ),
                  ),
                ),
                child:
                    Text('Crosswalk is Safe'), // Adjust button text as needed
              ),
            ),
            Container(
              padding: EdgeInsets.symmetric(vertical: 20),
            ),
            SizedBox(
              width: 200,
              child: ElevatedButton(
                onPressed: () {
                  playSound("audio2.mp3");
                },
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all<Color>(
                    Color(
                        0xFF9c27b0), // Adjust color to your desired shade of purple
                  ),
                  elevation: MaterialStateProperty.all<double>(
                      4), // Adjust elevation as needed
                  textStyle: MaterialStateProperty.all<TextStyle>(
                    TextStyle(
                      fontSize: 16, // Adjust font size as needed
                      fontWeight: FontWeight.bold,
                      color: Colors.white, // Adjust text color as needed
                    ),
                  ),
                  padding: MaterialStateProperty.all<EdgeInsetsGeometry>(
                    EdgeInsets.symmetric(
                        vertical: 16,
                        horizontal: 24), // Adjust padding as needed
                  ),
                  shape: MaterialStateProperty.all<OutlinedBorder>(
                    RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(
                          8), // Adjust border radius as needed
                    ),
                  ),
                ),
                child: Text('Crosswalk Done'), // Adjust button text as needed
              ),
            ),
            Container(
              padding: EdgeInsets.symmetric(vertical: 20),
            ),
            SizedBox(
              width: 200,
              child: ElevatedButton(
                onPressed: () {
                  playSound("audio3.mp3");
                },
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all<Color>(
                    Color(
                        0xFF9c27b0), // Adjust color to your desired shade of purple
                  ),
                  elevation: MaterialStateProperty.all<double>(
                      4), // Adjust elevation as needed
                  textStyle: MaterialStateProperty.all<TextStyle>(
                    TextStyle(
                      fontSize: 16, // Adjust font size as needed
                      fontWeight: FontWeight.bold,
                      color: Colors.white, // Adjust text color as needed
                    ),
                  ),
                  padding: MaterialStateProperty.all<EdgeInsetsGeometry>(
                    EdgeInsets.symmetric(
                        vertical: 16,
                        horizontal: 24), // Adjust padding as needed
                  ),
                  shape: MaterialStateProperty.all<OutlinedBorder>(
                    RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(
                          8), // Adjust border radius as needed
                    ),
                  ),
                ),
                child:
                    Text('Obstruction Ahead'), // Adjust button text as needed
              ),
            ),
          ],
        ),
      ),
    );
  }
}




/*
import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

import 'new_page_model.dart';
export 'new_page_model.dart';

class NewPageWidget extends StatefulWidget {
  const NewPageWidget({super.key});

  @override
  State<NewPageWidget> createState() => _NewPageWidgetState();
}

class _NewPageWidgetState extends State<NewPageWidget> {
  late NewPageModel _model;

  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => NewPageModel());
  }

  @override
  void dispose() {
    _model.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => _model.unfocusNode.canRequestFocus
          ? FocusScope.of(context).requestFocus(_model.unfocusNode)
          : FocusScope.of(context).unfocus(),
      child: Scaffold(
        key: scaffoldKey,
        backgroundColor: FlutterFlowTheme.of(context).primaryBackground,
        appBar: responsiveVisibility(
          context: context,
          tabletLandscape: false,
          desktop: false,
        )
            ? AppBar(
                backgroundColor: FlutterFlowTheme.of(context).primaryBackground,
                automaticallyImplyLeading: false,
                leading: FlutterFlowIconButton(
                  buttonSize: 60,
                  icon: Icon(
                    Icons.menu,
                    color: FlutterFlowTheme.of(context).primaryText,
                    size: 24,
                  ),
                  onPressed: () {
                    print('IconButton pressed ...');
                  },
                ),
                actions: [
                  FlutterFlowIconButton(
                    buttonSize: 60,
                    icon: Icon(
                      Icons.power_settings_new,
                      color: FlutterFlowTheme.of(context).primaryText,
                      size: 24,
                    ),
                    onPressed: () {
                      print('IconButton pressed ...');
                    },
                  ),
                ],
                centerTitle: false,
                elevation: 0,
              )
            : null,
        body: SafeArea(
          top: true,
          child: Padding(
            padding: EdgeInsetsDirectional.fromSTEB(16, 0, 16, 0),
            child: Column(
              mainAxisSize: MainAxisSize.max,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Text(
                  'RoboDog Assistant',
                  style: FlutterFlowTheme.of(context).displayLarge.override(
                        fontFamily: 'Outfit',
                        color: FlutterFlowTheme.of(context).primaryText,
                        fontWeight: FontWeight.w600,
                      ),
                ),
                Image.network(
                  'https://images.unsplash.com/source-404?w=512&h=512',
                  width: 200,
                  height: 200,
                  fit: BoxFit.cover,
                ),
                Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(24, 0, 16, 0),
                  child: Text(
                    'Control your RoboDog with voice commands.',
                    style: FlutterFlowTheme.of(context).headlineMedium.override(
                          fontFamily: 'Outfit',
                          color: FlutterFlowTheme.of(context).secondaryText,
                        ),
                  ),
                ),
                Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(0, 24, 0, 0),
                  child: FFButtonWidget(
                    onPressed: () {
                      print('Button pressed ...');
                    },
                    text: 'Audio Commands',
                    options: FFButtonOptions(
                      width: 300,
                      height: 60,
                      padding: EdgeInsetsDirectional.fromSTEB(0, 0, 0, 0),
                      iconPadding: EdgeInsetsDirectional.fromSTEB(0, 0, 0, 0),
                      color: FlutterFlowTheme.of(context).primary,
                      textStyle:
                          FlutterFlowTheme.of(context).titleMedium.override(
                                fontFamily: 'Plus Jakarta Sans',
                                color: Colors.white,
                              ),
                      elevation: 3,
                      borderRadius: BorderRadius.circular(30),
                    ),
                  ),
                ),
                Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(0, 24, 0, 0),
                  child: FFButtonWidget(
                    onPressed: () {
                      print('Button pressed ...');
                    },
                    text: 'Bark Translator',
                    options: FFButtonOptions(
                      width: 300,
                      height: 60,
                      padding: EdgeInsetsDirectional.fromSTEB(0, 0, 0, 0),
                      iconPadding: EdgeInsetsDirectional.fromSTEB(0, 0, 0, 0),
                      color: FlutterFlowTheme.of(context).primary,
                      textStyle:
                          FlutterFlowTheme.of(context).titleMedium.override(
                                fontFamily: 'Plus Jakarta Sans',
                                color: Colors.white,
                              ),
                      elevation: 3,
                      borderRadius: BorderRadius.circular(30),
                    ),
                  ),
                ),
                Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(0, 24, 0, 0),
                  child: FFButtonWidget(
                    onPressed: () {
                      print('Button pressed ...');
                    },
                    text: 'Training Modes',
                    options: FFButtonOptions(
                      width: 300,
                      height: 60,
                      padding: EdgeInsetsDirectional.fromSTEB(0, 0, 0, 0),
                      iconPadding: EdgeInsetsDirectional.fromSTEB(0, 0, 0, 0),
                      color: FlutterFlowTheme.of(context).primary,
                      textStyle:
                          FlutterFlowTheme.of(context).titleMedium.override(
                                fontFamily: 'Plus Jakarta Sans',
                                color: Colors.white,
                              ),
                      elevation: 3,
                      borderRadius: BorderRadius.circular(30),
                    ),
                  ),
                ),
                Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(0, 24, 0, 0),
                  child: FFButtonWidget(
                    onPressed: () {
                      print('Button pressed ...');
                    },
                    text: 'Settings',
                    options: FFButtonOptions(
                      width: 300,
                      height: 60,
                      padding: EdgeInsetsDirectional.fromSTEB(0, 0, 0, 0),
                      iconPadding: EdgeInsetsDirectional.fromSTEB(0, 0, 0, 0),
                      color: FlutterFlowTheme.of(context).primary,
                      textStyle:
                          FlutterFlowTheme.of(context).titleMedium.override(
                                fontFamily: 'Plus Jakarta Sans',
                                color: Colors.white,
                              ),
                      elevation: 3,
                      borderRadius: BorderRadius.circular(30),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
*/