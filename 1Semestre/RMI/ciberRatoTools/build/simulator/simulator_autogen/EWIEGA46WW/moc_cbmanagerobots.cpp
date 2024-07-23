/****************************************************************************
** Meta object code from reading C++ file 'cbmanagerobots.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.15.3)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../../../../simulator/cbmanagerobots.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'cbmanagerobots.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.15.3. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_cbManageRobots_t {
    QByteArrayData data[19];
    char stringdata0[382];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_cbManageRobots_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_cbManageRobots_t qt_meta_stringdata_cbManageRobots = {
    {
QT_MOC_LITERAL(0, 0, 14), // "cbManageRobots"
QT_MOC_LITERAL(1, 15, 6), // "closed"
QT_MOC_LITERAL(2, 22, 0), // ""
QT_MOC_LITERAL(3, 23, 15), // "resetRobWidgets"
QT_MOC_LITERAL(4, 39, 18), // "refreshPosComboBox"
QT_MOC_LITERAL(5, 58, 12), // "addRobWidget"
QT_MOC_LITERAL(6, 71, 2), // "id"
QT_MOC_LITERAL(7, 74, 15), // "removeRobWidget"
QT_MOC_LITERAL(8, 90, 19), // "currentAgentChanged"
QT_MOC_LITERAL(9, 110, 11), // "QModelIndex"
QT_MOC_LITERAL(10, 122, 17), // "tryEnableAddRobot"
QT_MOC_LITERAL(11, 140, 20), // "registrationsAllowed"
QT_MOC_LITERAL(12, 161, 31), // "on_pushButton_LoadAgent_clicked"
QT_MOC_LITERAL(13, 193, 33), // "on_pushButton_RemoveAgent_cli..."
QT_MOC_LITERAL(14, 227, 40), // "on_comboBox_Position_currentI..."
QT_MOC_LITERAL(15, 268, 5), // "index"
QT_MOC_LITERAL(16, 274, 30), // "on_pushButton_AddRobot_clicked"
QT_MOC_LITERAL(17, 305, 42), // "on_tableWidget_Robots_itemSel..."
QT_MOC_LITERAL(18, 348, 33) // "on_pushButton_DeleteRobot_cli..."

    },
    "cbManageRobots\0closed\0\0resetRobWidgets\0"
    "refreshPosComboBox\0addRobWidget\0id\0"
    "removeRobWidget\0currentAgentChanged\0"
    "QModelIndex\0tryEnableAddRobot\0"
    "registrationsAllowed\0"
    "on_pushButton_LoadAgent_clicked\0"
    "on_pushButton_RemoveAgent_clicked\0"
    "on_comboBox_Position_currentIndexChanged\0"
    "index\0on_pushButton_AddRobot_clicked\0"
    "on_tableWidget_Robots_itemSelectionChanged\0"
    "on_pushButton_DeleteRobot_clicked"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_cbManageRobots[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      13,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,   79,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       3,    1,   80,    2, 0x08 /* Private */,
       4,    0,   83,    2, 0x08 /* Private */,
       5,    1,   84,    2, 0x08 /* Private */,
       7,    1,   87,    2, 0x08 /* Private */,
       8,    2,   90,    2, 0x08 /* Private */,
      10,    1,   95,    2, 0x08 /* Private */,
      12,    0,   98,    2, 0x08 /* Private */,
      13,    0,   99,    2, 0x08 /* Private */,
      14,    1,  100,    2, 0x08 /* Private */,
      16,    0,  103,    2, 0x08 /* Private */,
      17,    0,  104,    2, 0x08 /* Private */,
      18,    0,  105,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,    6,
    QMetaType::Void, QMetaType::Int,    6,
    QMetaType::Void, 0x80000000 | 9, 0x80000000 | 9,    2,    2,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,   15,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void cbManageRobots::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<cbManageRobots *>(_o);
        (void)_t;
        switch (_id) {
        case 0: _t->closed(); break;
        case 1: _t->resetRobWidgets((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->refreshPosComboBox(); break;
        case 3: _t->addRobWidget((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->removeRobWidget((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: _t->currentAgentChanged((*reinterpret_cast< QModelIndex(*)>(_a[1])),(*reinterpret_cast< QModelIndex(*)>(_a[2]))); break;
        case 6: _t->tryEnableAddRobot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 7: _t->on_pushButton_LoadAgent_clicked(); break;
        case 8: _t->on_pushButton_RemoveAgent_clicked(); break;
        case 9: _t->on_comboBox_Position_currentIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 10: _t->on_pushButton_AddRobot_clicked(); break;
        case 11: _t->on_tableWidget_Robots_itemSelectionChanged(); break;
        case 12: _t->on_pushButton_DeleteRobot_clicked(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (cbManageRobots::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&cbManageRobots::closed)) {
                *result = 0;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject cbManageRobots::staticMetaObject = { {
    QMetaObject::SuperData::link<QWidget::staticMetaObject>(),
    qt_meta_stringdata_cbManageRobots.data,
    qt_meta_data_cbManageRobots,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *cbManageRobots::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *cbManageRobots::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_cbManageRobots.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int cbManageRobots::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 13)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 13;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 13)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 13;
    }
    return _id;
}

// SIGNAL 0
void cbManageRobots::closed()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
