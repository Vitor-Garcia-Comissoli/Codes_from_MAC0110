#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Servidor web para pÃ¡gina da guitar heroine"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from ep10 import crie_guitarra, produza_musica

import json

# CONSTANTE
PORT = 8000

#--------------------------------------------------------------------------------
def main():
    '''(None) -> None

    Cria um controlador http e inicia o servidor na porta PORT
    '''
    port = PORT
    print(f'VÃ¡ para o seu navegador em http://localhost:{port}/ e cruze os dedos ;-)')
    print(f'Para encerrar venha atÃ© estÃ¡ janela e tecle CTRL+C')
    server = HTTPServer(('', port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

#------------------------------------------------------------------------------
class Handler(BaseHTTPRequestHandler):
    """ Um HTTP controlador de pÃ¡gina web da guitarra digital."""
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text')
        self.end_headers()

        if self.path == '/':
            # pegue a representaÃ§Ã£o da guitarra
            data = json.dumps(crie_guitarra(), )
            # produza e pegue a mÃºsica prÃ©-definida
            song = json.dumps(produza_musica(), )
            # crie a pÃ¡gina
            self.wfile.write(PREFIXO.encode('utf8'))
            self.wfile.write(data.encode('utf8'))
            self.wfile.write(MEIO.encode('utf8'))
            self.wfile.write(song.encode('utf8'))
            self.wfile.write(SUFIXO.encode('utf8'))
        else:
            self.wfile.write(''.encode('utf8'))
        
#---------------------------------------------------------------------------------
# MAIS CONSTANTES
# parte incial da pÃ¡gina HTML
PREFIXO = """
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width">

    <title>Guitar Heroine</title>

    <link rel="stylesheet" href="">
    <!--[if lt IE 9]>
      <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
  </head>

  <body>
    <h1>Guitar Heroine</h1>
    <button>â–º Ouvir mÃºsica</button>
    <pre></pre>
    <p id="demo"></p>
  </body>

<script>

var strings = """

# parte central da pÃ¡gina HTML
MEIO     = """;
var song = """

# parte final da pÃ¡gina HTML
SUFIXO = """;

  // variÃ¡veis globais
  var sample_rate = 44100;
  var channels    = 1;
  var keys        = [];
  var frames      = song[0].length;
  var notas       = song.length;
  var frameCount  = frames*notas;
  
   
  // variÃ¡veis de contexto
  var audioCtx       = new (window.AudioContext || window.webkitAudioContext)();
  var button         = document.querySelector('button');
  var myArrayBuffer  = audioCtx.createBuffer(channels, frameCount , sample_rate);
  var myArrayBuffer1 = audioCtx.createBuffer(channels, frames , sample_rate);

  // funÃ§Ã£o de normalizaÃ§Ã£o
  function scale(samples) {
    return (samples.map(function(x) { return x/256.0; }));
  }
  
  // mapeamento do teclado com as notas musicais
  demoP = document.getElementById("demo");
  strings.forEach(function(item, index) { 
    var key = item[0];
    var msg = item[1];
    var keyCode = key.toUpperCase().charCodeAt(0);
    keys[keyCode] = item;
    demoP.innerHTML = demoP.innerHTML + key + ": "+msg +"<br>"; 
  });
  
  
  // funÃ§Ã£o interativa de entradas pelo teclado
  function playKey(keyCode) {
    note_samples = keys[keyCode][2];
    note_samples = scale(note_samples);
          
    var nowBuffering = myArrayBuffer1.getChannelData(0);
    for (var i = 0; i < frames; i++) {
        nowBuffering[i] = note_samples[i];            
    }
    var source = audioCtx.createBufferSource();
    source.buffer = myArrayBuffer1;
    source.connect(audioCtx.destination);
    //source.loop = true;
    source.start();
    
    source.onended = () => {
      console.log('Guitarra finalizada');
    }   
        
  }
  
  // mapeamento de teclado com a funÃ§Ã£o iterativa
  document.addEventListener('keydown', (event) => {
      const keyName = event.key;
      if (event.which in keys) {
          playKey(event.which);
      } 
  }, false);
  
  // funÃ§Ã£o para dar inÃ­cio Ã  mÃºsica prÃ©-definida
  button.onclick = function() {
      var nowBuffering = myArrayBuffer.getChannelData(0);
      for (var i = 0; i < notas; i++) {
        samples_=scale(song[i]);
        for (var j = 0; j < frames; j++) {
            nowBuffering[i*frames+j] = samples_[j];            
        }
      }     
        
      var source = audioCtx.createBufferSource();
      source.buffer = myArrayBuffer;
      source.connect(audioCtx.destination);
      // source.loop = true;
      source.start();
        
        
      source.onended = () => {
          console.log('ViolÃ£o finalizado');
      }
      // window.setTimeout(loop, 1000);
  }
</script>
</head>

</html>
"""

#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()