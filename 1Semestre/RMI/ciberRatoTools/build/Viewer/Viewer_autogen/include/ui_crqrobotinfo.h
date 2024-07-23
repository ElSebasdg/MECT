/********************************************************************************
** Form generated from reading UI file 'crqrobotinfo.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CRQROBOTINFO_H
#define UI_CRQROBOTINFO_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_CRQRobotInfo
{
public:
    QHBoxLayout *horizontalLayout;
    QLabel *label_Icon;
    QLCDNumber *lcdNumber_ID;
    QLabel *label_Name;
    QLCDNumber *lcdNumber_Time;
    QLCDNumber *lcdNumber_Collisions;
    QLabel *label_State;
    QLCDNumber *lcdNumber_Score;

    void setupUi(QWidget *CRQRobotInfo)
    {
        if (CRQRobotInfo->objectName().isEmpty())
            CRQRobotInfo->setObjectName(QString::fromUtf8("CRQRobotInfo"));
        CRQRobotInfo->resize(462, 28);
        CRQRobotInfo->setMaximumSize(QSize(16777215, 28));
        horizontalLayout = new QHBoxLayout(CRQRobotInfo);
        horizontalLayout->setSpacing(10);
        horizontalLayout->setContentsMargins(2, 2, 2, 2);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label_Icon = new QLabel(CRQRobotInfo);
        label_Icon->setObjectName(QString::fromUtf8("label_Icon"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(label_Icon->sizePolicy().hasHeightForWidth());
        label_Icon->setSizePolicy(sizePolicy);
        label_Icon->setMinimumSize(QSize(24, 24));
        label_Icon->setMaximumSize(QSize(24, 24));
        label_Icon->setAlignment(Qt::AlignCenter);

        horizontalLayout->addWidget(label_Icon);

        lcdNumber_ID = new QLCDNumber(CRQRobotInfo);
        lcdNumber_ID->setObjectName(QString::fromUtf8("lcdNumber_ID"));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Minimum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(lcdNumber_ID->sizePolicy().hasHeightForWidth());
        lcdNumber_ID->setSizePolicy(sizePolicy1);
        lcdNumber_ID->setMinimumSize(QSize(30, 0));
        lcdNumber_ID->setMaximumSize(QSize(30, 16777215));
        lcdNumber_ID->setFrameShape(QFrame::NoFrame);
        lcdNumber_ID->setDigitCount(1);
        lcdNumber_ID->setSegmentStyle(QLCDNumber::Outline);

        horizontalLayout->addWidget(lcdNumber_ID);

        label_Name = new QLabel(CRQRobotInfo);
        label_Name->setObjectName(QString::fromUtf8("label_Name"));
        QSizePolicy sizePolicy2(QSizePolicy::MinimumExpanding, QSizePolicy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(label_Name->sizePolicy().hasHeightForWidth());
        label_Name->setSizePolicy(sizePolicy2);
        label_Name->setMinimumSize(QSize(100, 0));
        QFont font;
        font.setFamily(QString::fromUtf8("Courier"));
        font.setPointSize(14);
        font.setBold(true);
        font.setWeight(75);
        label_Name->setFont(font);

        horizontalLayout->addWidget(label_Name);

        lcdNumber_Time = new QLCDNumber(CRQRobotInfo);
        lcdNumber_Time->setObjectName(QString::fromUtf8("lcdNumber_Time"));
        sizePolicy1.setHeightForWidth(lcdNumber_Time->sizePolicy().hasHeightForWidth());
        lcdNumber_Time->setSizePolicy(sizePolicy1);
        lcdNumber_Time->setMinimumSize(QSize(70, 0));
        lcdNumber_Time->setMaximumSize(QSize(70, 16777215));
        lcdNumber_Time->setFrameShape(QFrame::NoFrame);
        lcdNumber_Time->setDigitCount(4);
        lcdNumber_Time->setSegmentStyle(QLCDNumber::Flat);

        horizontalLayout->addWidget(lcdNumber_Time);

        lcdNumber_Collisions = new QLCDNumber(CRQRobotInfo);
        lcdNumber_Collisions->setObjectName(QString::fromUtf8("lcdNumber_Collisions"));
        sizePolicy1.setHeightForWidth(lcdNumber_Collisions->sizePolicy().hasHeightForWidth());
        lcdNumber_Collisions->setSizePolicy(sizePolicy1);
        lcdNumber_Collisions->setMinimumSize(QSize(70, 0));
        lcdNumber_Collisions->setMaximumSize(QSize(70, 16777215));
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

        label_State = new QLabel(CRQRobotInfo);
        label_State->setObjectName(QString::fromUtf8("label_State"));
        sizePolicy.setHeightForWidth(label_State->sizePolicy().hasHeightForWidth());
        label_State->setSizePolicy(sizePolicy);
        label_State->setMinimumSize(QSize(24, 24));
        label_State->setMaximumSize(QSize(24, 24));
        label_State->setAlignment(Qt::AlignCenter);

        horizontalLayout->addWidget(label_State);

        lcdNumber_Score = new QLCDNumber(CRQRobotInfo);
        lcdNumber_Score->setObjectName(QString::fromUtf8("lcdNumber_Score"));
        sizePolicy1.setHeightForWidth(lcdNumber_Score->sizePolicy().hasHeightForWidth());
        lcdNumber_Score->setSizePolicy(sizePolicy1);
        lcdNumber_Score->setMinimumSize(QSize(80, 0));
        lcdNumber_Score->setMaximumSize(QSize(80, 16777215));
        lcdNumber_Score->setFrameShape(QFrame::Panel);
        lcdNumber_Score->setDigitCount(5);
        lcdNumber_Score->setSegmentStyle(QLCDNumber::Flat);

        horizontalLayout->addWidget(lcdNumber_Score);


        retranslateUi(CRQRobotInfo);

        QMetaObject::connectSlotsByName(CRQRobotInfo);
    } // setupUi

    void retranslateUi(QWidget *CRQRobotInfo)
    {
        CRQRobotInfo->setWindowTitle(QCoreApplication::translate("CRQRobotInfo", "Form", nullptr));
#if QT_CONFIG(tooltip)
        label_Icon->setToolTip(QCoreApplication::translate("CRQRobotInfo", "Robot Icon", nullptr));
#endif // QT_CONFIG(tooltip)
        label_Icon->setText(QString());
#if QT_CONFIG(tooltip)
        lcdNumber_ID->setToolTip(QCoreApplication::translate("CRQRobotInfo", "Robot ID", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        label_Name->setToolTip(QCoreApplication::translate("CRQRobotInfo", "Robot name", nullptr));
#endif // QT_CONFIG(tooltip)
        label_Name->setText(QCoreApplication::translate("CRQRobotInfo", "RobName", nullptr));
#if QT_CONFIG(tooltip)
        lcdNumber_Time->setToolTip(QCoreApplication::translate("CRQRobotInfo", "Time", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        lcdNumber_Collisions->setToolTip(QCoreApplication::translate("CRQRobotInfo", "Collisions", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        label_State->setToolTip(QCoreApplication::translate("CRQRobotInfo", "Status", nullptr));
#endif // QT_CONFIG(tooltip)
        label_State->setText(QString());
#if QT_CONFIG(tooltip)
        lcdNumber_Score->setToolTip(QCoreApplication::translate("CRQRobotInfo", "Score", nullptr));
#endif // QT_CONFIG(tooltip)
    } // retranslateUi

};

namespace Ui {
    class CRQRobotInfo: public Ui_CRQRobotInfo {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CRQROBOTINFO_H
