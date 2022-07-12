# Generated from ..\Lua.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LuaParser import LuaParser
else:
    from LuaParser import LuaParser

# This class defines a complete listener for a parse tree produced by LuaParser.
class LuaListener(ParseTreeListener):

    # Enter a parse tree produced by LuaParser#chunk.
    def enterChunk(self, ctx:LuaParser.ChunkContext):
        pass

    # Exit a parse tree produced by LuaParser#chunk.
    def exitChunk(self, ctx:LuaParser.ChunkContext):
        pass


    # Enter a parse tree produced by LuaParser#block.
    def enterBlock(self, ctx:LuaParser.BlockContext):
        pass

    # Exit a parse tree produced by LuaParser#block.
    def exitBlock(self, ctx:LuaParser.BlockContext):
        pass


    # Enter a parse tree produced by LuaParser#lineEnd.
    def enterLineEnd(self, ctx:LuaParser.LineEndContext):
        pass

    # Exit a parse tree produced by LuaParser#lineEnd.
    def exitLineEnd(self, ctx:LuaParser.LineEndContext):
        pass


    # Enter a parse tree produced by LuaParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:LuaParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by LuaParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:LuaParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by LuaParser#functionCallStat.
    def enterFunctionCallStat(self, ctx:LuaParser.FunctionCallStatContext):
        pass

    # Exit a parse tree produced by LuaParser#functionCallStat.
    def exitFunctionCallStat(self, ctx:LuaParser.FunctionCallStatContext):
        pass


    # Enter a parse tree produced by LuaParser#incrementalInit.
    def enterIncrementalInit(self, ctx:LuaParser.IncrementalInitContext):
        pass

    # Exit a parse tree produced by LuaParser#incrementalInit.
    def exitIncrementalInit(self, ctx:LuaParser.IncrementalInitContext):
        pass


    # Enter a parse tree produced by LuaParser#labelStat.
    def enterLabelStat(self, ctx:LuaParser.LabelStatContext):
        pass

    # Exit a parse tree produced by LuaParser#labelStat.
    def exitLabelStat(self, ctx:LuaParser.LabelStatContext):
        pass


    # Enter a parse tree produced by LuaParser#break.
    def enterBreak(self, ctx:LuaParser.BreakContext):
        pass

    # Exit a parse tree produced by LuaParser#break.
    def exitBreak(self, ctx:LuaParser.BreakContext):
        pass


    # Enter a parse tree produced by LuaParser#gotoLabel.
    def enterGotoLabel(self, ctx:LuaParser.GotoLabelContext):
        pass

    # Exit a parse tree produced by LuaParser#gotoLabel.
    def exitGotoLabel(self, ctx:LuaParser.GotoLabelContext):
        pass


    # Enter a parse tree produced by LuaParser#doStat.
    def enterDoStat(self, ctx:LuaParser.DoStatContext):
        pass

    # Exit a parse tree produced by LuaParser#doStat.
    def exitDoStat(self, ctx:LuaParser.DoStatContext):
        pass


    # Enter a parse tree produced by LuaParser#whileLoop.
    def enterWhileLoop(self, ctx:LuaParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by LuaParser#whileLoop.
    def exitWhileLoop(self, ctx:LuaParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by LuaParser#repeatLoop.
    def enterRepeatLoop(self, ctx:LuaParser.RepeatLoopContext):
        pass

    # Exit a parse tree produced by LuaParser#repeatLoop.
    def exitRepeatLoop(self, ctx:LuaParser.RepeatLoopContext):
        pass


    # Enter a parse tree produced by LuaParser#ifShortHand.
    def enterIfShortHand(self, ctx:LuaParser.IfShortHandContext):
        pass

    # Exit a parse tree produced by LuaParser#ifShortHand.
    def exitIfShortHand(self, ctx:LuaParser.IfShortHandContext):
        pass


    # Enter a parse tree produced by LuaParser#ifThen.
    def enterIfThen(self, ctx:LuaParser.IfThenContext):
        pass

    # Exit a parse tree produced by LuaParser#ifThen.
    def exitIfThen(self, ctx:LuaParser.IfThenContext):
        pass


    # Enter a parse tree produced by LuaParser#forLoop.
    def enterForLoop(self, ctx:LuaParser.ForLoopContext):
        pass

    # Exit a parse tree produced by LuaParser#forLoop.
    def exitForLoop(self, ctx:LuaParser.ForLoopContext):
        pass


    # Enter a parse tree produced by LuaParser#forShortHand.
    def enterForShortHand(self, ctx:LuaParser.ForShortHandContext):
        pass

    # Exit a parse tree produced by LuaParser#forShortHand.
    def exitForShortHand(self, ctx:LuaParser.ForShortHandContext):
        pass


    # Enter a parse tree produced by LuaParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:LuaParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by LuaParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:LuaParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by LuaParser#localFunctionDeclaration.
    def enterLocalFunctionDeclaration(self, ctx:LuaParser.LocalFunctionDeclarationContext):
        pass

    # Exit a parse tree produced by LuaParser#localFunctionDeclaration.
    def exitLocalFunctionDeclaration(self, ctx:LuaParser.LocalFunctionDeclarationContext):
        pass


    # Enter a parse tree produced by LuaParser#localVariableDecalaration.
    def enterLocalVariableDecalaration(self, ctx:LuaParser.LocalVariableDecalarationContext):
        pass

    # Exit a parse tree produced by LuaParser#localVariableDecalaration.
    def exitLocalVariableDecalaration(self, ctx:LuaParser.LocalVariableDecalarationContext):
        pass


    # Enter a parse tree produced by LuaParser#printStatement.
    def enterPrintStatement(self, ctx:LuaParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by LuaParser#printStatement.
    def exitPrintStatement(self, ctx:LuaParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by LuaParser#attnamelist.
    def enterAttnamelist(self, ctx:LuaParser.AttnamelistContext):
        pass

    # Exit a parse tree produced by LuaParser#attnamelist.
    def exitAttnamelist(self, ctx:LuaParser.AttnamelistContext):
        pass


    # Enter a parse tree produced by LuaParser#attrib.
    def enterAttrib(self, ctx:LuaParser.AttribContext):
        pass

    # Exit a parse tree produced by LuaParser#attrib.
    def exitAttrib(self, ctx:LuaParser.AttribContext):
        pass


    # Enter a parse tree produced by LuaParser#retstat.
    def enterRetstat(self, ctx:LuaParser.RetstatContext):
        pass

    # Exit a parse tree produced by LuaParser#retstat.
    def exitRetstat(self, ctx:LuaParser.RetstatContext):
        pass


    # Enter a parse tree produced by LuaParser#label.
    def enterLabel(self, ctx:LuaParser.LabelContext):
        pass

    # Exit a parse tree produced by LuaParser#label.
    def exitLabel(self, ctx:LuaParser.LabelContext):
        pass


    # Enter a parse tree produced by LuaParser#funcname.
    def enterFuncname(self, ctx:LuaParser.FuncnameContext):
        pass

    # Exit a parse tree produced by LuaParser#funcname.
    def exitFuncname(self, ctx:LuaParser.FuncnameContext):
        pass


    # Enter a parse tree produced by LuaParser#varlist.
    def enterVarlist(self, ctx:LuaParser.VarlistContext):
        pass

    # Exit a parse tree produced by LuaParser#varlist.
    def exitVarlist(self, ctx:LuaParser.VarlistContext):
        pass


    # Enter a parse tree produced by LuaParser#namelist.
    def enterNamelist(self, ctx:LuaParser.NamelistContext):
        pass

    # Exit a parse tree produced by LuaParser#namelist.
    def exitNamelist(self, ctx:LuaParser.NamelistContext):
        pass


    # Enter a parse tree produced by LuaParser#explist.
    def enterExplist(self, ctx:LuaParser.ExplistContext):
        pass

    # Exit a parse tree produced by LuaParser#explist.
    def exitExplist(self, ctx:LuaParser.ExplistContext):
        pass


    # Enter a parse tree produced by LuaParser#exp.
    def enterExp(self, ctx:LuaParser.ExpContext):
        pass

    # Exit a parse tree produced by LuaParser#exp.
    def exitExp(self, ctx:LuaParser.ExpContext):
        pass


    # Enter a parse tree produced by LuaParser#prefixexp.
    def enterPrefixexp(self, ctx:LuaParser.PrefixexpContext):
        pass

    # Exit a parse tree produced by LuaParser#prefixexp.
    def exitPrefixexp(self, ctx:LuaParser.PrefixexpContext):
        pass


    # Enter a parse tree produced by LuaParser#functioncall.
    def enterFunctioncall(self, ctx:LuaParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by LuaParser#functioncall.
    def exitFunctioncall(self, ctx:LuaParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by LuaParser#varOrExp.
    def enterVarOrExp(self, ctx:LuaParser.VarOrExpContext):
        pass

    # Exit a parse tree produced by LuaParser#varOrExp.
    def exitVarOrExp(self, ctx:LuaParser.VarOrExpContext):
        pass


    # Enter a parse tree produced by LuaParser#var_.
    def enterVar_(self, ctx:LuaParser.Var_Context):
        pass

    # Exit a parse tree produced by LuaParser#var_.
    def exitVar_(self, ctx:LuaParser.Var_Context):
        pass


    # Enter a parse tree produced by LuaParser#varSuffix.
    def enterVarSuffix(self, ctx:LuaParser.VarSuffixContext):
        pass

    # Exit a parse tree produced by LuaParser#varSuffix.
    def exitVarSuffix(self, ctx:LuaParser.VarSuffixContext):
        pass


    # Enter a parse tree produced by LuaParser#nameAndArgs.
    def enterNameAndArgs(self, ctx:LuaParser.NameAndArgsContext):
        pass

    # Exit a parse tree produced by LuaParser#nameAndArgs.
    def exitNameAndArgs(self, ctx:LuaParser.NameAndArgsContext):
        pass


    # Enter a parse tree produced by LuaParser#args.
    def enterArgs(self, ctx:LuaParser.ArgsContext):
        pass

    # Exit a parse tree produced by LuaParser#args.
    def exitArgs(self, ctx:LuaParser.ArgsContext):
        pass


    # Enter a parse tree produced by LuaParser#functiondef.
    def enterFunctiondef(self, ctx:LuaParser.FunctiondefContext):
        pass

    # Exit a parse tree produced by LuaParser#functiondef.
    def exitFunctiondef(self, ctx:LuaParser.FunctiondefContext):
        pass


    # Enter a parse tree produced by LuaParser#funcbody.
    def enterFuncbody(self, ctx:LuaParser.FuncbodyContext):
        pass

    # Exit a parse tree produced by LuaParser#funcbody.
    def exitFuncbody(self, ctx:LuaParser.FuncbodyContext):
        pass


    # Enter a parse tree produced by LuaParser#parlist.
    def enterParlist(self, ctx:LuaParser.ParlistContext):
        pass

    # Exit a parse tree produced by LuaParser#parlist.
    def exitParlist(self, ctx:LuaParser.ParlistContext):
        pass


    # Enter a parse tree produced by LuaParser#tableconstructor.
    def enterTableconstructor(self, ctx:LuaParser.TableconstructorContext):
        pass

    # Exit a parse tree produced by LuaParser#tableconstructor.
    def exitTableconstructor(self, ctx:LuaParser.TableconstructorContext):
        pass


    # Enter a parse tree produced by LuaParser#fieldlist.
    def enterFieldlist(self, ctx:LuaParser.FieldlistContext):
        pass

    # Exit a parse tree produced by LuaParser#fieldlist.
    def exitFieldlist(self, ctx:LuaParser.FieldlistContext):
        pass


    # Enter a parse tree produced by LuaParser#field.
    def enterField(self, ctx:LuaParser.FieldContext):
        pass

    # Exit a parse tree produced by LuaParser#field.
    def exitField(self, ctx:LuaParser.FieldContext):
        pass


    # Enter a parse tree produced by LuaParser#fieldsep.
    def enterFieldsep(self, ctx:LuaParser.FieldsepContext):
        pass

    # Exit a parse tree produced by LuaParser#fieldsep.
    def exitFieldsep(self, ctx:LuaParser.FieldsepContext):
        pass


    # Enter a parse tree produced by LuaParser#operatorOr.
    def enterOperatorOr(self, ctx:LuaParser.OperatorOrContext):
        pass

    # Exit a parse tree produced by LuaParser#operatorOr.
    def exitOperatorOr(self, ctx:LuaParser.OperatorOrContext):
        pass


    # Enter a parse tree produced by LuaParser#operatorAnd.
    def enterOperatorAnd(self, ctx:LuaParser.OperatorAndContext):
        pass

    # Exit a parse tree produced by LuaParser#operatorAnd.
    def exitOperatorAnd(self, ctx:LuaParser.OperatorAndContext):
        pass


    # Enter a parse tree produced by LuaParser#operatorComparison.
    def enterOperatorComparison(self, ctx:LuaParser.OperatorComparisonContext):
        pass

    # Exit a parse tree produced by LuaParser#operatorComparison.
    def exitOperatorComparison(self, ctx:LuaParser.OperatorComparisonContext):
        pass


    # Enter a parse tree produced by LuaParser#operatorStrcat.
    def enterOperatorStrcat(self, ctx:LuaParser.OperatorStrcatContext):
        pass

    # Exit a parse tree produced by LuaParser#operatorStrcat.
    def exitOperatorStrcat(self, ctx:LuaParser.OperatorStrcatContext):
        pass


    # Enter a parse tree produced by LuaParser#operatorAddSub.
    def enterOperatorAddSub(self, ctx:LuaParser.OperatorAddSubContext):
        pass

    # Exit a parse tree produced by LuaParser#operatorAddSub.
    def exitOperatorAddSub(self, ctx:LuaParser.OperatorAddSubContext):
        pass


    # Enter a parse tree produced by LuaParser#operatorMulDivMod.
    def enterOperatorMulDivMod(self, ctx:LuaParser.OperatorMulDivModContext):
        pass

    # Exit a parse tree produced by LuaParser#operatorMulDivMod.
    def exitOperatorMulDivMod(self, ctx:LuaParser.OperatorMulDivModContext):
        pass


    # Enter a parse tree produced by LuaParser#operatorBitwise.
    def enterOperatorBitwise(self, ctx:LuaParser.OperatorBitwiseContext):
        pass

    # Exit a parse tree produced by LuaParser#operatorBitwise.
    def exitOperatorBitwise(self, ctx:LuaParser.OperatorBitwiseContext):
        pass


    # Enter a parse tree produced by LuaParser#operatorUnary.
    def enterOperatorUnary(self, ctx:LuaParser.OperatorUnaryContext):
        pass

    # Exit a parse tree produced by LuaParser#operatorUnary.
    def exitOperatorUnary(self, ctx:LuaParser.OperatorUnaryContext):
        pass


    # Enter a parse tree produced by LuaParser#operatorPrint.
    def enterOperatorPrint(self, ctx:LuaParser.OperatorPrintContext):
        pass

    # Exit a parse tree produced by LuaParser#operatorPrint.
    def exitOperatorPrint(self, ctx:LuaParser.OperatorPrintContext):
        pass


    # Enter a parse tree produced by LuaParser#operatorPeek.
    def enterOperatorPeek(self, ctx:LuaParser.OperatorPeekContext):
        pass

    # Exit a parse tree produced by LuaParser#operatorPeek.
    def exitOperatorPeek(self, ctx:LuaParser.OperatorPeekContext):
        pass


    # Enter a parse tree produced by LuaParser#operatorPower.
    def enterOperatorPower(self, ctx:LuaParser.OperatorPowerContext):
        pass

    # Exit a parse tree produced by LuaParser#operatorPower.
    def exitOperatorPower(self, ctx:LuaParser.OperatorPowerContext):
        pass


    # Enter a parse tree produced by LuaParser#number.
    def enterNumber(self, ctx:LuaParser.NumberContext):
        pass

    # Exit a parse tree produced by LuaParser#number.
    def exitNumber(self, ctx:LuaParser.NumberContext):
        pass


    # Enter a parse tree produced by LuaParser#string.
    def enterString(self, ctx:LuaParser.StringContext):
        pass

    # Exit a parse tree produced by LuaParser#string.
    def exitString(self, ctx:LuaParser.StringContext):
        pass



del LuaParser