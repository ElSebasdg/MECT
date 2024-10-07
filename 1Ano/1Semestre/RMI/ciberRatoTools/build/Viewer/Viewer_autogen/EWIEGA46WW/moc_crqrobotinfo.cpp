/****************************************************************************
** Meta object code from reading C++ file 'crqrobotinfo.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.15.3)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../../../../Viewer/crqrobotinfo.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'crqrobotinfo.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.15.3. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_CRQRobotInfo_t {
    QByteArrayData data[7];
    char stringdata0[53];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_CRQRobotInfo_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_CRQRobotInfo_t qt_meta_stringdata_CRQRobotInfo = {
    {
QT_MOC_LITERAL(0, 0, 12), // "CRQRobotInfo"
QT_MOC_LITERAL(1, 13, 5), // "score"
QT_MOC_LITERAL(2, 19, 0), // ""
QT_MOC_LITERAL(3, 20, 10), // "returnTime"
QT_MOC_LITERAL(4, 31, 10), // "collisions"
QT_MOC_LITERAL(5, 42, 5), // "state"
QT_MOC_LITERAL(6, 48, 4) // "time"

    },
    "CRQRobotInfo\0score\0\0returnTime\0"
    "collisions\0state\0time"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_CRQRobotInfo[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       5,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   39,    2, 0x06 /* Public */,
       3,    1,   42,    2, 0x06 /* Public */,
       4,    1,   45,    2, 0x06 /* Public */,
       5,    1,   48,    2, 0x06 /* Public */,
       6,    1,   51,    2, 0x06 /* Public */,

 // signals: parameters
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::QPixmap,    2,
    QMetaType::Void, QMetaType::Int,    2,

       0        // eod
};

void CRQRobotInfo::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<CRQRobotInfo *>(_o);
        (void)_t;
        switch (_id) {
        case 0: _t->score((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->returnTime((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->collisions((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: _t->state((*reinterpret_cast< const QPixmap(*)>(_a[1]))); break;
        case 4: _t->time((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (CRQRobotInfo::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CRQRobotInfo::score)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (CRQRobotInfo::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CRQRobotInfo::returnTime)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (CRQRobotInfo::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CRQRobotInfo::collisions)) {
                *result = 2;
                return;
            }
        }
        {
            using _t = void (CRQRobotInfo::*)(const QPixmap & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CRQRobotInfo::state)) {
                *result = 3;
                return;
            }
        }
        {
            using _t = void (CRQRobotInfo::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CRQRobotInfo::time)) {
                *result = 4;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject CRQRobotInfo::staticMetaObject = { {
    QMetaObject::SuperData::link<QWidget::staticMetaObject>(),
    qt_meta_stringdata_CRQRobotInfo.data,
    qt_meta_data_CRQRobotInfo,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *CRQRobotInfo::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *CRQRobotInfo::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_CRQRobotInfo.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int CRQRobotInfo::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 5;
    }
    return _id;
}

// SIGNAL 0
void CRQRobotInfo::score(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void CRQRobotInfo::returnTime(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void CRQRobotInfo::collisions(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}

// SIGNAL 3
void CRQRobotInfo::state(const QPixmap & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 3, _a);
}

// SIGNAL 4
void CRQRobotInfo::time(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 4, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
