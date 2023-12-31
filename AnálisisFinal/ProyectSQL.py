# -*- coding: utf-8 -*-
"""
Created on Sat May 22 21:35:49 2021

@author: David
"""
#Funcion para determinar el promedio obtenido en el area de ingles por departamentos
def avgIngles():
    return ''' select avg(x.puntaje_ingles)::real as promingles, d.nombre_d as departamento from 
    ((((examen x inner join estudiante e on x.id_estudiante=e.id_estudiante)
    inner join colegio c on c.codigo=e.codigo_colegio)inner join municipio m on m.codigo_m=c.codigo_m_municipio)
    inner join departamento d on d.codigo_d=m.codigo_d_departamento) 
    where x.puntaje_ingles is not null group by d.nombre_d;'''
    
#Promedio de cada asignatura para los hombres(H)
def avgSubjectsM():
    return ''' select e.sexo,avg(x.puntaje_c_naturales)::real as promNaturales,
    avg(x.puntaje_matematicas)::real as promMatematicas,
    avg(x.puntaje_sociales)::real as promSociales,
    avg(x.puntaje_ingles)::real as promIngles,
    avg(x.puntaje_lectura_critica)::real as promLectura 
    from examen x inner join estudiante e on e.id_estudiante=x.id_estudiante 
    group by e.sexo having e.sexo<>'-' and e.sexo='M';'''
    
#Promedio de cada asignatura para las mujeres(F)
def avgSubjectsF():
    return ''' select e.sexo,avg(x.puntaje_c_naturales)::real as promNaturales,
    avg(x.puntaje_matematicas)::real as promMatematicas,
    avg(x.puntaje_sociales)::real as promSociales,
    avg(x.puntaje_ingles)::real as promIngles,
    avg(x.puntaje_lectura_critica)::real as promLectura 
    from examen x inner join estudiante e on e.id_estudiante=x.id_estudiante 
    group by e.sexo having e.sexo<>'-' and e.sexo='F' '''

#Los 7 mejores colegios del departamento seleccionado
def rankingColegios():
    return '''select c.nombre_colegio as colegio ,avg(x.puntaje_global)::real as puntaje from 
    (((departamento d inner join municipio m on d.codigo_d=m.codigo_d_departamento)
    inner join colegio c on c.codigo_m_municipio=m.codigo_m)inner join estudiante e 
    on e.codigo_colegio=c.codigo) inner join examen x on x.id_estudiante=e.id_estudiante
    where d.nombre_d='{0}' group by c.nombre_colegio order by puntaje desc limit 7;'''
    

#Puntaje de cada asignatura por estrato (slider)
def PromPuntajeSlider():
    return ''' select avg(x.puntaje_c_naturales)::real as promNaturales,
    avg(x.puntaje_matematicas)::real as promMatematicas,
    avg(x.puntaje_sociales)::real as promSociales,
    avg(x.puntaje_ingles)::real as promIngles,
    avg(x.puntaje_lectura_critica)::real as promLectura 
    from examen x inner join estudiante e on e.id_estudiante=x.id_estudiante
    where e.estrato='{0}' group by e.estrato having e.estrato<>-1;'''
    

#Promedio del puntaje por cada estrato
def PuntajeByEstrato():
    return """select avg(x.puntaje_global)::real as promedio_puntaje, e.estrato as estrato
              from examen x inner join estudiante e on x.id_estudiante = e.id_estudiante
              where e.estrato<>-1
              group by e.estrato"""
    
#Número de estuidantes por estrato
def CuantosPorEstrato():
    return """select estrato, count(estrato) as many
                from estudiante
                    group by estrato"""

#Colegios de Bogotá ordenados por puntaje                    
def RankingMejoresColegiosBogota():
    return """select c.nombre_colegio as colegio, avg(x.puntaje_global)::real as puntaje
                from ((examen x inner join estudiante e on x.id_estudiante = e.id_estudiante) 
                inner join colegio c on e.codigo_colegio = c.codigo) 
                inner join municipio m on m.codigo_m = c.codigo_m_municipio
                group by colegio  order by puntaje desc"""

#Promedio de puntaje global obtenido en colegios oficiales y no oficiales
def avgPromediosTipoColegio():
    return ''' SELECT c.naturaleza, avg(ex.puntaje_global)::real as puntaje_global
               FROM ((colegio as c INNER JOIN estudiante as est ON c.codigo = est.codigo_colegio)
               INNER JOIN examen as ex ON est.id_estudiante = ex.id_estudiante)  
               GROUP BY c.naturaleza; ''' 
