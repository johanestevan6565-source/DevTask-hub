class Tarea (): 
    Indicador_Id = 1

    def __init__ (self, Titulo, Descripcion, Prioridad, Completada):
        self.Id = Tarea.Indicador_Id
        Tarea.Indicador_Id +=1
        self.Titulo = Titulo
        self.Descripcion = Descripcion
        self.Prioridad = Prioridad
        self.__Completada = Completada



    def prioridad_tarea (self):
        if self.Prioridad == 0:
            return ("baja")
        elif self.Prioridad == 1:
            return ("media")
        elif self.Prioridad == 2:
            return("Alta")
        
    def __str__(self):
        return (
            f"ID: {self.Id}\n"
            f"Título: {self.Titulo}\n"
            f"Descripción: {self.Descripcion}\n"
            f"Prioridad: {self.prioridad_tarea()}\n"
            f"Completada: {self.__Completada}"
    )

    def esta_completada(self):
        return self.__Completada

    def marcar_completada(self, estado=True):
        self.__Completada = estado


class Proyecto():
    def __init__(self):
        self.Lista_tareas = []

    def agregar_tarea (self, titulo, descripcion, prioridad):
        titulo = input("Agregue el nombre de la tarea: ")
        descripcion = input("Ingrese la descripción: ")
        prioridad = int(input("Prioridad (0 baja, 1 media, 2 alta): "))

        nueva_tarea = Tarea(
            titulo,
            descripcion,
            prioridad,
            False
        )

        self.Lista_tareas.append(nueva_tarea)
        return nueva_tarea

    def obtener_progreso(self):
        total_tareas = len(self.Lista_tareas)

        if total_tareas == 0:
            return 0.0
        
        tareas_completadas = 0

        for tarea in self.Lista_tareas:
            if tarea.esta_completada():
                tareas_completadas += 1

        progreso = (tareas_completadas / total_tareas) * 100

        return progreso