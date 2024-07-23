/********************************************************************************
** Form generated from reading UI file 'cbmanagerobots.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CBMANAGEROBOTS_H
#define UI_CBMANAGEROBOTS_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListView>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_cbManageRobots
{
public:
    QGridLayout *gridLayout;
    QGroupBox *groupBox_Agents;
    QGridLayout *gridLayout_2;
    QPushButton *pushButton_LoadAgent;
    QPushButton *pushButton_RemoveAgent;
    QListView *listView_Agents;
    QGroupBox *groupBox_Registered;
    QVBoxLayout *verticalLayout_2;
    QTableWidget *tableWidget_Robots;
    QPushButton *pushButton_DeleteRobot;
    QGroupBox *groupBox_AddRobot;
    QFormLayout *formLayout_1;
    QLabel *label_1;
    QLabel *label_Agent;
    QLabel *label_2;
    QLineEdit *lineEdit_Name;
    QLabel *label_3;
    QComboBox *comboBox_Position;
    QPushButton *pushButton_AddRobot;
    QPushButton *pushButton_Close;

    void setupUi(QWidget *cbManageRobots)
    {
        if (cbManageRobots->objectName().isEmpty())
            cbManageRobots->setObjectName(QString::fromUtf8("cbManageRobots"));
        cbManageRobots->resize(575, 323);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/images/buttons/mouse"), QSize(), QIcon::Normal, QIcon::Off);
        cbManageRobots->setWindowIcon(icon);
        gridLayout = new QGridLayout(cbManageRobots);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        groupBox_Agents = new QGroupBox(cbManageRobots);
        groupBox_Agents->setObjectName(QString::fromUtf8("groupBox_Agents"));
        gridLayout_2 = new QGridLayout(groupBox_Agents);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        pushButton_LoadAgent = new QPushButton(groupBox_Agents);
        pushButton_LoadAgent->setObjectName(QString::fromUtf8("pushButton_LoadAgent"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/images/buttons/open"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_LoadAgent->setIcon(icon1);

        gridLayout_2->addWidget(pushButton_LoadAgent, 0, 0, 1, 1);

        pushButton_RemoveAgent = new QPushButton(groupBox_Agents);
        pushButton_RemoveAgent->setObjectName(QString::fromUtf8("pushButton_RemoveAgent"));
        pushButton_RemoveAgent->setEnabled(false);
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/images/buttons/delete"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_RemoveAgent->setIcon(icon2);

        gridLayout_2->addWidget(pushButton_RemoveAgent, 0, 1, 1, 1);

        listView_Agents = new QListView(groupBox_Agents);
        listView_Agents->setObjectName(QString::fromUtf8("listView_Agents"));
        listView_Agents->setEditTriggers(QAbstractItemView::NoEditTriggers);

        gridLayout_2->addWidget(listView_Agents, 1, 0, 1, 2);


        gridLayout->addWidget(groupBox_Agents, 0, 0, 1, 1);

        groupBox_Registered = new QGroupBox(cbManageRobots);
        groupBox_Registered->setObjectName(QString::fromUtf8("groupBox_Registered"));
        verticalLayout_2 = new QVBoxLayout(groupBox_Registered);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        tableWidget_Robots = new QTableWidget(groupBox_Registered);
        tableWidget_Robots->setObjectName(QString::fromUtf8("tableWidget_Robots"));
        tableWidget_Robots->setAutoFillBackground(true);
        tableWidget_Robots->setSelectionMode(QAbstractItemView::ExtendedSelection);
        tableWidget_Robots->setSelectionBehavior(QAbstractItemView::SelectRows);
        tableWidget_Robots->setShowGrid(false);
        tableWidget_Robots->setCornerButtonEnabled(false);
        tableWidget_Robots->horizontalHeader()->setCascadingSectionResizes(true);
        tableWidget_Robots->horizontalHeader()->setHighlightSections(false);
        tableWidget_Robots->horizontalHeader()->setStretchLastSection(true);
        tableWidget_Robots->verticalHeader()->setVisible(false);
        tableWidget_Robots->verticalHeader()->setCascadingSectionResizes(true);

        verticalLayout_2->addWidget(tableWidget_Robots);

        pushButton_DeleteRobot = new QPushButton(groupBox_Registered);
        pushButton_DeleteRobot->setObjectName(QString::fromUtf8("pushButton_DeleteRobot"));
        pushButton_DeleteRobot->setEnabled(false);
        pushButton_DeleteRobot->setIcon(icon2);

        verticalLayout_2->addWidget(pushButton_DeleteRobot);


        gridLayout->addWidget(groupBox_Registered, 0, 1, 2, 1);

        groupBox_AddRobot = new QGroupBox(cbManageRobots);
        groupBox_AddRobot->setObjectName(QString::fromUtf8("groupBox_AddRobot"));
        groupBox_AddRobot->setEnabled(false);
        formLayout_1 = new QFormLayout(groupBox_AddRobot);
        formLayout_1->setObjectName(QString::fromUtf8("formLayout_1"));
        formLayout_1->setFieldGrowthPolicy(QFormLayout::AllNonFixedFieldsGrow);
        label_1 = new QLabel(groupBox_AddRobot);
        label_1->setObjectName(QString::fromUtf8("label_1"));

        formLayout_1->setWidget(0, QFormLayout::LabelRole, label_1);

        label_Agent = new QLabel(groupBox_AddRobot);
        label_Agent->setObjectName(QString::fromUtf8("label_Agent"));

        formLayout_1->setWidget(0, QFormLayout::FieldRole, label_Agent);

        label_2 = new QLabel(groupBox_AddRobot);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        formLayout_1->setWidget(1, QFormLayout::LabelRole, label_2);

        lineEdit_Name = new QLineEdit(groupBox_AddRobot);
        lineEdit_Name->setObjectName(QString::fromUtf8("lineEdit_Name"));

        formLayout_1->setWidget(1, QFormLayout::FieldRole, lineEdit_Name);

        label_3 = new QLabel(groupBox_AddRobot);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        formLayout_1->setWidget(2, QFormLayout::LabelRole, label_3);

        comboBox_Position = new QComboBox(groupBox_AddRobot);
        comboBox_Position->setObjectName(QString::fromUtf8("comboBox_Position"));
        comboBox_Position->setInsertPolicy(QComboBox::InsertAlphabetically);

        formLayout_1->setWidget(2, QFormLayout::FieldRole, comboBox_Position);

        pushButton_AddRobot = new QPushButton(groupBox_AddRobot);
        pushButton_AddRobot->setObjectName(QString::fromUtf8("pushButton_AddRobot"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/images/buttons/add"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_AddRobot->setIcon(icon3);

        formLayout_1->setWidget(3, QFormLayout::SpanningRole, pushButton_AddRobot);


        gridLayout->addWidget(groupBox_AddRobot, 1, 0, 1, 1);

        pushButton_Close = new QPushButton(cbManageRobots);
        pushButton_Close->setObjectName(QString::fromUtf8("pushButton_Close"));

        gridLayout->addWidget(pushButton_Close, 2, 0, 1, 2);


        retranslateUi(cbManageRobots);
        QObject::connect(lineEdit_Name, SIGNAL(returnPressed()), pushButton_AddRobot, SLOT(click()));
        QObject::connect(pushButton_Close, SIGNAL(clicked()), cbManageRobots, SLOT(close()));

        QMetaObject::connectSlotsByName(cbManageRobots);
    } // setupUi

    void retranslateUi(QWidget *cbManageRobots)
    {
        cbManageRobots->setWindowTitle(QCoreApplication::translate("cbManageRobots", "Manage Robots", nullptr));
        groupBox_Agents->setTitle(QCoreApplication::translate("cbManageRobots", "Select a Robotic Agent", nullptr));
        pushButton_LoadAgent->setText(QCoreApplication::translate("cbManageRobots", "Load Agent", nullptr));
        pushButton_RemoveAgent->setText(QCoreApplication::translate("cbManageRobots", "Remove Selected", nullptr));
        groupBox_Registered->setTitle(QCoreApplication::translate("cbManageRobots", "Registered Robots", nullptr));
        pushButton_DeleteRobot->setText(QCoreApplication::translate("cbManageRobots", "Delete Selected Robot(s)", nullptr));
        groupBox_AddRobot->setTitle(QCoreApplication::translate("cbManageRobots", "Add Robot", nullptr));
        label_1->setText(QCoreApplication::translate("cbManageRobots", "Agent", nullptr));
        label_Agent->setText(QCoreApplication::translate("cbManageRobots", "NO AGENT SELECTED", nullptr));
        label_2->setText(QCoreApplication::translate("cbManageRobots", "Name", nullptr));
        label_3->setText(QCoreApplication::translate("cbManageRobots", "Position", nullptr));
        pushButton_AddRobot->setText(QCoreApplication::translate("cbManageRobots", "Add Robot", nullptr));
        pushButton_Close->setText(QCoreApplication::translate("cbManageRobots", "Hide", nullptr));
    } // retranslateUi

};

namespace Ui {
    class cbManageRobots: public Ui_cbManageRobots {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CBMANAGEROBOTS_H
