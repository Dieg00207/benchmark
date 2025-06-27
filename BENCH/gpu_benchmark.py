import pyopencl as cl
import numpy as np
import time

def gpu_performance():
    context = cl.create_some_context() #crear contexto

    queue = cl.create_queue(context) #crear colas de comando en el contexto
    vec_size = 10000000 #10 millones

    #crear dos vecntores grande con nuevos aleatorios
    a = np.random.rand(vec_size).astype(np.float32) 
    b = np.random.rand(vec_size).astype(np.float32)

    result = np.empty_like(a)

    #crear buferes para los vectores en el dispositivo
    mf = cl.mem_flags

    a_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
    b_buf = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)
    res_buf = cl.Buffer(context, mf.WRITE_ONLY, result.nbytes)
    kernel_code = """
    __kernel void vector_add(__global const float * a, __global const float *b, __global const float *res)
    {
        int gid = get_global_id(0);
        res[gid] = a[gid] + b[gid];
    }
    """
    program = cl.program(context, kernel_code).build()
    kernel = cl.kernel(program, 'vector_add')

# establcer los argunmentos del kernel
    kernel.set_arg(0, a_buf)
    kernel.set_arg(1, b_buf)
    kernel.set_arg(2, res_buf)

# ejecutar el kernel
    start_time = time.time()
    cl.enqueue_nd_range_kernel(queue, kernel, (vec_size), None)
    queue.finish()
    end_time = time.time()
    # tiempo de ejecucion
    run_time = end_time - start_time
    print(f"Tiempo de ejecucion del benchmark de la GPU: {run_time:.6f} Seconds")


    #leer el resultado
    cl.enqueue_copy(queue, result, res_buf)
    queue.finish()

    #comprobar algunos resultados
    for i in range(5):
        print(f"result[{i}] = {result[i]}")


