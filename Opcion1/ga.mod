/*********************************************
 * OPL 12.10.0.0 Model
 * Author: cardo
 * Creation Date: Nov 1, 2020 at 6:42:15 PM
 *********************************************/
range manzanas = 1..4605;
range locales = 1..63;

int poblacion[manzanas] = ...;
int centros = 6554; // 412840 / 63
float cost_distances[manzanas][locales] = ...;
 
dvar float+ x[manzanas][locales];

dexpr float cost = sum(i in manzanas, j in locales) cost_distances[i][j] * x[i][j];

minimize cost;

subject to {
 cons1:
 	sum(i in manzanas) poblacion[i] <= centros*63;
 cons2:
 	forall(j in locales)
 		sum(i in manzanas) x[i][j] <= centros;
 cons3:
 	forall(i in manzanas, j in locales)
 	  x[i][j] >= 0;
 cons4:
 	forall(i in manzanas)
 	  sum(j in locales) x[i][j] == poblacion[i];
}
