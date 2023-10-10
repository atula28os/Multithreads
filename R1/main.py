from alpha import demo
from beta import trail

from alpha.config import Configuration as AlphaConfig
from beta.config import Configuration as BetaConfig

def main():
    demo.get_alpha()
    print(AlphaConfig.AUTHOR)
    trail.get_beta()
    print(BetaConfig.EMAIL)

if __name__ == '__main__':
    main()