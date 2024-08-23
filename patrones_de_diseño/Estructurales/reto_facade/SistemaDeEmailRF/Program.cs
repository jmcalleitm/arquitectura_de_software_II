class Program
{
    static void Main(string[] args)
    {
        // El cliente ahora solo interactúa con el Facade para enviar correos
        EmailFacade emailFacade = new EmailFacade();
        emailFacade.SendEmail("usuario", "password", "from@example.com", "to@example.com", "Asunto", "Contenido del correo", "ruta/al/archivo");
    }
}
