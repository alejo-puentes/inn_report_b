from django.urls import path
#from pucSup.views import PucSupApiView, PucSupApiViewDetail
from Resumen.views import DocumentoUploadView, DocumentoListCreateView, DocumentoVistaPDF, DocumentoDescarga
  
urlpatterns_Resumen = [
    path('v1/subirDocumento', DocumentoUploadView.as_view()), 
    path('v1/Documento', DocumentoListCreateView.as_view()), 
    path('v1/DocumentoPDF/<int:documento_id>/', DocumentoVistaPDF.as_view()), 
    path('v1/DocumentoDownload/<int:documento_id>/', DocumentoDescarga.as_view()), 
]