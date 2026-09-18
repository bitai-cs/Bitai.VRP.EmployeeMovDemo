# Bitai.VRP.EmployeeMovDemo

Demo de Vehicle Routing Problem para escenarios de transporte de empleados.

## Desarrollo con UV

Requiere [UV](https://docs.astral.sh/uv/). Desde la raíz del proyecto:

```powershell
uv sync
uv run scr/main.py --env-file base_to_home.env
```

También puedes ejecutar el escenario de regreso:

```powershell
uv run scr/main.py --env-file home_to_base.env
```

UV administra el entorno `.venv` y las dependencias declaradas en `pyproject.toml`.
El archivo `requirements.txt` se conserva para compatibilidad con instalaciones basadas en pip.
