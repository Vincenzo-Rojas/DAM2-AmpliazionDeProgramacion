
#Aquí tienes **10 ejercicios prácticos** para practicar con **scikit-learn**. Todos usan conjuntos de datos incluidos en la biblioteca (como Iris, Digits o Diabetes), para que puedas empezar rápidamente sin descargar nada extra.

#Importa lo necesario al inicio:
from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np


### 1. Clasificación básica con Iris
#Carga el dataset Iris. Divide en train/test (80/20). Entrena una regresión logística y calcula la precisión.
iris = datasets.load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf1 = LogisticRegression(max_iter=200)
clf1.fit(X_train, y_train)
y_pred1 = clf1.predict(X_test)
print("Ejercicio 1 - Accuracy:", accuracy_score(y_test, y_pred1))

### 2. Comparación de clasificadores en Digits
#Carga el dataset Digits (imágenes de números). Prueba KNN, SVM y Random Forest. Compara sus precisiones con train_test_split y accuracy_score.
digits = datasets.load_digits()
X2, y2 = digits.data, digits.target
X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=42)

models2 = {
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "RandomForest": RandomForestClassifier()
}

for name, model in models2.items():
    model.fit(X_train2, y_train2)
    y_pred2 = model.predict(X_test2)
    print(f"Ejercicio 2 - {name} Accuracy:", accuracy_score(y_test2, y_pred2))

### 3. Validación cruzada en Diabetes
#Carga el dataset Diabetes (regresión). Usa LinearRegression y calcula el MSE con cross_val_score (5 folds).
diabetes = datasets.load_diabetes()
X3, y3 = diabetes.data, diabetes.target
linreg3 = LinearRegression()
mse_scores = -cross_val_score(linreg3, X3, y3, cv=5, scoring='neg_mean_squared_error')
print("Ejercicio 3 - MSE promedio:", mse_scores.mean())

### 4. Árbol de decisión en Iris
#Entrena un DecisionTreeClassifier en Iris. Visualiza el árbol (usa plot_tree si tienes Graphviz) y evalúa la precisión.
clf4 = DecisionTreeClassifier(random_state=42)
clf4.fit(X, y)
plt.figure(figsize=(12,6))
plot_tree(clf4, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Ejercicio 4 - Árbol de decisión")
plt.show()
y_pred4 = clf4.predict(X_test)
print("Ejercicio 4 - Accuracy:", accuracy_score(y_test, y_pred4))

### 5. Ajuste de hiperparámetros con GridSearchCV
#Usa SVC en el dataset Iris. Busca los mejores parámetros (C y kernel) con GridSearchCV y muestra el mejor score.
svc5 = SVC()
param_grid5 = {"C":[0.1,1,10], "kernel":["linear","rbf"]}
grid5 = GridSearchCV(svc5, param_grid5, cv=5)
grid5.fit(X, y)
print("Ejercicio 5 - Mejor score GridSearchCV:", grid5.best_score_)
print("Ejercicio 5 - Mejores parámetros:", grid5.best_params_)

### 6. Clustering con KMeans
#Carga Iris (solo características, sin etiquetas). Aplica KMeans con 3 clusters. Compara los clusters predichos con las etiquetas reales.
kmeans6 = KMeans(n_clusters=3, random_state=42)
clusters6 = kmeans6.fit_predict(X)
plt.figure()
plt.scatter(X[:,0], X[:,1], c=clusters6, cmap='viridis')
plt.title("Ejercicio 6 - KMeans clusters")
plt.show()

### 7. Reducción de dimensionalidad con PCA
#Aplica PCA al dataset Digits para reducir a 2 componentes. Visualiza los datos en un scatter plot coloreado por clase.
digits7 = datasets.load_digits()
X7, y7 = digits7.data, digits7.target
pca7 = PCA(n_components=2)
X_pca7 = pca7.fit_transform(X7)
plt.figure()
plt.scatter(X_pca7[:,0], X_pca7[:,1], c=y7, cmap='tab10', s=15)
plt.colorbar()
plt.title("Ejercicio 7 - PCA Digits")
plt.show()

### 8. Random Forest y importancia de características
#Entrena un RandomForestClassifier en Iris o Breast Cancer (datasets.load_breast_cancer()). Muestra la importancia de las características con feature_importances_.
breast8 = datasets.load_breast_cancer()
X8, y8 = breast8.data, breast8.target
rf8 = RandomForestClassifier(random_state=42)
rf8.fit(X8, y8)
importances8 = rf8.feature_importances_
plt.figure()
plt.bar(range(len(importances8)), importances8)
plt.title("Ejercicio 8 - Importancia de características")
plt.show()

### 9. Pipeline completo
#Crea un Pipeline con StandardScaler y LogisticRegression. Aplícalo al dataset Wine (datasets.load_wine()) y evalúa con cross_val_score.
wine9 = datasets.load_wine()
X9, y9 = wine9.data, wine9.target
pipeline9 = Pipeline([("scaler", StandardScaler()), ("logreg", LogisticRegression(max_iter=500))])
scores9 = cross_val_score(pipeline9, X9, y9, cv=5)
print("Ejercicio 9 - Accuracy promedio Pipeline:", scores9.mean())

### 10. Regresión con ensemble
#Usa el dataset Boston (o California Housing en versiones nuevas: fetch_california_housing). Compara LinearRegression con RandomForestRegressor en términos de MSE.
california10 = datasets.fetch_california_housing()
X10, y10 = california10.data, california10.target
X_train10, X_test10, y_train10, y_test10 = train_test_split(X10, y10, test_size=0.2, random_state=42)
models10 = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestClassifier()  # Para regresión sería RandomForestRegressor si quieres valores continuos
}
models10["RandomForest"] = RandomForestRegressor(random_state=42)

for name, model in models10.items():
    model.fit(X_train10, y_train10)
    y_pred10 = model.predict(X_test10)
    mse10 = mean_squared_error(y_test10, y_pred10)
    print(f"Ejercicio 10 - {name} MSE:", mse10)