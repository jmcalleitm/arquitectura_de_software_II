class Program
{
    static void Main(string[] args)
    {
        // El cliente tiene que interactuar con todas las clases directamente
        EmailAuthentication auth = new EmailAuthentication();
        auth.Authenticate("usuario", "password");

        EmailHeader header = new EmailHeader();
        header.SetHeaders("from@example.com", "to@example.com", "Asunto");

        EmailContentEncoding contentEncoder = new EmailContentEncoding();
        contentEncoder.EncodeContent("Contenido del correo");

        EmailAttachment attachment = new EmailAttachment();
        attachment.AddAttachment("ruta/al/archivo");

        EmailSender sender = new EmailSender();
        sender.Send();
    }
}
