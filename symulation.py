import generator
import Tripling_codder
import Channel
import Tripling_decoder
import ResultsTable
import BSC_Channel
import Gilbert_Channel


generator.generate_f(10000)       #parametr ilosc generowanych bitów
Tripling_codder.tripling_code()
#Channel.passing()
BSC_Channel.passing(0.01)     #parametr N - prawdopodobienstwo pojedynczego bledu w modelu BSC
#Gilbert_Channel.passing(0.01, 0.1, 0, 0.5)       #G_B-prawd. GOOD->BAD 0.01 ,B_G-prawd. BAD->GOOD 0.1,
                                # errorGood-prawd. bledu w stanie Good ok.0%, errorBad prwad. bledu w stanie BAD ok50%
                            #wstepne absorwacja 99,96% przy bledzie 0.01, ok. 50% przy 0.5
Tripling_decoder.tripling_decode()
ResultsTable.scores()

