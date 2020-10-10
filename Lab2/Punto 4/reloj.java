//Reloj
public void establecerHora(){
 
        int h;
        int m;
        int s;
 
        Calendar calendario = new GregorianCalendar();
        Date fechaHoraActual = new Date();
 
        calendario.setTime(fechaHoraActual);
 
        meridiem = calendario.get(Calendar.AM_PM);
 
        if(meridiem == 1){
            h = calendario.get(Calendar.HOUR_OF_DAY) - 12;
            if(h > 9){
                this.hora = h + "";
            }else
                this.hora = "0" + h;
        }else{
            h = calendario.get(Calendar.HOUR_OF_DAY);
            if(h > 9){
                this.hora = h + "";
            }else{
                this.hora = "0" + h;
            }
        }
 
        m = calendario.get(Calendar.MINUTE);
        if(m > 9){
            minuto = m + "";
        }else{
            minuto = "0" + m;
        }
 
        s = calendario.get(Calendar.SECOND);
        if(s > 9){
            segundo = s + "";
        }else{
            segundo = "0" + s;
        }
 
    }

