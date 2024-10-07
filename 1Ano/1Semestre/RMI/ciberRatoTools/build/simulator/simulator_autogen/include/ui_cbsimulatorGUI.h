/********************************************************************************
** Form generated from reading UI file 'cbsimulatorGUI.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CBSIMULATORGUI_H
#define UI_CBSIMULATORGUI_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDockWidget>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_cbSimulatorGUI
{
public:
    QAction *actionReset;
    QAction *actionSimulator_Help;
    QAction *actionAbout_Simulator;
    QAction *actionExit;
    QAction *actionGPS_Enabled;
    QAction *actionScore_Sensor_Enabled;
    QAction *actionTime_Enabled;
    QAction *actionOpen_Lab;
    QAction *actionEdit_Configuration;
    QAction *actionOpen_Configuration;
    QAction *actionSave_Configuration;
    QAction *actionLaunch_Viewer;
    QAction *actionRegistrations_Open;
    QAction *actionStartStop;
    QAction *actionManageRobots;
    QAction *actionControl_Panel;
    QAction *actionLoad_Defaults;
    QAction *actionCollisions_Enabled;
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout;
    QTextEdit *messages;
    QMenuBar *menubar;
    QMenu *menuFile;
    QMenu *menuConfiguration;
    QMenu *menuCommand;
    QMenu *menuOptions;
    QMenu *menuHelp;
    QStatusBar *statusbar;
    QToolBar *toolBar_1;
    QDockWidget *dockWidget_Score;
    QWidget *dockWidgetContents_Score;
    QGridLayout *gridLayout;
    QLabel *label_2;
    QGridLayout *gridLayout_Scores;
    QSpacerItem *horizontalSpacer_2;
    QLCDNumber *lcdNumber_TimeRemain;
    QSpacerItem *verticalSpacer_2;
    QToolBar *toolBar_2;
    QDockWidget *dockWidget_Mailbox;
    QWidget *dockWidgetContents_Mail;
    QVBoxLayout *verticalLayout_2;
    QGroupBox *groupBox;
    QGridLayout *gridLayout_3;
    QComboBox *comboBox_Robot;
    QCheckBox *checkBox_Actions;
    QCheckBox *checkBox_Measures;
    QCheckBox *checkBox_Positions;
    QLabel *label;
    QPushButton *pushButton_ClearMailBox;
    QSpacerItem *horizontalSpacer;
    QTextEdit *textEdit_Mailbox;

    void setupUi(QMainWindow *cbSimulatorGUI)
    {
        if (cbSimulatorGUI->objectName().isEmpty())
            cbSimulatorGUI->setObjectName(QString::fromUtf8("cbSimulatorGUI"));
        cbSimulatorGUI->resize(994, 750);
        actionReset = new QAction(cbSimulatorGUI);
        actionReset->setObjectName(QString::fromUtf8("actionReset"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/images/control/reset"), QSize(), QIcon::Normal, QIcon::Off);
        actionReset->setIcon(icon);
        actionSimulator_Help = new QAction(cbSimulatorGUI);
        actionSimulator_Help->setObjectName(QString::fromUtf8("actionSimulator_Help"));
        actionAbout_Simulator = new QAction(cbSimulatorGUI);
        actionAbout_Simulator->setObjectName(QString::fromUtf8("actionAbout_Simulator"));
        actionExit = new QAction(cbSimulatorGUI);
        actionExit->setObjectName(QString::fromUtf8("actionExit"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/images/buttons/exit"), QSize(), QIcon::Normal, QIcon::Off);
        actionExit->setIcon(icon1);
        actionGPS_Enabled = new QAction(cbSimulatorGUI);
        actionGPS_Enabled->setObjectName(QString::fromUtf8("actionGPS_Enabled"));
        actionGPS_Enabled->setCheckable(true);
        actionGPS_Enabled->setChecked(true);
        actionScore_Sensor_Enabled = new QAction(cbSimulatorGUI);
        actionScore_Sensor_Enabled->setObjectName(QString::fromUtf8("actionScore_Sensor_Enabled"));
        actionScore_Sensor_Enabled->setCheckable(true);
        actionTime_Enabled = new QAction(cbSimulatorGUI);
        actionTime_Enabled->setObjectName(QString::fromUtf8("actionTime_Enabled"));
        actionTime_Enabled->setCheckable(true);
        actionTime_Enabled->setChecked(true);
        actionTime_Enabled->setEnabled(true);
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/images/buttons/time_off"), QSize(), QIcon::Normal, QIcon::Off);
        icon2.addFile(QString::fromUtf8(":/images/buttons/time_on"), QSize(), QIcon::Normal, QIcon::On);
        actionTime_Enabled->setIcon(icon2);
        actionOpen_Lab = new QAction(cbSimulatorGUI);
        actionOpen_Lab->setObjectName(QString::fromUtf8("actionOpen_Lab"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/images/buttons/lab"), QSize(), QIcon::Normal, QIcon::Off);
        actionOpen_Lab->setIcon(icon3);
        actionEdit_Configuration = new QAction(cbSimulatorGUI);
        actionEdit_Configuration->setObjectName(QString::fromUtf8("actionEdit_Configuration"));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/images/buttons/config"), QSize(), QIcon::Normal, QIcon::Off);
        actionEdit_Configuration->setIcon(icon4);
        actionOpen_Configuration = new QAction(cbSimulatorGUI);
        actionOpen_Configuration->setObjectName(QString::fromUtf8("actionOpen_Configuration"));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/images/buttons/open"), QSize(), QIcon::Normal, QIcon::Off);
        actionOpen_Configuration->setIcon(icon5);
        actionSave_Configuration = new QAction(cbSimulatorGUI);
        actionSave_Configuration->setObjectName(QString::fromUtf8("actionSave_Configuration"));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/images/buttons/save"), QSize(), QIcon::Normal, QIcon::Off);
        actionSave_Configuration->setIcon(icon6);
        actionLaunch_Viewer = new QAction(cbSimulatorGUI);
        actionLaunch_Viewer->setObjectName(QString::fromUtf8("actionLaunch_Viewer"));
        actionLaunch_Viewer->setCheckable(true);
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/images/buttons/viewer_close"), QSize(), QIcon::Normal, QIcon::Off);
        icon7.addFile(QString::fromUtf8(":/images/buttons/viewer_open"), QSize(), QIcon::Normal, QIcon::On);
        actionLaunch_Viewer->setIcon(icon7);
        actionRegistrations_Open = new QAction(cbSimulatorGUI);
        actionRegistrations_Open->setObjectName(QString::fromUtf8("actionRegistrations_Open"));
        actionRegistrations_Open->setCheckable(true);
        actionRegistrations_Open->setChecked(true);
        actionRegistrations_Open->setEnabled(false);
        QIcon icon8;
        icon8.addFile(QString::fromUtf8(":/images/buttons/lock_closed"), QSize(), QIcon::Normal, QIcon::Off);
        icon8.addFile(QString::fromUtf8(":/images/buttons/lock_open"), QSize(), QIcon::Normal, QIcon::On);
        actionRegistrations_Open->setIcon(icon8);
        actionStartStop = new QAction(cbSimulatorGUI);
        actionStartStop->setObjectName(QString::fromUtf8("actionStartStop"));
        actionStartStop->setEnabled(false);
        QIcon icon9;
        icon9.addFile(QString::fromUtf8(":/images/control/start"), QSize(), QIcon::Normal, QIcon::Off);
        icon9.addFile(QString::fromUtf8(":/images/control/stop"), QSize(), QIcon::Normal, QIcon::On);
        actionStartStop->setIcon(icon9);
        actionManageRobots = new QAction(cbSimulatorGUI);
        actionManageRobots->setObjectName(QString::fromUtf8("actionManageRobots"));
        actionManageRobots->setCheckable(true);
        QIcon icon10;
        icon10.addFile(QString::fromUtf8(":/images/buttons/mouse"), QSize(), QIcon::Normal, QIcon::Off);
        actionManageRobots->setIcon(icon10);
        actionControl_Panel = new QAction(cbSimulatorGUI);
        actionControl_Panel->setObjectName(QString::fromUtf8("actionControl_Panel"));
        actionControl_Panel->setCheckable(true);
        QIcon icon11;
        icon11.addFile(QString::fromUtf8(":/images/buttons/panel"), QSize(), QIcon::Normal, QIcon::Off);
        actionControl_Panel->setIcon(icon11);
        actionLoad_Defaults = new QAction(cbSimulatorGUI);
        actionLoad_Defaults->setObjectName(QString::fromUtf8("actionLoad_Defaults"));
        QIcon icon12;
        icon12.addFile(QString::fromUtf8(":/images/buttons/defaults"), QSize(), QIcon::Normal, QIcon::Off);
        actionLoad_Defaults->setIcon(icon12);
        actionCollisions_Enabled = new QAction(cbSimulatorGUI);
        actionCollisions_Enabled->setObjectName(QString::fromUtf8("actionCollisions_Enabled"));
        actionCollisions_Enabled->setCheckable(true);
        actionCollisions_Enabled->setChecked(true);
        QIcon icon13;
        icon13.addFile(QString::fromUtf8(":/images/buttons/collisions_off"), QSize(), QIcon::Normal, QIcon::Off);
        icon13.addFile(QString::fromUtf8(":/images/buttons/collisions_on"), QSize(), QIcon::Normal, QIcon::On);
        actionCollisions_Enabled->setIcon(icon13);
        centralwidget = new QWidget(cbSimulatorGUI);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout = new QVBoxLayout(centralwidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        messages = new QTextEdit(centralwidget);
        messages->setObjectName(QString::fromUtf8("messages"));
        messages->setReadOnly(true);

        verticalLayout->addWidget(messages);

        cbSimulatorGUI->setCentralWidget(centralwidget);
        menubar = new QMenuBar(cbSimulatorGUI);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 994, 25));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QString::fromUtf8("menuFile"));
        menuConfiguration = new QMenu(menuFile);
        menuConfiguration->setObjectName(QString::fromUtf8("menuConfiguration"));
        menuCommand = new QMenu(menubar);
        menuCommand->setObjectName(QString::fromUtf8("menuCommand"));
        menuOptions = new QMenu(menubar);
        menuOptions->setObjectName(QString::fromUtf8("menuOptions"));
        menuHelp = new QMenu(menubar);
        menuHelp->setObjectName(QString::fromUtf8("menuHelp"));
        cbSimulatorGUI->setMenuBar(menubar);
        statusbar = new QStatusBar(cbSimulatorGUI);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        cbSimulatorGUI->setStatusBar(statusbar);
        toolBar_1 = new QToolBar(cbSimulatorGUI);
        toolBar_1->setObjectName(QString::fromUtf8("toolBar_1"));
        toolBar_1->setIconSize(QSize(24, 24));
        cbSimulatorGUI->addToolBar(Qt::TopToolBarArea, toolBar_1);
        dockWidget_Score = new QDockWidget(cbSimulatorGUI);
        dockWidget_Score->setObjectName(QString::fromUtf8("dockWidget_Score"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(dockWidget_Score->sizePolicy().hasHeightForWidth());
        dockWidget_Score->setSizePolicy(sizePolicy);
        QIcon icon14;
        icon14.addFile(QString::fromUtf8(":/images/icons/score"), QSize(), QIcon::Normal, QIcon::Off);
        dockWidget_Score->setWindowIcon(icon14);
        dockWidget_Score->setFloating(false);
        dockWidget_Score->setFeatures(QDockWidget::AllDockWidgetFeatures);
        dockWidgetContents_Score = new QWidget();
        dockWidgetContents_Score->setObjectName(QString::fromUtf8("dockWidgetContents_Score"));
        gridLayout = new QGridLayout(dockWidgetContents_Score);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_2 = new QLabel(dockWidgetContents_Score);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        QFont font;
        font.setPointSize(11);
        font.setBold(false);
        font.setWeight(50);
        label_2->setFont(font);

        gridLayout->addWidget(label_2, 0, 0, 1, 1);

        gridLayout_Scores = new QGridLayout();
        gridLayout_Scores->setObjectName(QString::fromUtf8("gridLayout_Scores"));

        gridLayout->addLayout(gridLayout_Scores, 0, 2, 3, 2);

        horizontalSpacer_2 = new QSpacerItem(60, 1, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 0, 1, 1, 1);

        lcdNumber_TimeRemain = new QLCDNumber(dockWidgetContents_Score);
        lcdNumber_TimeRemain->setObjectName(QString::fromUtf8("lcdNumber_TimeRemain"));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(lcdNumber_TimeRemain->sizePolicy().hasHeightForWidth());
        lcdNumber_TimeRemain->setSizePolicy(sizePolicy1);
        lcdNumber_TimeRemain->setMinimumSize(QSize(100, 27));
        lcdNumber_TimeRemain->setMaximumSize(QSize(100, 27));
        QPalette palette;
        QBrush brush(QColor(0, 0, 0, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::WindowText, brush);
        QBrush brush1(QColor(255, 255, 255, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Button, brush1);
        palette.setBrush(QPalette::Active, QPalette::Light, brush1);
        palette.setBrush(QPalette::Active, QPalette::Midlight, brush1);
        QBrush brush2(QColor(127, 127, 127, 255));
        brush2.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Dark, brush2);
        QBrush brush3(QColor(170, 170, 170, 255));
        brush3.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Mid, brush3);
        palette.setBrush(QPalette::Active, QPalette::Text, brush);
        palette.setBrush(QPalette::Active, QPalette::BrightText, brush1);
        palette.setBrush(QPalette::Active, QPalette::ButtonText, brush);
        palette.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette.setBrush(QPalette::Active, QPalette::Shadow, brush);
        palette.setBrush(QPalette::Active, QPalette::AlternateBase, brush1);
        QBrush brush4(QColor(255, 255, 220, 255));
        brush4.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::ToolTipBase, brush4);
        palette.setBrush(QPalette::Active, QPalette::ToolTipText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Button, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Light, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Midlight, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Dark, brush2);
        palette.setBrush(QPalette::Inactive, QPalette::Mid, brush3);
        palette.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette.setBrush(QPalette::Inactive, QPalette::BrightText, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Shadow, brush);
        palette.setBrush(QPalette::Inactive, QPalette::AlternateBase, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::ToolTipBase, brush4);
        palette.setBrush(QPalette::Inactive, QPalette::ToolTipText, brush);
        palette.setBrush(QPalette::Disabled, QPalette::WindowText, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::Button, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Light, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Midlight, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Dark, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::Mid, brush3);
        palette.setBrush(QPalette::Disabled, QPalette::Text, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::BrightText, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::ButtonText, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Shadow, brush);
        palette.setBrush(QPalette::Disabled, QPalette::AlternateBase, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::ToolTipBase, brush4);
        palette.setBrush(QPalette::Disabled, QPalette::ToolTipText, brush);
        lcdNumber_TimeRemain->setPalette(palette);
        lcdNumber_TimeRemain->setFrameShape(QFrame::NoFrame);
        lcdNumber_TimeRemain->setDigitCount(4);
        lcdNumber_TimeRemain->setSegmentStyle(QLCDNumber::Flat);

        gridLayout->addWidget(lcdNumber_TimeRemain, 1, 0, 1, 1);

        verticalSpacer_2 = new QSpacerItem(1, 0, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_2, 2, 0, 1, 2);

        dockWidget_Score->setWidget(dockWidgetContents_Score);
        cbSimulatorGUI->addDockWidget(Qt::BottomDockWidgetArea, dockWidget_Score);
        toolBar_2 = new QToolBar(cbSimulatorGUI);
        toolBar_2->setObjectName(QString::fromUtf8("toolBar_2"));
        toolBar_2->setIconSize(QSize(24, 24));
        cbSimulatorGUI->addToolBar(Qt::TopToolBarArea, toolBar_2);
        dockWidget_Mailbox = new QDockWidget(cbSimulatorGUI);
        dockWidget_Mailbox->setObjectName(QString::fromUtf8("dockWidget_Mailbox"));
        dockWidget_Mailbox->setEnabled(true);
        sizePolicy.setHeightForWidth(dockWidget_Mailbox->sizePolicy().hasHeightForWidth());
        dockWidget_Mailbox->setSizePolicy(sizePolicy);
        QIcon icon15;
        icon15.addFile(QString::fromUtf8(":/images/icons/message"), QSize(), QIcon::Normal, QIcon::Off);
        dockWidget_Mailbox->setWindowIcon(icon15);
        dockWidget_Mailbox->setFloating(false);
        dockWidgetContents_Mail = new QWidget();
        dockWidgetContents_Mail->setObjectName(QString::fromUtf8("dockWidgetContents_Mail"));
        verticalLayout_2 = new QVBoxLayout(dockWidgetContents_Mail);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        groupBox = new QGroupBox(dockWidgetContents_Mail);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout_3 = new QGridLayout(groupBox);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        comboBox_Robot = new QComboBox(groupBox);
        comboBox_Robot->setObjectName(QString::fromUtf8("comboBox_Robot"));
        comboBox_Robot->setMinimumSize(QSize(120, 0));
        comboBox_Robot->setInsertPolicy(QComboBox::InsertAlphabetically);

        gridLayout_3->addWidget(comboBox_Robot, 0, 4, 1, 1);

        checkBox_Actions = new QCheckBox(groupBox);
        checkBox_Actions->setObjectName(QString::fromUtf8("checkBox_Actions"));
        checkBox_Actions->setChecked(true);

        gridLayout_3->addWidget(checkBox_Actions, 0, 0, 1, 1);

        checkBox_Measures = new QCheckBox(groupBox);
        checkBox_Measures->setObjectName(QString::fromUtf8("checkBox_Measures"));
        checkBox_Measures->setChecked(true);

        gridLayout_3->addWidget(checkBox_Measures, 0, 1, 1, 1);

        checkBox_Positions = new QCheckBox(groupBox);
        checkBox_Positions->setObjectName(QString::fromUtf8("checkBox_Positions"));
        checkBox_Positions->setChecked(false);

        gridLayout_3->addWidget(checkBox_Positions, 0, 2, 1, 1);

        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));
        label->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout_3->addWidget(label, 0, 3, 1, 1);

        pushButton_ClearMailBox = new QPushButton(groupBox);
        pushButton_ClearMailBox->setObjectName(QString::fromUtf8("pushButton_ClearMailBox"));

        gridLayout_3->addWidget(pushButton_ClearMailBox, 0, 6, 1, 1);

        horizontalSpacer = new QSpacerItem(0, 1, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_3->addItem(horizontalSpacer, 0, 5, 1, 1);


        verticalLayout_2->addWidget(groupBox);

        textEdit_Mailbox = new QTextEdit(dockWidgetContents_Mail);
        textEdit_Mailbox->setObjectName(QString::fromUtf8("textEdit_Mailbox"));
        textEdit_Mailbox->setReadOnly(true);

        verticalLayout_2->addWidget(textEdit_Mailbox);

        dockWidget_Mailbox->setWidget(dockWidgetContents_Mail);
        cbSimulatorGUI->addDockWidget(Qt::BottomDockWidgetArea, dockWidget_Mailbox);

        menubar->addAction(menuFile->menuAction());
        menubar->addAction(menuCommand->menuAction());
        menubar->addAction(menuOptions->menuAction());
        menubar->addAction(menuHelp->menuAction());
        menuFile->addAction(menuConfiguration->menuAction());
        menuFile->addAction(actionOpen_Lab);
        menuFile->addAction(actionLoad_Defaults);
        menuFile->addSeparator();
        menuFile->addAction(actionManageRobots);
        menuFile->addAction(actionControl_Panel);
        menuFile->addAction(actionLaunch_Viewer);
        menuFile->addSeparator();
        menuFile->addAction(actionExit);
        menuConfiguration->addAction(actionEdit_Configuration);
        menuConfiguration->addAction(actionOpen_Configuration);
        menuConfiguration->addAction(actionSave_Configuration);
        menuCommand->addAction(actionReset);
        menuCommand->addAction(actionStartStop);
        menuOptions->addAction(actionGPS_Enabled);
        menuOptions->addAction(actionScore_Sensor_Enabled);
        menuOptions->addAction(actionTime_Enabled);
        menuOptions->addAction(actionCollisions_Enabled);
        menuOptions->addAction(actionRegistrations_Open);
        menuHelp->addAction(actionSimulator_Help);
        menuHelp->addAction(actionAbout_Simulator);
        toolBar_1->addAction(actionReset);
        toolBar_1->addAction(actionStartStop);
        toolBar_1->addSeparator();
        toolBar_1->addAction(actionTime_Enabled);
        toolBar_1->addAction(actionCollisions_Enabled);
        toolBar_1->addAction(actionRegistrations_Open);
        toolBar_1->addAction(actionManageRobots);
        toolBar_1->addSeparator();
        toolBar_1->addAction(actionControl_Panel);
        toolBar_1->addAction(actionLaunch_Viewer);
        toolBar_2->addAction(actionEdit_Configuration);
        toolBar_2->addAction(actionOpen_Configuration);
        toolBar_2->addAction(actionSave_Configuration);
        toolBar_2->addAction(actionOpen_Lab);
        toolBar_2->addAction(actionLoad_Defaults);

        retranslateUi(cbSimulatorGUI);

        QMetaObject::connectSlotsByName(cbSimulatorGUI);
    } // setupUi

    void retranslateUi(QMainWindow *cbSimulatorGUI)
    {
        cbSimulatorGUI->setWindowTitle(QCoreApplication::translate("cbSimulatorGUI", "Explorer Simulator 2023", nullptr));
        actionReset->setText(QCoreApplication::translate("cbSimulatorGUI", "&Reset", nullptr));
#if QT_CONFIG(shortcut)
        actionReset->setShortcut(QCoreApplication::translate("cbSimulatorGUI", "Ctrl+R", nullptr));
#endif // QT_CONFIG(shortcut)
        actionSimulator_Help->setText(QCoreApplication::translate("cbSimulatorGUI", "&Help", nullptr));
#if QT_CONFIG(shortcut)
        actionSimulator_Help->setShortcut(QCoreApplication::translate("cbSimulatorGUI", "F1", nullptr));
#endif // QT_CONFIG(shortcut)
        actionAbout_Simulator->setText(QCoreApplication::translate("cbSimulatorGUI", "&About Simulator", nullptr));
        actionExit->setText(QCoreApplication::translate("cbSimulatorGUI", "E&xit", nullptr));
#if QT_CONFIG(shortcut)
        actionExit->setShortcut(QCoreApplication::translate("cbSimulatorGUI", "Ctrl+Q", nullptr));
#endif // QT_CONFIG(shortcut)
        actionGPS_Enabled->setText(QCoreApplication::translate("cbSimulatorGUI", "GP&S Enabled", nullptr));
#if QT_CONFIG(tooltip)
        actionGPS_Enabled->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Toggle GPS", nullptr));
#endif // QT_CONFIG(tooltip)
        actionScore_Sensor_Enabled->setText(QCoreApplication::translate("cbSimulatorGUI", "S&core Sensor Enabled", nullptr));
#if QT_CONFIG(tooltip)
        actionScore_Sensor_Enabled->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Toggle Score Sensor", nullptr));
#endif // QT_CONFIG(tooltip)
        actionTime_Enabled->setText(QCoreApplication::translate("cbSimulatorGUI", "T&ime Enabled", nullptr));
#if QT_CONFIG(tooltip)
        actionTime_Enabled->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Toggle Simulation Time Limit", nullptr));
#endif // QT_CONFIG(tooltip)
        actionOpen_Lab->setText(QCoreApplication::translate("cbSimulatorGUI", "Change &Lab", nullptr));
#if QT_CONFIG(tooltip)
        actionOpen_Lab->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Change Lab and Grid", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        actionOpen_Lab->setShortcut(QCoreApplication::translate("cbSimulatorGUI", "Ctrl+L", nullptr));
#endif // QT_CONFIG(shortcut)
        actionEdit_Configuration->setText(QCoreApplication::translate("cbSimulatorGUI", "&Edit Configuration", nullptr));
#if QT_CONFIG(shortcut)
        actionEdit_Configuration->setShortcut(QCoreApplication::translate("cbSimulatorGUI", "Ctrl+E", nullptr));
#endif // QT_CONFIG(shortcut)
        actionOpen_Configuration->setText(QCoreApplication::translate("cbSimulatorGUI", "Open &Configuration", nullptr));
        actionSave_Configuration->setText(QCoreApplication::translate("cbSimulatorGUI", "&Save Configuration", nullptr));
        actionLaunch_Viewer->setText(QCoreApplication::translate("cbSimulatorGUI", "Launch &Viewer", nullptr));
#if QT_CONFIG(shortcut)
        actionLaunch_Viewer->setShortcut(QCoreApplication::translate("cbSimulatorGUI", "Ctrl+V", nullptr));
#endif // QT_CONFIG(shortcut)
        actionRegistrations_Open->setText(QCoreApplication::translate("cbSimulatorGUI", "Re&gistrations Allowed", nullptr));
#if QT_CONFIG(tooltip)
        actionRegistrations_Open->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Toggle Robot Registrations", nullptr));
#endif // QT_CONFIG(tooltip)
        actionStartStop->setText(QCoreApplication::translate("cbSimulatorGUI", "&Start", nullptr));
#if QT_CONFIG(tooltip)
        actionStartStop->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Start", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        actionStartStop->setShortcut(QCoreApplication::translate("cbSimulatorGUI", "Ctrl+S", nullptr));
#endif // QT_CONFIG(shortcut)
        actionManageRobots->setText(QCoreApplication::translate("cbSimulatorGUI", "&Manage Robots", nullptr));
#if QT_CONFIG(tooltip)
        actionManageRobots->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Show Robots Management Window", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        actionManageRobots->setShortcut(QCoreApplication::translate("cbSimulatorGUI", "Ctrl+M", nullptr));
#endif // QT_CONFIG(shortcut)
        actionControl_Panel->setText(QCoreApplication::translate("cbSimulatorGUI", "Control &Panel", nullptr));
#if QT_CONFIG(tooltip)
        actionControl_Panel->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Show Control Panel Window", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        actionControl_Panel->setShortcut(QCoreApplication::translate("cbSimulatorGUI", "F2", nullptr));
#endif // QT_CONFIG(shortcut)
        actionLoad_Defaults->setText(QCoreApplication::translate("cbSimulatorGUI", "Load &Defaults", nullptr));
#if QT_CONFIG(tooltip)
        actionLoad_Defaults->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Sets Lab, Grid and Parameters to Default Values", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        actionLoad_Defaults->setShortcut(QCoreApplication::translate("cbSimulatorGUI", "Ctrl+D", nullptr));
#endif // QT_CONFIG(shortcut)
        actionCollisions_Enabled->setText(QCoreApplication::translate("cbSimulatorGUI", "Co&llisions Enabled", nullptr));
#if QT_CONFIG(tooltip)
        actionCollisions_Enabled->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Toggle Collisions between Robots", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        messages->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Messages", nullptr));
#endif // QT_CONFIG(tooltip)
        menuFile->setTitle(QCoreApplication::translate("cbSimulatorGUI", "&File", nullptr));
        menuConfiguration->setTitle(QCoreApplication::translate("cbSimulatorGUI", "&Configuration", nullptr));
        menuCommand->setTitle(QCoreApplication::translate("cbSimulatorGUI", "&Command", nullptr));
        menuOptions->setTitle(QCoreApplication::translate("cbSimulatorGUI", "&Options", nullptr));
        menuHelp->setTitle(QCoreApplication::translate("cbSimulatorGUI", "&Help", nullptr));
        toolBar_1->setWindowTitle(QCoreApplication::translate("cbSimulatorGUI", "Control ToolBar", nullptr));
        dockWidget_Score->setWindowTitle(QCoreApplication::translate("cbSimulatorGUI", "ScoreBoard", nullptr));
        label_2->setText(QCoreApplication::translate("cbSimulatorGUI", "Time remaining", nullptr));
#if QT_CONFIG(tooltip)
        lcdNumber_TimeRemain->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Time remaining", nullptr));
#endif // QT_CONFIG(tooltip)
        toolBar_2->setWindowTitle(QCoreApplication::translate("cbSimulatorGUI", "Settings ToolBar", nullptr));
        dockWidget_Mailbox->setWindowTitle(QCoreApplication::translate("cbSimulatorGUI", "Mailbox", nullptr));
        groupBox->setTitle(QCoreApplication::translate("cbSimulatorGUI", "Show messages", nullptr));
#if QT_CONFIG(tooltip)
        comboBox_Robot->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Robot", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        checkBox_Actions->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Motor Actions received from robot", nullptr));
#endif // QT_CONFIG(tooltip)
        checkBox_Actions->setText(QCoreApplication::translate("cbSimulatorGUI", "Actions received", nullptr));
#if QT_CONFIG(tooltip)
        checkBox_Measures->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Sensor Measures sent to robot", nullptr));
#endif // QT_CONFIG(tooltip)
        checkBox_Measures->setText(QCoreApplication::translate("cbSimulatorGUI", "Measures sent", nullptr));
#if QT_CONFIG(tooltip)
        checkBox_Positions->setToolTip(QCoreApplication::translate("cbSimulatorGUI", "Robot Positions sent to Viewer(s)", nullptr));
#endif // QT_CONFIG(tooltip)
        checkBox_Positions->setText(QCoreApplication::translate("cbSimulatorGUI", "Positions Sent", nullptr));
        label->setText(QCoreApplication::translate("cbSimulatorGUI", "relative to", nullptr));
        pushButton_ClearMailBox->setText(QCoreApplication::translate("cbSimulatorGUI", "Clear", nullptr));
    } // retranslateUi

};

namespace Ui {
    class cbSimulatorGUI: public Ui_cbSimulatorGUI {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CBSIMULATORGUI_H
