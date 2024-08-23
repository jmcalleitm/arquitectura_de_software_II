// Clase Facade que simplifica la interacción con el sistema de envío de correos
public class EmailFacade
{
    private EmailAuthentication _auth;
    private EmailHeader _header;
    private EmailContentEncoding _contentEncoder;
    private EmailAttachment _attachment;
    private EmailSender _sender;

    public EmailFacade()
    {
        _auth = new EmailAuthentication();
        _header = new EmailHeader();
        _contentEncoder = new EmailContentEncoding();
        _attachment = new EmailAttachment();
        _sender = new EmailSender();
    }

    public void SendEmail(string user, string password, string from, string to, string subject, string content, string filePath)
    {
        _auth.Authenticate(user, password);
        _header.SetHeaders(from, to, subject);
        _contentEncoder.EncodeContent(content);

        if (!string.IsNullOrEmpty(filePath))
        {
            _attachment.AddAttachment(filePath);
        }

        _sender.Send();
    }
}
