/****************************************************************************
** Meta object code from reading C++ file 'crqlabview.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.15.3)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../../../../Viewer/crqlabview.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'crqlabview.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.15.3. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_CRQLabView_t {
    QByteArrayData data[12];
    char stringdata0[272];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_CRQLabView_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_CRQLabView_t qt_meta_stringdata_CRQLabView = {
    {
QT_MOC_LITERAL(0, 0, 10), // "CRQLabView"
QT_MOC_LITERAL(1, 11, 31), // "on_actionReset_Viewer_triggered"
QT_MOC_LITERAL(2, 43, 0), // ""
QT_MOC_LITERAL(3, 44, 24), // "on_actionConnect_toggled"
QT_MOC_LITERAL(4, 69, 7), // "connect"
QT_MOC_LITERAL(5, 77, 24), // "on_actionAbout_triggered"
QT_MOC_LITERAL(6, 102, 36), // "on_actionLower_walls_color_tr..."
QT_MOC_LITERAL(7, 139, 38), // "on_actionHigher_walls_collor_..."
QT_MOC_LITERAL(8, 178, 29), // "on_actionSound_On_Off_toggled"
QT_MOC_LITERAL(9, 208, 7), // "soundON"
QT_MOC_LITERAL(10, 216, 30), // "on_actionChange_skin_triggered"
QT_MOC_LITERAL(11, 247, 24) // "on_actionStart_triggered"

    },
    "CRQLabView\0on_actionReset_Viewer_triggered\0"
    "\0on_actionConnect_toggled\0connect\0"
    "on_actionAbout_triggered\0"
    "on_actionLower_walls_color_triggered\0"
    "on_actionHigher_walls_collor_triggered\0"
    "on_actionSound_On_Off_toggled\0soundON\0"
    "on_actionChange_skin_triggered\0"
    "on_actionStart_triggered"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_CRQLabView[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    0,   54,    2, 0x08 /* Private */,
       3,    1,   55,    2, 0x08 /* Private */,
       5,    0,   58,    2, 0x08 /* Private */,
       6,    0,   59,    2, 0x08 /* Private */,
       7,    0,   60,    2, 0x08 /* Private */,
       8,    1,   61,    2, 0x08 /* Private */,
      10,    0,   64,    2, 0x08 /* Private */,
      11,    0,   65,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::Bool,    4,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Bool,    9,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void CRQLabView::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<CRQLabView *>(_o);
        (void)_t;
        switch (_id) {
        case 0: _t->on_actionReset_Viewer_triggered(); break;
        case 1: _t->on_actionConnect_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 2: _t->on_actionAbout_triggered(); break;
        case 3: _t->on_actionLower_walls_color_triggered(); break;
        case 4: _t->on_actionHigher_walls_collor_triggered(); break;
        case 5: _t->on_actionSound_On_Off_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 6: _t->on_actionChange_skin_triggered(); break;
        case 7: _t->on_actionStart_triggered(); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject CRQLabView::staticMetaObject = { {
    QMetaObject::SuperData::link<QMainWindow::staticMetaObject>(),
    qt_meta_stringdata_CRQLabView.data,
    qt_meta_data_CRQLabView,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *CRQLabView::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *CRQLabView::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_CRQLabView.stringdata0))
        return static_cast<void*>(this);
    return QMainWindow::qt_metacast(_clname);
}

int CRQLabView::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 8)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 8;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 8)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 8;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
