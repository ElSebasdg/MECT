/********************************************************************************
** Form generated from reading UI file 'crqdataview.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CRQDATAVIEW_H
#define UI_CRQDATAVIEW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_CRQDataView
{
public:
    QGridLayout *gridLayout_2;
    QGridLayout *gridLayout_Robots;
    QSpacerItem *horizontalSpacer;
    QSpacerItem *verticalSpacer;
    QLCDNumber *lcdNumber_Time;
    QLabel *label_Time;
    QLabel *label_Lab;
    QSpacerItem *horizontalSpacer_2;
    QLabel *label_2;
    QLabel *label_5;
    QLabel *label_3;
    QLabel *label_4;

    void setupUi(QWidget *CRQDataView)
    {
        if (CRQDataView->objectName().isEmpty())
            CRQDataView->setObjectName(QString::fromUtf8("CRQDataView"));
        CRQDataView->resize(714, 129);
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(CRQDataView->sizePolicy().hasHeightForWidth());
        CRQDataView->setSizePolicy(sizePolicy);
        gridLayout_2 = new QGridLayout(CRQDataView);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout_Robots = new QGridLayout();
        gridLayout_Robots->setSpacing(2);
        gridLayout_Robots->setObjectName(QString::fromUtf8("gridLayout_Robots"));

        gridLayout_2->addLayout(gridLayout_Robots, 3, 2, 2, 5);

        horizontalSpacer = new QSpacerItem(20, 1, QSizePolicy::MinimumExpanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer, 3, 1, 1, 1);

        verticalSpacer = new QSpacerItem(1, 0, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_2->addItem(verticalSpacer, 4, 0, 1, 1);

        lcdNumber_Time = new QLCDNumber(CRQDataView);
        lcdNumber_Time->setObjectName(QString::fromUtf8("lcdNumber_Time"));
        lcdNumber_Time->setMinimumSize(QSize(200, 40));
        QPalette palette;
        QBrush brush(QColor(0, 0, 0, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::WindowText, brush);
        QBrush brush1(QColor(0, 0, 200, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Button, brush1);
        QBrush brush2(QColor(45, 45, 255, 255));
        brush2.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Light, brush2);
        QBrush brush3(QColor(22, 22, 227, 255));
        brush3.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Midlight, brush3);
        QBrush brush4(QColor(0, 0, 100, 255));
        brush4.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Dark, brush4);
        QBrush brush5(QColor(0, 0, 133, 255));
        brush5.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Mid, brush5);
        palette.setBrush(QPalette::Active, QPalette::Text, brush);
        QBrush brush6(QColor(255, 255, 255, 255));
        brush6.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::BrightText, brush6);
        palette.setBrush(QPalette::Active, QPalette::ButtonText, brush);
        palette.setBrush(QPalette::Active, QPalette::Base, brush6);
        palette.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette.setBrush(QPalette::Active, QPalette::Shadow, brush);
        QBrush brush7(QColor(127, 127, 227, 255));
        brush7.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::AlternateBase, brush7);
        QBrush brush8(QColor(255, 255, 220, 255));
        brush8.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::ToolTipBase, brush8);
        palette.setBrush(QPalette::Active, QPalette::ToolTipText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Button, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Light, brush2);
        palette.setBrush(QPalette::Inactive, QPalette::Midlight, brush3);
        palette.setBrush(QPalette::Inactive, QPalette::Dark, brush4);
        palette.setBrush(QPalette::Inactive, QPalette::Mid, brush5);
        palette.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette.setBrush(QPalette::Inactive, QPalette::BrightText, brush6);
        palette.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Base, brush6);
        palette.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Shadow, brush);
        palette.setBrush(QPalette::Inactive, QPalette::AlternateBase, brush7);
        palette.setBrush(QPalette::Inactive, QPalette::ToolTipBase, brush8);
        palette.setBrush(QPalette::Inactive, QPalette::ToolTipText, brush);
        palette.setBrush(QPalette::Disabled, QPalette::WindowText, brush4);
        palette.setBrush(QPalette::Disabled, QPalette::Button, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Light, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::Midlight, brush3);
        palette.setBrush(QPalette::Disabled, QPalette::Dark, brush4);
        palette.setBrush(QPalette::Disabled, QPalette::Mid, brush5);
        palette.setBrush(QPalette::Disabled, QPalette::Text, brush4);
        palette.setBrush(QPalette::Disabled, QPalette::BrightText, brush6);
        palette.setBrush(QPalette::Disabled, QPalette::ButtonText, brush4);
        palette.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Shadow, brush);
        palette.setBrush(QPalette::Disabled, QPalette::AlternateBase, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::ToolTipBase, brush8);
        palette.setBrush(QPalette::Disabled, QPalette::ToolTipText, brush);
        lcdNumber_Time->setPalette(palette);
        lcdNumber_Time->setFrameShape(QFrame::NoFrame);
        lcdNumber_Time->setDigitCount(4);

        gridLayout_2->addWidget(lcdNumber_Time, 3, 0, 1, 1);

        label_Time = new QLabel(CRQDataView);
        label_Time->setObjectName(QString::fromUtf8("label_Time"));
        QFont font;
        font.setFamily(QString::fromUtf8("Courier"));
        font.setPointSize(14);
        font.setBold(true);
        font.setWeight(75);
        label_Time->setFont(font);
        label_Time->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_Time, 1, 0, 1, 1);

        label_Lab = new QLabel(CRQDataView);
        label_Lab->setObjectName(QString::fromUtf8("label_Lab"));
        QFont font1;
        font1.setFamily(QString::fromUtf8("Courier"));
        font1.setPointSize(20);
        font1.setBold(true);
        font1.setWeight(75);
        label_Lab->setFont(font1);
        label_Lab->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_Lab, 0, 0, 1, 7);

        horizontalSpacer_2 = new QSpacerItem(80, 1, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_2, 1, 2, 1, 1);

        label_2 = new QLabel(CRQDataView);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        QSizePolicy sizePolicy1(QSizePolicy::MinimumExpanding, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(label_2->sizePolicy().hasHeightForWidth());
        label_2->setSizePolicy(sizePolicy1);
        label_2->setMinimumSize(QSize(100, 0));
        QFont font2;
        font2.setFamily(QString::fromUtf8("Courier"));
        font2.setPointSize(10);
        font2.setBold(true);
        font2.setWeight(75);
        label_2->setFont(font2);

        gridLayout_2->addWidget(label_2, 1, 3, 1, 1);

        label_5 = new QLabel(CRQDataView);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        QSizePolicy sizePolicy2(QSizePolicy::Fixed, QSizePolicy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(label_5->sizePolicy().hasHeightForWidth());
        label_5->setSizePolicy(sizePolicy2);
        label_5->setMinimumSize(QSize(70, 0));
        label_5->setMaximumSize(QSize(70, 16777215));
        label_5->setFont(font2);
        label_5->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_5, 1, 4, 1, 1);

        label_3 = new QLabel(CRQDataView);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        sizePolicy2.setHeightForWidth(label_3->sizePolicy().hasHeightForWidth());
        label_3->setSizePolicy(sizePolicy2);
        label_3->setMinimumSize(QSize(110, 0));
        label_3->setMaximumSize(QSize(110, 16777215));
        label_3->setFont(font2);

        gridLayout_2->addWidget(label_3, 1, 5, 1, 1);

        label_4 = new QLabel(CRQDataView);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        sizePolicy2.setHeightForWidth(label_4->sizePolicy().hasHeightForWidth());
        label_4->setSizePolicy(sizePolicy2);
        label_4->setMinimumSize(QSize(80, 0));
        label_4->setMaximumSize(QSize(80, 16777215));
        label_4->setFont(font2);
        label_4->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_4, 1, 6, 1, 1);


        retranslateUi(CRQDataView);

        QMetaObject::connectSlotsByName(CRQDataView);
    } // setupUi

    void retranslateUi(QWidget *CRQDataView)
    {
        CRQDataView->setWindowTitle(QCoreApplication::translate("CRQDataView", "Form", nullptr));
#if QT_CONFIG(tooltip)
        lcdNumber_Time->setToolTip(QCoreApplication::translate("CRQDataView", "Time remaining", nullptr));
#endif // QT_CONFIG(tooltip)
        label_Time->setText(QCoreApplication::translate("CRQDataView", "TIME REMAINING", nullptr));
        label_Lab->setText(QCoreApplication::translate("CRQDataView", "LABNAME", nullptr));
        label_2->setText(QCoreApplication::translate("CRQDataView", "Name", nullptr));
        label_5->setText(QCoreApplication::translate("CRQDataView", "Time", nullptr));
        label_3->setText(QCoreApplication::translate("CRQDataView", "Collisions", nullptr));
        label_4->setText(QCoreApplication::translate("CRQDataView", "Score", nullptr));
    } // retranslateUi

};

namespace Ui {
    class CRQDataView: public Ui_CRQDataView {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CRQDATAVIEW_H
