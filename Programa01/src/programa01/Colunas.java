/*
    Universidade Tecnológica Federal do Paraná - CM
    Autor: Renan Kodama 
    Disciplina: Engenharia de Software02
    Data: 12/09/2019
 */

package programa01;

import java.util.ArrayList;
import java.util.List;

public class Colunas {
    String cabecalho;
    List<Double> valores = new ArrayList<>();
    float desvio;
    float media;

    public List<Double> getValores() {
        return valores;
    }

    public void setValores(List<Double> valores) {
        this.valores = valores;
    }

    public String getCabecalho() {
        return cabecalho;
    }

    public void setCabecalho(String cabecalho) {
        this.cabecalho = cabecalho;
    }

    public double getDesvio() {
        return desvio;
    }

    public void setDesvio(float desvio) {
        this.desvio = desvio;
    }

    public double getMedia() {
        return media;
    }

    public void setMedia(float media) {
        this.media = media;
    }
}