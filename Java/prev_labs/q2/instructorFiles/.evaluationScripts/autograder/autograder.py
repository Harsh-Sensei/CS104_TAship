#Identify 3 classes which implement the java.lang.Comparable interface 
#You are given a file named "Solution.java" Write java code to create a file named it as "output.txt" and write your answer in it
#write your answer in below format
#Class1,Class2,Class3



# student soltution in output.txt


import os
import json



overall = {
    "data": []
}

data = []


#------------------------------test case 1---------------------------
msg = "No output."
total = 0
result = {
      "testid": "1",
      "status": "failed",
      "score": 0,
      "maximum marks" : 1,
      "message": ""
    }


try:
	os.system("javac Solution.java")
	os.system("java Solution")
	# file1 = open('solution.txt', 'r')
	# Lines1 = file1.readlines()
	file2 = open('output.txt', 'r')
	Lines2 = file2.readlines()
except Exception as e:
	result["message"] = str(e) 
	data.append(result)
	overall['data'] = data
	print(json.dumps(overall, indent=4))
	with open('../evaluate.json', 'w') as f:
		json.dump(overall,f,indent=4)
	exit()

present = 0

s = "AbstractChronology,AbstractRegionPainter.PaintContext.CacheMode,AccessMode,AclEntryFlag,AclEntryPermission,AclEntryType,AddressingFeature.Responses,Authenticator.RequestorType,BigDecimal,BigInteger,Boolean,Byte,ByteBuffer,Calendar,CertPathValidatorException.BasicReason,Character,Character.UnicodeScript,CharBuffer,Charset,ChronoField,ChronoUnit,ClientInfoStatus,CollationKey,Collector.Characteristics,Component.BaselineResizeBehavior,CompositeName,CompoundName,CRLReason,CryptoPrimitive,Date,Date,DayOfWeek,Desktop.Action,Diagnostic.Kind,Dialog.ModalExclusionType,Dialog.ModalityType,DocumentationTool.Location,Double,DoubleBuffer,DropMode,Duration,ElementKind,ElementType,Enum,File,FileTime,FileVisitOption,FileVisitResult,Float,FloatBuffer,FormatStyle,Formatter.BigDecimalLayoutForm,FormSubmitEvent.MethodType,GraphicsDevice.WindowTranslucency,GregorianCalendar,GroupLayout.Alignment,HijrahChronology,HijrahDate,HijrahEra,Instant,IntBuffer,Integer,IsoChronology,IsoEra,JapaneseChronology,JapaneseDate,JavaFileObject.Kind,JDBCType,JTable.PrintMode,KeyRep.Type,LayoutStyle.ComponentPlacement,LdapName,LinkOption,LocalDate,LocalDateTime,Locale.Category,Locale.FilteringMode,LocalTime,Long,LongBuffer,MappedByteBuffer,MemoryType,MessageContext.Scope,MinguoChronology,MinguoDate,MinguoEra,Modifier,Month,MonthDay,MultipleGradientPaint.ColorSpaceType,MultipleGradientPaint.CycleMethod,NestingKind,Normalizer.Form,NumericShaper.Range,ObjectName,ObjectStreamField,OffsetDateTime,OffsetTime,PKIXReason,PKIXRevocationChecker.Option,PosixFilePermission,ProcessBuilder.Redirect.Type,Proxy.Type,PseudoColumnUsage,Rdn,ResolverStyle,Resource.AuthenticationType,RetentionPolicy,RoundingMode,RowFilter.ComparisonType,RowIdLifetime,RowSorterEvent.Type,Service.Mode,Short,ShortBuffer,SignStyle,SOAPBinding.ParameterStyle,SOAPBinding.Style,SOAPBinding.Use,SortOrder,SourceVersion,SSLEngineResult.HandshakeStatus,SSLEngineResult.Status,StandardCopyOption,StandardLocation,StandardOpenOption,StandardProtocolFamily,String,SwingWorker.StateValue,TextStyle,ThaiBuddhistChronology,ThaiBuddhistDate,ThaiBuddhistEra,Thread.State,Time,Timestamp,TimeUnit,TrayIcon.MessageType,TypeKind,URI,UUID,WebParam.Mode,Window.Type,XmlAccessOrder,XmlAccessType,XmlNsForm,Year,YearMonth,ZonedDateTime,ZoneOffset,ZoneOffsetTransition,ZoneOffsetTransitionRule.TimeDefinitionAbstractChronology,AbstractRegionPainter.PaintContext.CacheMode,AccessMode,AclEntryFlag,AclEntryPermission,AclEntryType,AddressingFeature.Responses,Authenticator.RequestorType,BigDecimal,BigInteger,Boolean,Byte,ByteBuffer,Calendar,CertPathValidatorException.BasicReason,Character,Character.UnicodeScript,CharBuffer,Charset,ChronoField,ChronoUnit,ClientInfoStatus,CollationKey,Collector.Characteristics,Component.BaselineResizeBehavior,CompositeName,CompoundName,CRLReason,CryptoPrimitive,Date,Date,DayOfWeek,Desktop.Action,Diagnostic.Kind,Dialog.ModalExclusionType,Dialog.ModalityType,DocumentationTool.Location,Double,DoubleBuffer,DropMode,Duration,ElementKind,ElementType,Enum,File,FileTime,FileVisitOption,FileVisitResult,Float,FloatBuffer,FormatStyle,Formatter.BigDecimalLayoutForm,FormSubmitEvent.MethodType,GraphicsDevice.WindowTranslucency,GregorianCalendar,GroupLayout.Alignment,HijrahChronology,HijrahDate,HijrahEra,Instant,IntBuffer,Integer,IsoChronology,IsoEra,JapaneseChronology,JapaneseDate,JavaFileObject.Kind,JDBCType,JTable.PrintMode,KeyRep.Type,LayoutStyle.ComponentPlacement,LdapName,LinkOption,LocalDate,LocalDateTime,Locale.Category,Locale.FilteringMode,LocalTime,Long,LongBuffer,MappedByteBuffer,MemoryType,MessageContext.Scope,MinguoChronology,MinguoDate,MinguoEra,Modifier,Month,MonthDay,MultipleGradientPaint.ColorSpaceType,MultipleGradientPaint.CycleMethod,NestingKind,Normalizer.Form,NumericShaper.Range,ObjectName,ObjectStreamField,OffsetDateTime,OffsetTime,PKIXReason,PKIXRevocationChecker.Option,PosixFilePermission,ProcessBuilder.Redirect.Type,Proxy.Type,PseudoColumnUsage,Rdn,ResolverStyle,Resource.AuthenticationType,RetentionPolicy,RoundingMode,RowFilter.ComparisonType,RowIdLifetime,RowSorterEvent.Type, Service.Mode,Short,ShortBuffer,SignStyle,SOAPBinding.ParameterStyle,SOAPBinding.Style,SOAPBinding.Use,SortOrder,SourceVersion,SSLEngineResult.HandshakeStatus,SSLEngineResult.Status,StandardCopyOption,StandardLocation,StandardOpenOption,StandardProtocolFamily,String,SwingWorker.StateValue,TextStyle,ThaiBuddhistChronology,ThaiBuddhistDate,ThaiBuddhistEra,Thread.State,Time,Timestamp,TimeUnit,TrayIcon.MessageType,TypeKind,URI,UUID,WebParam.Mode,Window.Type,XmlAccessOrder,XmlAccessType,XmlNsForm,Year,YearMonth,ZonedDateTime,ZoneOffset,ZoneOffsetTransition,ZoneOffsetTransitionRule.TimeDefinition"

