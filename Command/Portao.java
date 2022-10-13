public class Portao {
    public final static int ABERTO = 0;
    public final static int FECHADO = 1;

    private int estado = 0;

    public int getEstado() {
        return estado;
    }

    public void setEstado(int estado) {
        this.estado = estado;
    }

    public void abrir() {
        this.estado = ABERTO;
        System.out.println("O portão abriu.");
    }

    public void fechar() {
        this.estado = FECHADO;
        System.out.println("O portão fechou.");
    }
}