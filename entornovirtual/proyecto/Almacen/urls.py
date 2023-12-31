from django.urls import path
from .import views

urlpatterns=[

    #login
    #path("",views.home),
    #path("RegistroUsuario",views.registrar_usuario),
    path('',views.home,name="inicio"),
    path('salir/',views.salir,name='salir'),

    path('marca',views.marca,name='marca'),
    path('marca/registrarmarca',views.registrarmarca),
    path('marca/edicionmarca/<codigo>',views.edicionmarca),
    path('marca/updatemarca/<codigo>',views.updatemarca),
    path('marca/eliminarmarca/<codigo>',views.eliminarmarca),

    path('modelo',views.modelo,name='modelo'),
    path('modelo/registrarmodelo',views.registrarmodelo),
    path('modelo/edicionmodelo/<codigo>',views.edicionmodelo),
    path('modelo/updatemodelo/<codigo>',views.updatemodelo),
    path('modelo/eliminarmodelo/<codigo>',views.eliminarmodelo),

    path('categoria',views.categoria,name='categoria'),
    path('categoria/registrarcategoria',views.registrarcategoria),
    path('categoria/edicioncategoria/<codigo>',views.edicioncategoria),
    path('categoria/updatecategoria/<codigo>',views.updatecategoria),
    path('categoria/eliminarcategoria/<codigo>',views.eliminarcategoria),

    path('articulo',views.articulo,name='articulo'),
    path('articulo/registrararticulo',views.registrararticulo),
    path('articulo/edicionarticulo/<codigo>',views.edicionarticulo),
    path('articulo/updatearticulo/<codigo>',views.updatearticulo),
    path('articulo/eliminararticulo/<codigo>',views.eliminararticulo),

    path('ingreso',views.ingreso,name='ingreso'),
    path('ingreso/registraringreso',views.registraringreso),
    path('ingreso/edicioningreso/<codigo>',views.edicioningreso),
    path('ingreso/updateingreso/<codigo>',views.updateingreso),
    path('ingreso/eliminaringreso/<codigo>',views.eliminaringreso),

    path('pedido',views.pedido,name='pedido'),
    path('pedido/registrarpedido',views.registrarpedido),
    path('pedido/edicionpedido/<codigo>',views.edicionpedido),
    path('pedido/updatepedido/<codigo>',views.updatepedido),
    path('pedido/eliminarpedido/<codigo>',views.eliminarpedido),

    path('salida',views.salida,name='salida'),
    path('salida/registrarsalida',views.registrarsalida),
    path('salida/edicionsalida/<codigo>',views.edicionsalida),
    path('salida/updatesalida/<codigo>',views.updatesalida),
    path('salida/eliminarsalida/<codigo>',views.eliminarsalida),

    path('reporteingreso',views.reporteingreso,name='reporteingreso'),
    path('reportepedido',views.reportepedido,name='reportepedido'),
    path("reporte/<codigo>",views.find_reporte,name="find_reporte"),
    path('reportesalida',views.reportesalida,name='reportesalida'),
    

    path('generar-reporte/', views.generar_reporte_ingreso.as_view(), name='generar_reporte'),
    path('generar-reporte-completo/', views.generar_reporte_ingreso_total.as_view(), name='generar_reporte_completo'),
    
    path('generar-reporte-salida/', views.generar_reporte_salida.as_view(), name='generar_reporte_salida'),
    path('generar-reporte-completo-salida/', views.generar_reporte_salida_total.as_view(), name='generar_reporte_completo_salida'),
    
    path('generar-reporte-pedido-pedido/', views.generar_reporte_pedido.as_view(), name='generar_reporte_pedido'),
    path('generar-reporte-completo-pedido/', views.generar_reporte_pedido_total.as_view(), name='generar_reporte_completo_pedido'),
    #path("Inicio",views.index)
    ]