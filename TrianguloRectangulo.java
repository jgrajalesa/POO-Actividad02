package PruebasFigura;

public class TrianguloRectangulo {
    int base;
    int altura;

    public TrianguloRectangulo(int base, int altura) {
        this.base = base;
        this.altura = altura;
    }

    public double calcularArea() {
        return (base * altura / 2);
    }

    public double calcularPerimetro() {
        return base + altura + calcularHipotenusa();
    }

    public double calcularHipotenusa() {
        return Math.pow(base * base + altura * altura, 0.5);
    }

    public void determinarTipoTriangulo() {
        if ((base == altura) && (base == calcularHipotenusa()) && (altura == calcularHipotenusa())) {
            System.out.println("Es un triangulo equilatero");
        } else if ((base != altura) && (base != calcularHipotenusa()) && (altura != calcularHipotenusa())) {
            System.out.println("Es un triangulo escaleno");
        } else {
            System.out.println("Es un triangulo isosceles");
        }
    }
}
