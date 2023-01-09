let
    //Datas iniciais e finais                                                                                                                                                                               
    DataMin = Date.FromText ( "1995-01-01" ),
    DataMax = List.Max(f_currentAccount[data]),
//Quantidade de Dias                                                                                                                                            
    QtdeDias = Duration.Days ( DataMax - DataMin ) + 1,
// Gerar Lista e converter
    ListDatas = List.Dates ( DataMin, QtdeDias, #duration ( 1, 0, 0, 0 ) ),
    #"Convertido para Tabela" = Table.FromList ( ListDatas, Splitter.SplitByNothing(), null, null, ExtraValues.Error ),
    #"Tipo Alterado" = Table.TransformColumnTypes ( #"Convertido para Tabela", { { "Column1", type date } } ),
    #"Colunas Renomeadas" = Table.RenameColumns ( #"Tipo Alterado", { { "Column1", "Data" } } ),
//YearQuaterMonth
    Year = Table.AddColumn ( #"Colunas Renomeadas", "Year", each Date.Year ( [Data] ), Int64.Type ),
    Semerter = Table.AddColumn ( Year, "Semestre", each if Date.QuarterOfYear ( [Data] ) < 3 then "Semest 1" else "Semest 2", type text ),
    Quarter = Table.AddColumn ( Semerter, "Quarter", each "Q" & Number.ToText ( Date.QuarterOfYear ( [Data] ) ), type text ),
//month
    Month = Table.AddColumn ( Quarter, "Month", each Date.ToText ( [Data], [Format="MMM", Culture = "en-US"] ), type text ),
    MonthNum = Table.AddColumn ( Month, "NumMonth", each Date.Month ( [Data] ), Int64.Type ),
    MonthYear = Table.AddColumn ( MonthNum, "MonthYear", each Text.Combine ( { Text.From ( [Month], "pt-BR" ), Text.From ( [Year], "pt-BR" ) } ), type text ),
    UppercaseMonth = Table.TransformColumns ( MonthYear, { { "Month", Text.Proper, type text } } ),
//week
    WeekOfYear = Table.AddColumn ( UppercaseMonth, "WeekOfYear", each Date.WeekOfYear ( [Data] ), Int64.Type ),
    WeekOfMonth = Table.AddColumn ( WeekOfYear, "WeekOfMonth", each Date.WeekOfMonth ( [Data], 1 ), Int64.Type ),
//day
    Day = Table.AddColumn ( WeekOfMonth, "Day", each Date.Day ( [Data] ), Int64.Type ),
    DayWeek = Table.AddColumn ( Day, "DayOfWeek", each Date.DayOfWeek ( [Data] ), Int64.Type ),
    DayName = Table.AddColumn ( DayWeek, "DayName", each Text.Start( Date.DayOfWeekName ( [Data], "en-US" ), 3), type text ),
    DayOfYear = Table.AddColumn ( DayName, "DayOfYear", each Date.DayOfYear ( [Data] ), Int32.Type ),
    WorkDay = Table.AddColumn ( DayOfYear, "WorkDay", each if [DayOfWeek] = 0 then 0 else if [DayOfWeek] = 6 then 0 else 1, Int64.Type ),
//SmallerThanToday
    SmallerThanToday = Table.AddColumn ( WorkDay, "SmallerThanToday", each if Date.From ( [Data] ) < Date.From ( DateTime.LocalNow() ) then 1 else 0, Int64.Type ),
//actually
    ThisDay = Table.AddColumn ( SmallerThanToday, "ThisDay", each Date.IsInCurrentDay ( [Data] ), type logical ),
    ThisWeek = Table.AddColumn ( ThisDay, "ThisWeek", each Date.IsInCurrentWeek ( [Data] ), type logical ),
    ThisMonth = Table.AddColumn ( ThisWeek, "ThisMonth", each Date.IsInCurrentMonth ( [Data] ), type logical ),
    ThisQuarter = Table.AddColumn ( ThisMonth, "ThisQuarter", each Date.IsInCurrentQuarter ( [Data] ), type logical ),
    ThisYear = Table.AddColumn ( ThisQuarter, "ThisYear", each Date.IsInCurrentYear ( [Data] ), type logical ),
//previous
    PreviousDay = Table.AddColumn ( ThisYear, "PreviousDay", each Date.IsInPreviousDay ( [Data] ), type logical ),
    PreviousWeek = Table.AddColumn ( PreviousDay, "PreviousWeek", each Date.IsInPreviousWeek ( [Data] ), type logical ),
    PreviousMonth = Table.AddColumn ( PreviousWeek, "PreviousMonth", each Date.IsInPreviousMonth ( [Data] ), type logical ),
    PreviousQuarter = Table.AddColumn ( PreviousMonth, "PreviousQuarter", each Date.IsInPreviousQuarter ( [Data] ), type logical ),
    PreviousYear = Table.AddColumn ( PreviousQuarter, "PreviousYear", each Date.IsInPreviousYear ( [Data] ), type logical ),
//next
    NextDay = Table.AddColumn ( PreviousYear, "NextDay", each Date.IsInNextDay ( [Data] ), type logical ),
    NextWeek = Table.AddColumn ( NextDay, "NextWeek", each Date.IsInNextWeek ( [Data] ), type logical ),
    NextMonth = Table.AddColumn ( NextWeek, "NextMonth", each Date.IsInNextMonth ( [Data] ), type logical ),
    NextQuarter = Table.AddColumn ( NextMonth, "NextQuarter", each Date.IsInNextQuarter ( [Data] ), type logical )
in
    NextQuarter