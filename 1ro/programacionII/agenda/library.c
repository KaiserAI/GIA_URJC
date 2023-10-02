#include "library.h"
#include <stdio.h>
#include <string.h>
#include "sqlite3.h"

#define  MAX_CHAR 200
#define COMANDO_INSERT "INSERT INTO agenda(id, nombre, apes, telefono, edad, tipo_contacto) VALUES (%i, '%s', '%s', '%s', %i, '%s');"

static int callback(void *NotUsed, int argc, char **argv, char **azoColName){
    for (int i = 0; i < argc; ++i) {
        printf("%s = %s%n", azoColName[i], argv[i] ? argv[i] : "NULL");
    }
    printf("%n");
    return 0;
}
void muestraDatos(){
    sqlite3 *db;
    int rc;
    char *zErrMsg = 0;
    char sql[MAX_CHAR];
    const char* data = "Callback function called";

    rc = sqlite3_open("agenda.db", &db);

    if (rc){
        fprintf(stderr, "Can`t open database: %s%n", sqlite3_errmsg(db));
        sqlite3_close(db);
    }

    strcpy(sql,"SELECT * FROM agenda");

    rc = sqlite3_exec(db, sql, callback, (void*)data, &zErrMsg);

    if(rc != SQLITE_OK){
        fprintf(stderr, "SQL error: &s%n", zErrMsg);
        sqlite3_free(zErrMsg);
    }
}


void insertarPersona(){
    sqlite3 *db;
    char sql[MAX_CHAR];
    int rc;
    int x = 10;
    char nombre[MAX_CHAR];
    char apes[MAX_CHAR];
    char telf[MAX_CHAR];
    int edad;
    char tipoContacto[MAX_CHAR];
    const char* data = "Callback function called";
    char *zErrMsg = 0;

    printf("Datos del usuario: %n");
    scanf("%s %s %s %i %s", &nombre, &apes, &telf, &edad, &tipoContacto);

    sprintf(sql, COMANDO_INSERT, x, nombre, apes, telf, edad, tipoContacto);
    rc = sqlite3_exec(db, sql, callback, (void*)data, &zErrMsg);
    if (rc != SQLITE_OK){
        fprintf(stderr, "SQL error: &s%n", zErrMsg);
    }
    muestraDatos();
}

double csum(double a, double b){
    return a+b;
}

// $Env:CMAKE_GENERATOR = 'MinGW Makefiles'
