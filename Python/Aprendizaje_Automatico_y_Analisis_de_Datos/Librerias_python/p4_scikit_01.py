'''
https://scikit-learn.org/stable/
https://www.datacamp.com/es/tutorial/machine-learning-python
https://www.digitalocean.com/community/tutorials/python-scikit-learn-tutorial
https://www.geeksforgeeks.org/machine-learning/scikit-learn-tutorial/
https://scikit-learn.org/1.4/tutorial/index.html
https://www.tutorialspoint.com/scikit_learn/index.htm

'''
def ejem01():
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score, precision_score, recall_score

    # Cargar el dataset iris
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Dividir en conjunto de entrenamiento y prueba 80/20
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear y entrenar el clasificador de árbol de decisión
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Realizar predicciones
    y_pred = clf.predict(X_test)

    # Calcular métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')

    print(f'Accuracy: {accuracy:.2f}')
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')


#Evaluacion con crossvalidation    
def ejem02():
    from sklearn.datasets import load_iris
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import cross_val_score
    from sklearn.metrics import make_scorer, precision_score, recall_score

    # Cargar el dataset iris
    iris = load_iris()
    X, y = iris.data, iris.target

    # Crear el clasificador
    clf = DecisionTreeClassifier(random_state=42)

    # Definir los scorers para precisión y recall promediados (macro para multiclase)
    precision = make_scorer(precision_score, average='macro')
    recall = make_scorer(recall_score, average='macro')

    # Calcular accuracy, precision y recall usando 10-fold cross validation
    accuracy_scores = cross_val_score(clf, X, y, cv=10, scoring='accuracy')
    precision_scores = cross_val_score(clf, X, y, cv=10, scoring=precision)
    recall_scores = cross_val_score(clf, X, y, cv=10, scoring=recall)

    # Mostrar resultados promedio
    print(f'Accuracy promedio: {accuracy_scores.mean():.2f}')
    print(f'Precision promedio: {precision_scores.mean():.2f}')
    print(f'Recall promedio: {recall_scores.mean():.2f}')
   
#Evaluacion con crossvalidation calculada por el programa
def ejem03():
    from sklearn.datasets import load_iris
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, ConfusionMatrixDisplay
    import numpy as np
    import matplotlib.pyplot as plt

    # Cargar el dataset iris
    iris = load_iris()
    X, y = iris.data, iris.target

    # Inicializar el clasificador y la validación cruzada
    clf = DecisionTreeClassifier(random_state=42)
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

    # Listas para almacenar resultados
    accuracies = []
    precisions = []
    recalls = []
    conf_matrix_total = np.zeros((len(np.unique(y)), len(np.unique(y))), dtype=int)

    # Cross-validation manual para poder acumular la matriz de confusión
    for train_index, test_index in skf.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracies.append(accuracy_score(y_test, y_pred))
        precisions.append(precision_score(y_test, y_pred, average='macro'))
        recalls.append(recall_score(y_test, y_pred, average='macro'))
        conf_matrix_total += confusion_matrix(y_test, y_pred, labels=np.unique(y))

    # Mostrar métricas promedio
    print(f'Accuracy promedio: {np.mean(accuracies):.2f}')
    print(f'Precision promedio: {np.mean(precisions):.2f}')
    print(f'Recall promedio: {np.mean(recalls):.2f}')

    # Mostrar la matriz de confusión acumulada
    print("\nMatriz de confusión acumulada (10 folds):")
    print(conf_matrix_total)

    # Visualizar la matriz de confusión
    disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_total, display_labels=iris.target_names)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Matriz de confusión acumulada (10 folds)")
    plt.show()
    
def ejer():
    from sklearn.datasets import load_iris
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    
    from sklearn.model_selection import cross_val_score
    from sklearn.metrics import make_scorer, precision_score, recall_score
    from sklearn import svm

    # Cargar el dataset iris
    iris = load_iris()
    X, y = iris.data, iris.target

    print("PART")
    # Crear el clasificador
    clf = DecisionTreeClassifier(random_state=42)

    # Definir los scorers para precisión y recall promediados (macro para multiclase)
    precision = make_scorer(precision_score, average='macro')
    recall = make_scorer(recall_score, average='macro')

    # Calcular accuracy, precision y recall usando 10-fold cross validation
    accuracy_scores = cross_val_score(clf, X, y, cv=10, scoring='accuracy')
    precision_scores = cross_val_score(clf, X, y, cv=10, scoring=precision)
    recall_scores = cross_val_score(clf, X, y, cv=10, scoring=recall)

    # Mostrar resultados promedio
    print(f'Accuracy promedio: {accuracy_scores.mean():.2f}')
    print(f'Precision promedio: {precision_scores.mean():.2f}')
    print(f'Recall promedio: {recall_scores.mean():.2f}')
    
    #COMPLETAR CON DOS ALGORITMOS MAS
    



    
print("Empezamos")
#ejemplo1()
#ejem01()
print("---------")
#ejem02()
print("---------")
#ejem03()
print("---------")
ejer()
print("---------")

print("Fin")

'''
Aquí tienes **10 ejercicios prácticos** para practicar con **scikit-learn**. Todos usan conjuntos de datos incluidos en la biblioteca (como Iris, Digits o Diabetes), para que puedas empezar rápidamente sin descargar nada extra.

Importa lo necesario al inicio:

"""python
from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
"""

### 1. Clasificación básica con Iris
Carga el dataset Iris. Divide en train/test (80/20). Entrena una regresión logística y calcula la precisión.

### 2. Comparación de clasificadores en Digits
Carga el dataset Digits (imágenes de números). Prueba KNN, SVM y Random Forest. Compara sus precisiones con train_test_split y accuracy_score.

### 3. Validación cruzada en Diabetes
Carga el dataset Diabetes (regresión). Usa LinearRegression y calcula el MSE con cross_val_score (5 folds).

### 4. Árbol de decisión en Iris
Entrena un DecisionTreeClassifier en Iris. Visualiza el árbol (usa plot_tree si tienes Graphviz) y evalúa la precisión.

### 5. Ajuste de hiperparámetros con GridSearchCV
Usa SVC en el dataset Iris. Busca los mejores parámetros (C y kernel) con GridSearchCV y muestra el mejor score.

### 6. Clustering con KMeans
Carga Iris (solo características, sin etiquetas). Aplica KMeans con 3 clusters. Compara los clusters predichos con las etiquetas reales.

### 7. Reducción de dimensionalidad con PCA
Aplica PCA al dataset Digits para reducir a 2 componentes. Visualiza los datos en un scatter plot coloreado por clase.

### 8. Random Forest y importancia de características
Entrena un RandomForestClassifier en Iris o Breast Cancer (datasets.load_breast_cancer()). Muestra la importancia de las características con feature_importances_.

### 9. Pipeline completo
Crea un Pipeline con StandardScaler y LogisticRegression. Aplícalo al dataset Wine (datasets.load_wine()) y evalúa con cross_val_score.

### 10. Regresión con ensemble
Usa el dataset Boston (o California Housing en versiones nuevas: fetch_california_housing). Compara LinearRegression con RandomForestRegressor en términos de MSE.


'''