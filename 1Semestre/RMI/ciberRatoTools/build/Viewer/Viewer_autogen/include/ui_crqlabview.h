/********************************************************************************
** Form generated from reading UI file 'crqlabview.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CRQLABVIEW_H
#define UI_CRQLABVIEW_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDockWidget>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_CRQLabView
{
public:
    QAction *actionAbout;
    QAction *actionReset_Viewer;
    QAction *actionConnect;
    QAction *actionExit;
    QAction *actionLower_walls_color;
    QAction *actionHigher_walls_collor;
    QAction *actionSound_On_Off;
    QAction *actionChange_skin;
    QAction *actionHelp;
    QAction *actionStart;
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_Central;
    QGraphicsView *graphicsView_lab;
    QMenuBar *menubar;
    QMenu *menuFile;
    QMenu *menuHelp;
    QMenu *menuOptions;
    QToolBar *toolBar;
    QDockWidget *dockWidget_Score;
    QWidget *dockWidgetContents_Score;
    QVBoxLayout *verticalLayout;
    QVBoxLayout *scoreLayout;

    void setupUi(QMainWindow *CRQLabView)
    {
        if (CRQLabView->objectName().isEmpty())
            CRQLabView->setObjectName(QString::fromUtf8("CRQLabView"));
        CRQLabView->resize(800, 600);
        actionAbout = new QAction(CRQLabView);
        actionAbout->setObjectName(QString::fromUtf8("actionAbout"));
        actionReset_Viewer = new QAction(CRQLabView);
        actionReset_Viewer->setObjectName(QString::fromUtf8("actionReset_Viewer"));
        actionConnect = new QAction(CRQLabView);
        actionConnect->setObjectName(QString::fromUtf8("actionConnect"));
        actionConnect->setCheckable(true);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/images/buttons/disconnect"), QSize(), QIcon::Normal, QIcon::Off);
        icon.addFile(QString::fromUtf8(":/images/buttons/connect"), QSize(), QIcon::Normal, QIcon::On);
        actionConnect->setIcon(icon);
        actionExit = new QAction(CRQLabView);
        actionExit->setObjectName(QString::fromUtf8("actionExit"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/images/buttons/exit"), QSize(), QIcon::Normal, QIcon::Off);
        actionExit->setIcon(icon1);
        actionLower_walls_color = new QAction(CRQLabView);
        actionLower_walls_color->setObjectName(QString::fromUtf8("actionLower_walls_color"));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/images/buttons/color_low"), QSize(), QIcon::Normal, QIcon::Off);
        actionLower_walls_color->setIcon(icon2);
        actionHigher_walls_collor = new QAction(CRQLabView);
        actionHigher_walls_collor->setObjectName(QString::fromUtf8("actionHigher_walls_collor"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/images/buttons/color_high"), QSize(), QIcon::Normal, QIcon::Off);
        actionHigher_walls_collor->setIcon(icon3);
        actionSound_On_Off = new QAction(CRQLabView);
        actionSound_On_Off->setObjectName(QString::fromUtf8("actionSound_On_Off"));
        actionSound_On_Off->setCheckable(true);
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/images/buttons/sound_on"), QSize(), QIcon::Normal, QIcon::Off);
        icon4.addFile(QString::fromUtf8(":/images/buttons/sound_off"), QSize(), QIcon::Normal, QIcon::On);
        actionSound_On_Off->setIcon(icon4);
        actionChange_skin = new QAction(CRQLabView);
        actionChange_skin->setObjectName(QString::fromUtf8("actionChange_skin"));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/images/buttons/skin"), QSize(), QIcon::Normal, QIcon::Off);
        actionChange_skin->setIcon(icon5);
        actionHelp = new QAction(CRQLabView);
        actionHelp->setObjectName(QString::fromUtf8("actionHelp"));
        actionStart = new QAction(CRQLabView);
        actionStart->setObjectName(QString::fromUtf8("actionStart"));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/images/control/start"), QSize(), QIcon::Normal, QIcon::On);
        actionStart->setIcon(icon6);
        centralwidget = new QWidget(CRQLabView);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout_Central = new QVBoxLayout(centralwidget);
        verticalLayout_Central->setContentsMargins(0, 0, 0, 0);
        verticalLayout_Central->setObjectName(QString::fromUtf8("verticalLayout_Central"));
        graphicsView_lab = new QGraphicsView(centralwidget);
        graphicsView_lab->setObjectName(QString::fromUtf8("graphicsView_lab"));
        graphicsView_lab->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        graphicsView_lab->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);

        verticalLayout_Central->addWidget(graphicsView_lab);

        CRQLabView->setCentralWidget(centralwidget);
        menubar = new QMenuBar(CRQLabView);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 800, 25));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QString::fromUtf8("menuFile"));
        menuHelp = new QMenu(menubar);
        menuHelp->setObjectName(QString::fromUtf8("menuHelp"));
        menuOptions = new QMenu(menubar);
        menuOptions->setObjectName(QString::fromUtf8("menuOptions"));
        CRQLabView->setMenuBar(menubar);
        toolBar = new QToolBar(CRQLabView);
        toolBar->setObjectName(QString::fromUtf8("toolBar"));
        CRQLabView->addToolBar(Qt::TopToolBarArea, toolBar);
        dockWidget_Score = new QDockWidget(CRQLabView);
        dockWidget_Score->setObjectName(QString::fromUtf8("dockWidget_Score"));
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/window/scores"), QSize(), QIcon::Normal, QIcon::Off);
        dockWidget_Score->setWindowIcon(icon7);
        dockWidgetContents_Score = new QWidget();
        dockWidgetContents_Score->setObjectName(QString::fromUtf8("dockWidgetContents_Score"));
        verticalLayout = new QVBoxLayout(dockWidgetContents_Score);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        scoreLayout = new QVBoxLayout();
        scoreLayout->setObjectName(QString::fromUtf8("scoreLayout"));

        verticalLayout->addLayout(scoreLayout);

        dockWidget_Score->setWidget(dockWidgetContents_Score);
        CRQLabView->addDockWidget(Qt::BottomDockWidgetArea, dockWidget_Score);

        menubar->addAction(menuFile->menuAction());
        menubar->addAction(menuOptions->menuAction());
        menubar->addAction(menuHelp->menuAction());
        menuFile->addAction(actionConnect);
        menuFile->addSeparator();
        menuFile->addAction(actionExit);
        menuHelp->addAction(actionHelp);
        menuHelp->addAction(actionAbout);
        menuOptions->addAction(actionChange_skin);
        menuOptions->addAction(actionLower_walls_color);
        menuOptions->addAction(actionHigher_walls_collor);
        menuOptions->addSeparator();
        menuOptions->addAction(actionSound_On_Off);
        toolBar->addAction(actionConnect);
        toolBar->addSeparator();
        toolBar->addAction(actionStart);
        toolBar->addAction(actionChange_skin);
        toolBar->addAction(actionHigher_walls_collor);
        toolBar->addAction(actionLower_walls_color);
        toolBar->addSeparator();
        toolBar->addAction(actionSound_On_Off);

        retranslateUi(CRQLabView);
        QObject::connect(actionExit, SIGNAL(triggered()), CRQLabView, SLOT(close()));

        QMetaObject::connectSlotsByName(CRQLabView);
    } // setupUi

    void retranslateUi(QMainWindow *CRQLabView)
    {
        CRQLabView->setWindowTitle(QCoreApplication::translate("CRQLabView", "MainWindow", nullptr));
        actionAbout->setText(QCoreApplication::translate("CRQLabView", "&About...", nullptr));
        actionReset_Viewer->setText(QCoreApplication::translate("CRQLabView", "&Reset Viewer", nullptr));
#if QT_CONFIG(shortcut)
        actionReset_Viewer->setShortcut(QCoreApplication::translate("CRQLabView", "Ctrl+R", nullptr));
#endif // QT_CONFIG(shortcut)
        actionConnect->setText(QCoreApplication::translate("CRQLabView", "&Connect", nullptr));
#if QT_CONFIG(tooltip)
        actionConnect->setToolTip(QCoreApplication::translate("CRQLabView", "Connect", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        actionConnect->setShortcut(QCoreApplication::translate("CRQLabView", "Ctrl+C", nullptr));
#endif // QT_CONFIG(shortcut)
        actionExit->setText(QCoreApplication::translate("CRQLabView", "E&xit", nullptr));
#if QT_CONFIG(shortcut)
        actionExit->setShortcut(QCoreApplication::translate("CRQLabView", "Ctrl+Q", nullptr));
#endif // QT_CONFIG(shortcut)
        actionLower_walls_color->setText(QCoreApplication::translate("CRQLabView", "&Lower walls color", nullptr));
#if QT_CONFIG(shortcut)
        actionLower_walls_color->setShortcut(QCoreApplication::translate("CRQLabView", "Ctrl+L", nullptr));
#endif // QT_CONFIG(shortcut)
        actionHigher_walls_collor->setText(QCoreApplication::translate("CRQLabView", "&Higher walls collor", nullptr));
#if QT_CONFIG(shortcut)
        actionHigher_walls_collor->setShortcut(QCoreApplication::translate("CRQLabView", "Ctrl+H", nullptr));
#endif // QT_CONFIG(shortcut)
        actionSound_On_Off->setText(QCoreApplication::translate("CRQLabView", "&Sound is on", nullptr));
#if QT_CONFIG(tooltip)
        actionSound_On_Off->setToolTip(QCoreApplication::translate("CRQLabView", "Mute", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        actionSound_On_Off->setShortcut(QCoreApplication::translate("CRQLabView", "Ctrl+S", nullptr));
#endif // QT_CONFIG(shortcut)
        actionChange_skin->setText(QCoreApplication::translate("CRQLabView", "Change s&kin", nullptr));
#if QT_CONFIG(tooltip)
        actionChange_skin->setToolTip(QCoreApplication::translate("CRQLabView", "Change skin", nullptr));
#endif // QT_CONFIG(tooltip)
        actionHelp->setText(QCoreApplication::translate("CRQLabView", "&Help", nullptr));
#if QT_CONFIG(shortcut)
        actionHelp->setShortcut(QCoreApplication::translate("CRQLabView", "F1", nullptr));
#endif // QT_CONFIG(shortcut)
        actionStart->setText(QCoreApplication::translate("CRQLabView", "Start", nullptr));
#if QT_CONFIG(tooltip)
        actionStart->setToolTip(QCoreApplication::translate("CRQLabView", "Start", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        actionStart->setShortcut(QCoreApplication::translate("CRQLabView", "Ctrl+G", nullptr));
#endif // QT_CONFIG(shortcut)
        menuFile->setTitle(QCoreApplication::translate("CRQLabView", "&File", nullptr));
        menuHelp->setTitle(QCoreApplication::translate("CRQLabView", "&Help", nullptr));
        menuOptions->setTitle(QCoreApplication::translate("CRQLabView", "&Options", nullptr));
        toolBar->setWindowTitle(QCoreApplication::translate("CRQLabView", "ToolBar", nullptr));
        dockWidget_Score->setWindowTitle(QCoreApplication::translate("CRQLabView", "ScoreBoard", nullptr));
    } // retranslateUi

};

namespace Ui {
    class CRQLabView: public Ui_CRQLabView {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CRQLABVIEW_H
