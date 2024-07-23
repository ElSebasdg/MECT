/********************************************************************************
** Form generated from reading UI file 'cbrobotinfo.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CBROBOTINFO_H
#define UI_CBROBOTINFO_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_cbRobotInfo
{
public:
    QHBoxLayout *horizontalLayout;
    QLCDNumber *lcdNumber_ID;
    QLabel *label_Name;
    QLCDNumber *lcdNumber_Time;
    QLCDNumber *lcdNumber_Collisions;
    QLabel *label_State;
    QLCDNumber *lcdNumber_Score;

    void setupUi(QWidget *cbRobotInfo)
    {
        if (cbRobotInfo->objectName().isEmpty())
            cbRobotInfo->setObjectName(QString::fromUtf8("cbRobotInfo"));
        cbRobotInfo->resize(392, 32);
        cbRobotInfo->setMinimumSize(QSize(0, 32));
        cbRobotInfo->setMaximumSize(QSize(16777215, 32));
        horizontalLayout = new QHBoxLayout(cbRobotInfo);
        horizontalLayout->setSpacing(10);
        horizontalLayout->setContentsMargins(4, 4, 4, 4);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        lcdNumber_ID = new QLCDNumber(cbRobotInfo);
        lcdNumber_ID->setObjectName(QString::fromUtf8("lcdNumber_ID"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(lcdNumber_ID->sizePolicy().hasHeightForWidth());
        lcdNumber_ID->setSizePolicy(sizePolicy);
        lcdNumber_ID->setMinimumSize(QSize(30, 0));
        lcdNumber_ID->setMaximumSize(QSize(30, 16777215));
        lcdNumber_ID->setFrameShape(QFrame::NoFrame);
        lcdNumber_ID->setDigitCount(1);
        lcdNumber_ID->setSegmentStyle(QLCDNumber::Outline);

        horizontalLayout->addWidget(lcdNumber_ID);

        label_Name = new QLabel(cbRobotInfo);
        label_Name->setObjectName(QString::fromUtf8("label_Name"));
        QSizePolicy sizePolicy1(QSizePolicy::MinimumExpanding, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(label_Name->sizePolicy().hasHeightForWidth());
        label_Name->setSizePolicy(sizePolicy1);
        label_Name->setMinimumSize(QSize(100, 0));
        QFont font;
        font.setFamily(QString::fromUtf8("Courier"));
        font.setPointSize(14);
        font.setBold(true);
        font.setWeight(75);
        label_Name->setFont(font);

        horizontalLayout->addWidget(label_Name);

        lcdNumber_Time = new QLCDNumber(cbRobotInfo);
        lcdNumber_Time->setObjectName(QString::fromUtf8("lcdNumber_Time"));
        sizePolicy.setHeightForWidth(lcdNumber_Time->sizePolicy().hasHeightForWidth());
        lcdNumber_Time->setSizePolicy(sizePolicy);
        lcdNumber_Time->setMinimumSize(QSize(60, 0));
        lcdNumber_Time->setMaximumSize(QSize(60, 16777215));
        lcdNumber_Time->setFrameShape(QFrame::NoFrame);
        lcdNumber_Time->setDigitCount(4);
        lcdNumber_Time->setSegmentStyle(QLCDNumber::Flat);

        horizontalLayout->addWidget(lcdNumber_Time);

        lcdNumber_Collisions = new QLCDNumber(cbRobotInfo);
        lcdNumber_Collisions->setObjectName(QString::fromUtf8("lcdNumber_Collisions"));
        sizePolicy.setHeightForWidth(lcdNumber_Collisions->sizePolicy().hasHeightForWidth());
        lcdNumber_Collisions->setSizePolicy(sizePolicy);
        lcdNumber_Collisions->setMinimumSize(QSize(60, 0));
        lcdNumber_Collisions->setMaximumSize(QSize(60, 16777215));
        QPalette palette;
        QBrush brush(QColor(255, 85, 0, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::WindowText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        QBrush brush1(QColor(120, 120, 120, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Disabled, QPalette::WindowText, brush1);
        lcdNumber_Collisions->setPalette(palette);
        lcdNumber_Collisions->setFrameShape(QFrame::NoFrame);
        lcdNumber_Collisions->setDigitCount(3);
        lcdNumber_Collisions->setSegmentStyle(QLCDNumber::Flat);

        horizontalLayout->addWidget(lcdNumber_Collisions);

        label_State = new QLabel(cbRobotInfo);
        label_State->setObjectName(QString::fromUtf8("label_State"));
        QSizePolicy sizePolicy2(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(label_State->sizePolicy().hasHeightForWidth());
        label_State->setSizePolicy(sizePolicy2);
        label_State->setMinimumSize(QSize(24, 24));
        label_State->setMaximumSize(QSize(24, 24));

        horizontalLayout->addWidget(label_State);

        lcdNumber_Score = new QLCDNumber(cbRobotInfo);
        lcdNumber_Score->setObjectName(QString::fromUtf8("lcdNumber_Score"));
        sizePolicy.setHeightForWidth(lcdNumber_Score->sizePolicy().hasHeightForWidth());
        lcdNumber_Score->setSizePolicy(sizePolicy);
        lcdNumber_Score->setMinimumSize(QSize(60, 0));
        lcdNumber_Score->setMaximumSize(QSize(60, 16777215));
        lcdNumber_Score->setFrameShape(QFrame::Panel);
        lcdNumber_Score->setFrameShadow(QFrame::Raised);
        lcdNumber_Score->setDigitCount(4);
        lcdNumber_Score->setSegmentStyle(QLCDNumber::Flat);

        horizontalLayout->addWidget(lcdNumber_Score);


        retranslateUi(cbRobotInfo);

        QMetaObject::connectSlotsByName(cbRobotInfo);
    } // setupUi

    void retranslateUi(QWidget *cbRobotInfo)
    {
        cbRobotInfo->setWindowTitle(QCoreApplication::translate("cbRobotInfo", "Robot Info", nullptr));
#if QT_CONFIG(statustip)
        lcdNumber_ID->setStatusTip(QCoreApplication::translate("cbRobotInfo", "Robot ID", nullptr));
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        label_Name->setToolTip(QCoreApplication::translate("cbRobotInfo", "Robot name", nullptr));
#endif // QT_CONFIG(tooltip)
        label_Name->setText(QCoreApplication::translate("cbRobotInfo", "RobName", nullptr));
#if QT_CONFIG(tooltip)
        lcdNumber_Time->setToolTip(QCoreApplication::translate("cbRobotInfo", "Time", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        lcdNumber_Collisions->setToolTip(QCoreApplication::translate("cbRobotInfo", "Collisions", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        label_State->setToolTip(QCoreApplication::translate("cbRobotInfo", "Status", nullptr));
#endif // QT_CONFIG(tooltip)
        label_State->setText(QString());
#if QT_CONFIG(tooltip)
        lcdNumber_Score->setToolTip(QCoreApplication::translate("cbRobotInfo", "Score", nullptr));
#endif // QT_CONFIG(tooltip)
    } // retranslateUi

};

namespace Ui {
    class cbRobotInfo: public Ui_cbRobotInfo {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CBROBOTINFO_H
