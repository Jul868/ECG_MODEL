import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
from sklearn.externals import joblib  # Para cargar el modelo

# Cargar el modelo entrenado
modelo = joblib.load('modelo_entrenado.pkl')

# Supongamos que 'X_test' son tus datos de prueba y 'y_test' son las etiquetas verdaderas
# Deben ser cargados o definidos en alguna parte del código
X_test = np.load('X_test.npy')
y_test = np.load('y_test.npy')

# Realizar predicciones
y_pred = modelo.predict(X_test)
y_probs = modelo.predict_proba(X_test)[:, 1]  # Probabilidades para la clase positiva

# Evaluación del modelo
print("Informe de clasificación:")
print(classification_report(y_test, y_pred))

# Matriz de confusión
conf_mat = confusion_matrix(y_test, y_pred)
print("Matriz de Confusión:")
print(conf_mat)

# Calcular ROC AUC
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
roc_auc = auc(fpr, tpr)

# Gráfica de la curva ROC
plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange', lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()
