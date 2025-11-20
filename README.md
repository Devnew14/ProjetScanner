# 🔍 Mini Scanner de Ports en Python

Ce projet est un petit scanner de ports éducatif écrit en Python.  
Il permet de tester si certains ports d’une machine locale ou du réseau sont ouverts.

> ⚠️ **Usage légal uniquement**  
> Ce scanner ne doit être utilisé que sur vos propres machines ou sur celles pour lesquelles vous avez une autorisation explicite.

---

## 🧠 Fonctionnement

Le script tente d'établir une connexion TCP sur une liste de ports.  
Si la connexion réussit → le port est considéré comme **ouvert**.  
Si la connexion échoue → le port est **fermé**.

Il utilise le module standard Python :

```python
import socket
