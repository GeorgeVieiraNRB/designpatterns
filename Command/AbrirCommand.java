public class AbrirCommand implements Command {
    private Portao portao;

    public AbrirCommand(Portao portao) {
        this.portao = portao;
    }

    public void execute() {
        portao.abrir();
    }

    public void undo() {
        portao.fechar();
    }
}