# A image classifier applied to time series data

Tendo em vista o excelente desempenho das redes neurais convolucionais para reconhecimento de imagens, é razoável pensar que se possa também aplicar tais modelos à séries temporais, uma vez que essas tenham sido convertidas para o mesmo formado (2d). 

Dessa forma, implementa-se aqui um classificador de séries temporais baseado em  algoritmos de aprendizado.
A arquitetura da rede da CNN foi inspirada no modelo proposto por [Hatami et al.(2018)](https://link.springer.com/article/10.1007/s10115-018-1264-0). Entretanto, para a representação das séries temporais, utilizou-se a metodologia proposta por [Yanqing Ye (2018)](https://link.springer.com/article/10.1007/s10115-018-1264-0)
