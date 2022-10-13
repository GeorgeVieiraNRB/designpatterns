public class FecharCommand implements Command {
    private Portao portao;

    public FecharCommand(Portao portao) {
        this.portao = portao;
    }

    public void execute() {
        portao.fechar();
    }

    public void undo() {
        portao.abrir();
    }
}