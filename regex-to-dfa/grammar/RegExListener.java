// Generated from RegEx.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link RegExParser}.
 */
public interface RegExListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link RegExParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(RegExParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link RegExParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(RegExParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code epsilon}
	 * labeled alternative in {@link RegExParser#regex}.
	 * @param ctx the parse tree
	 */
	void enterEpsilon(RegExParser.EpsilonContext ctx);
	/**
	 * Exit a parse tree produced by the {@code epsilon}
	 * labeled alternative in {@link RegExParser#regex}.
	 * @param ctx the parse tree
	 */
	void exitEpsilon(RegExParser.EpsilonContext ctx);
	/**
	 * Enter a parse tree produced by the {@code identifier}
	 * labeled alternative in {@link RegExParser#regex}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(RegExParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by the {@code identifier}
	 * labeled alternative in {@link RegExParser#regex}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(RegExParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by the {@code concatenation}
	 * labeled alternative in {@link RegExParser#regex}.
	 * @param ctx the parse tree
	 */
	void enterConcatenation(RegExParser.ConcatenationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code concatenation}
	 * labeled alternative in {@link RegExParser#regex}.
	 * @param ctx the parse tree
	 */
	void exitConcatenation(RegExParser.ConcatenationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code alternation}
	 * labeled alternative in {@link RegExParser#regex}.
	 * @param ctx the parse tree
	 */
	void enterAlternation(RegExParser.AlternationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code alternation}
	 * labeled alternative in {@link RegExParser#regex}.
	 * @param ctx the parse tree
	 */
	void exitAlternation(RegExParser.AlternationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code klnee}
	 * labeled alternative in {@link RegExParser#regex}.
	 * @param ctx the parse tree
	 */
	void enterKlnee(RegExParser.KlneeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code klnee}
	 * labeled alternative in {@link RegExParser#regex}.
	 * @param ctx the parse tree
	 */
	void exitKlnee(RegExParser.KlneeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parenthesis}
	 * labeled alternative in {@link RegExParser#regex}.
	 * @param ctx the parse tree
	 */
	void enterParenthesis(RegExParser.ParenthesisContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parenthesis}
	 * labeled alternative in {@link RegExParser#regex}.
	 * @param ctx the parse tree
	 */
	void exitParenthesis(RegExParser.ParenthesisContext ctx);
	/**
	 * Enter a parse tree produced by {@link RegExParser#newline}.
	 * @param ctx the parse tree
	 */
	void enterNewline(RegExParser.NewlineContext ctx);
	/**
	 * Exit a parse tree produced by {@link RegExParser#newline}.
	 * @param ctx the parse tree
	 */
	void exitNewline(RegExParser.NewlineContext ctx);
}