Lines1 = s.split(',')
for x in Lines1 :
    x = x.strip()
#print(Lines1)
Lines2 = Lines2[0].split(',')
#print(Lines2)
Lines2.sort()
# print(" expected : ")
# print(Lines1)
# print(" your : ")
# print(Lines2)
# if Lines1 == Lines2:
#     msg = "Correct "
#     total=1

# else:
#     msg = "Incorrect"
#     total = 0

cnt = 0
if len(Lines2) < 3 :
    total = 0
    msg = "Wrong Output, You have to give 3 classes "

for x in Lines2 :
    if x in Lines1:
        cnt=cnt+1
    else:
        msg = "Wrong Output '" + x + "' is incorrect"

# print("count is ",cnt)
if cnt == 3:
    total = 1





# if len(Lines1) < len(Lines2) :
#     total = 0
#     msg = "Wrong output, You have written extra interface '" + Lines2[len(Lines2) - 1].strip() +"' is extra or not in a correct place"
# elif len(Lines1) > len(Lines2) :
#     total = 0
#     msg = "Wrong output, Some interfaces are missing'"
# else :
#     for i in range(len(Lines1)) :
#         if Lines1[i].strip() != Lines2[i].strip() :
#             total = 0
#             msg = "Wrong output, Expected statment : '" + Lines1[i].strip() + "' Your output : '" + Lines2[i].strip() + "'"
#             break

if(total != 1) :
    result["status"] = "failed" 
else:
    result["status"] = "success" 
    msg = "Correct Output"
result["testid"] = 1
result["score"] = total
result["message"] = msg

os.system("rm output.txt")

data.append(result)



overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)
