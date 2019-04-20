/*
    Universidade Federal do Paraná
    Autor: Renan Kodama 
    Disciplina: Engenharia de Software02
    Data: 12/09/2019
 */

package programa01;

import java.io.FileNotFoundException;
import java.io.FileReader;
import static java.lang.Math.pow;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;

public class Programa01 {

    //lendo a primeira linha (esperado #NAME01, NAME02, NAME03, ...)
    public static void lerCabecalho(String primeiraLinha, List<Colunas> dadosObtidos, AtomicInteger numeroColunas) {
        String[] aux = primeiraLinha.split(", ");

        numeroColunas.set(aux.length);
        
        for (String nomeColuna : aux) {
            Colunas col = new Colunas();
            col.setCabecalho(nomeColuna);
            dadosObtidos.add(col);
        }
    }

    //lendo as demais linhas
    public static boolean lerArquivo(Scanner scanner, List<Colunas> dadosObtidos, AtomicInteger numColunas) {
        String[] aux;

        while (scanner.hasNext()) {
            aux = scanner.nextLine().split(", ");

            if (aux.length != numColunas.get()) {
                return false;
            }

            for (int i = 0; i < aux.length; i++) {
                dadosObtidos.get(i).getValores().add(Double.parseDouble(aux[i]));
            }
        }

        return true;
    }

    public static void calcularMediaDesvio(List<Colunas> dadosObtidos) {

        //calculo da media
        for (int i = 0; i < dadosObtidos.size(); i++) {
            float valorMedia = 0;

            for (Double valor : dadosObtidos.get(i).getValores()) {
                valorMedia += valor;
            }
            valorMedia = valorMedia / dadosObtidos.get(i).getValores().size();
            dadosObtidos.get(i).setMedia(valorMedia);
        }

        //calculo do desvio padrao
        for (int i = 0; i < dadosObtidos.size(); i++) {
            float valorDesvioPadrao = 0;

            for (Double valor : dadosObtidos.get(i).getValores()) {
                valorDesvioPadrao += pow((valor - dadosObtidos.get(i).getMedia()), 2);
            }

            valorDesvioPadrao = (float) pow(valorDesvioPadrao / (dadosObtidos.get(i).getValores().size() - 1), 0.5);
            dadosObtidos.get(i).setDesvio(valorDesvioPadrao);
        }

    }

    public static void vizualizarValores(List<Colunas> dadosObtidos) {
        for (int i = 0; i < dadosObtidos.size(); i++) {
            System.out.printf("Coluna  %d [%s] -\t\t- Média: %.2f  \t|| Desvio Padrão: % .2f \n", i, dadosObtidos.get(i).getCabecalho(),
                    dadosObtidos.get(i).getMedia(), dadosObtidos.get(i).getDesvio());
        }

    }

    public static void main(String[] args) {
        List<Colunas> dadosObtidos = new ArrayList<>();
        String nomeArq = JOptionPane.showInputDialog("Nome do Arquivo: ");
        AtomicInteger numeroColunas = new AtomicInteger(0);
        
        try {
            Scanner scanner = new Scanner(new FileReader("src/Arquivos/" + nomeArq));

            if (scanner.hasNext()) {
                String linha = scanner.nextLine();

                //lendo a primeira linha (esperado #NAME01, NAME02, NAME03, ...)
                lerCabecalho(linha, dadosObtidos, numeroColunas);

                //lendo o restante do arquivo (esperado #VAL01, VAL02, VAL03, ...)
                if (lerArquivo(scanner, dadosObtidos, numeroColunas)) {

                    //calcular media e desvido padrao de cada coluna 
                    calcularMediaDesvio(dadosObtidos);

                    //imprimir valores
                    vizualizarValores(dadosObtidos);
                }
                else {
                    System.out.println("\tErro no formato do arquivo!\n"
                            + "\tNº deCabeçalhos diferente no Nº de Valores.");
                }

            }
            else {
                System.out.println("Arquivo Vazio!");
            }

        } catch (FileNotFoundException ex) {
            Logger.getLogger(Programa01.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

}
