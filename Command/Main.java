public class Main {
    public static void main(String[] args) {
        Portao portao = new Portao();
        Command abrirCommand = new AbrirCommand(portao);
        Command fecharCommand = new FecharCommand(portao);

        Controle controle = new Controle(abrirCommand, fecharCommand);

        controle.abrirPortao();

        controle.fecharPortao();

        controle.desfazer();
    }
}