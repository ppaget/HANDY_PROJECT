
// parse en remplissant struct paramètres
// struct contenant variables 
// tableau de struct qui se remplit avec variables
// fichier contenant variables
// python lit ces fichiers et plot tout
// méthode runge kutta pour équa diff --> comparer les 2 méthodes pour précision


double * calculs(double xc, double xe, double y, double w, double am, double aM, double bc, double be, double g, double l, double s, double d, double k, double r) {

    double wth = (r * xc) + (k * r * xe) ;
    double cc ;
    double ce ;
    double ac ;
    double ae ;


    if (wth != 0) {
        double cc = min(1, w/wth) * s * xc ;
        double ce = min(1, w/wth) * k * s * xe ;
    }
    else {
        double cc = s * xc ;
        double ce = k * s * xe ;
    }
    if (s * xc != 0) {
        double ac = am + (max(0, 1 - (cc / (s * xc))) * (aM - am)) ;
    }
    else {
        double ac = am ;
    } 
    if (s * xe != 0) {
        double ae = am + (max(0, 1 - (ce / (s * xe))) * (aM - am)) ;
    }
    else {
        double ae = am ;
    }

    double dxc = (bc * xc) - (ac * xc) ;
    double dxe = (be * xe) - (ae * xe) ;
    double dy = (g * y * (l - y)) - (d * xc * y) ;
    double dw = (d * xc * y) - cc - ce ;

    double xc = xc + dxc ;
    if (xc < 0) xc = 0 ;
    double xe = xe + dxe ;
    if (xe < 0) xe = 0 ;
    double y = y + dy ;
    if (y < 0) y = 0 ;
    double w = w + dw ;
    if (w < 0) w = 0 ;


    // self.metrics = [xc, xe, y, w]
    // return [xc, xe, y, w]


}