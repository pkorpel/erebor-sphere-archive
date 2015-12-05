" Vim syntax file
" Language:	SphereScript
" Maintainer:	Pavel Mican (sirglorg@gmail.com)
" Last Change:	2015 Sep 28

" For version 5.x: Clear all syntax items
" For version 6.x: Quit when a syntax file was already loaded
if version < 600
  syntax clear
elseif exists("b:current_syntax")
  finish
endif

" SphereScript is case insensitive
syn case ignore

" These are Notes thingies that had an equivalent in the vb highlighter
" or I was already familiar with them
syn keyword sphscriptStatement dorand doswitch
syn keyword sphscriptStatement else elsif elseif endif enddo endwhile
syn keyword sphscriptStatement if
syn keyword sphscriptStatement while
syn match   sphscriptStatement "&\||\|!\|=\|<?\|?>\|<\|>\|%\|*\|+\|-\|/\|^\|\~"


syn keyword sphscriptDatatype Array Currency Double Integer Long Single String String$ Variant
syn keyword sphscriptDatatype act arg args argo argv
syn keyword sphscriptDatatype char cont CurrentSkill currentSkillParam currentSkillTarget1 currentSkillTarget2
syn keyword sphscriptDatatype lastnew lastnewchar link
syn keyword sphscriptDatatype qtag
syn keyword sphscriptDatatype serv src
syn keyword sphscriptDatatype tag targ this topobj Trigger
syn keyword sphscriptDatatype var

syn keyword sphscriptTriggers Field Button Navigator
syn keyword sphscriptTriggers abort
syn keyword sphscriptTriggers fail
syn keyword sphscriptTriggers select start stroke success
syn keyword sphscriptTriggers on
syn keyword sphscriptTriggers eof
syn match   sphscriptTriggers "@\a\+\>"
syn match   sphscriptTriggers "\*\*.\+\>"

syn keyword sphscriptVariables action AddTimer advrate amount anim armor attr aversions
syn keyword sphscriptVariables baseid bloodcolor body
syn keyword sphscriptVariables can color
syn keyword sphscriptVariables dam defname desires dex dispid
syn keyword sphscriptVariables fame findlayer findmemory findType flags flip food foodtype
syn keyword sphscriptVariables HasTimer hits hitpoints
syn keyword sphscriptVariables icon id int intelligence itemnewbie
syn keyword sphscriptVariables karma key
syn keyword sphscriptVariables obody oskin
syn keyword sphscriptVariables mana maxhits maxmana maxstam memoryfindtype more more1 more2 morep morex morey morez moverate
syn keyword sphscriptVariables name npc
syn keyword sphscriptVariables p
syn keyword sphscriptVariables RemoveTimer resources resources2 resmake
syn keyword sphscriptVariables serial shelter skillmake skillsum stam stamina statsum str strength strlen strmatch
syn keyword sphscriptVariables tdata1 tdata2 tdata3 tdata4 tevents timer timerd title tspeech type
syn keyword sphscriptVariables uid
syn keyword sphscriptVariables value
syn keyword sphscriptVariables weight

syn keyword sphscriptFunction AddTriggerGroup allskills attack
syn keyword sphscriptFunction bounce
syn keyword sphscriptFunction CanSeeLos charExists CheckSuccess classmessage consume create
syn keyword sphscriptFunction damage DelaySkillStroke dialog dismount distanceFrom dupe
syn keyword sphscriptFunction emote effect equip eval
syn keyword sphscriptFunction invul isChar isChardef isDead isGM isItem isItemdef itemExists
syn keyword sphscriptFunction findres finduid fix font
syn keyword sphscriptFunction gm go
syn keyword sphscriptFunction makeitem message mount
syn keyword sphscriptFunction newitem newitemsafe newnpc npcExists nuke
syn keyword sphscriptFunction playerExists profession
syn keyword sphscriptFunction rand redmessage resurrect return remove RemoveTriggerGroup rescount restest
syn keyword sphscriptFunction say sayU sayUA settext speak speakU sound skillCheck spellEffect srcCanSeeLOS suicide sysMessage
syn keyword sphscriptFunction target Trigger_Fail Trigger_Start Trigger_Success
syn keyword sphscriptFunction update unequip use
" GUMPS
syn keyword sphscriptFunction dialog_forcePage dialog_linkButton dialog_newPage dialog_page
syn keyword sphscriptFunction lastTextLine
syn keyword sphscriptFunction newTextLine
syn keyword sphscriptFunction questDialog_addResponse questDialog_baseButt questDialog_create questDialog_HTMLGUMP
syn keyword sphscriptFunction page
syn keyword sphscriptFunction resizepic
syn keyword sphscriptFunction setLocation
syn keyword sphscriptFunction texta textentry
syn match   sphscriptFunction "^\[.\+\]"


syn keyword sphscriptMethods AppendToTextList ArrayAppend ArrayReplace ArrayGetIndex
syn keyword sphscriptMethods Anatomy Alchemy AnimalLore Archery ArmsLore
syn keyword sphscriptMethods Begging Blacksmithing Bowcraft
syn keyword sphscriptMethods Camping Carpentry Cartography Cooking
syn keyword sphscriptMethods DetectingHidden
syn keyword sphscriptMethods Enticement EI EvaluatingIntel
syn keyword sphscriptMethods Fencing Fishing Forensics
syn keyword sphscriptMethods Healing Herding Hiding
syn keyword sphscriptMethods Inscription ItemID
syn keyword sphscriptMethods LockPicking Lumberjacking 
syn keyword sphscriptMethods Macefighting Magery MagicResistance Meditation Mining Musicianship
syn keyword sphscriptMethods Necromancy
syn keyword sphscriptMethods Peacemaking Provocation Parrying Poisoning
syn keyword sphscriptMethods RemoveTrap resist
syn keyword sphscriptMethods Snooping SpiritSpeak Stealing Stealth Swordsmanship
syn keyword sphscriptMethods Tactics Tailoring Taming TasteID Tinkering Tracking
syn keyword sphscriptMethods Veterinary
syn keyword sphscriptMethods Wrestling

syn keyword sphscriptEvents Compare OnError


syn keyword sphscriptTodo contained	TODO

"integer number, or floating point number without a dot.
syn match  sphscriptNumber		"\<\d\+\>"
"floating point number, with dot
syn match  sphscriptNumber		"\<\d\+\.\d*\>"

" String and Character constants
syn region  sphscriptString		start=+"+  end=+"+
syn region  sphscriptComment		start="//" end="$" contains=sphscriptTodo
"syn region  sphscriptLineNumber	start="^\d" end="\s"
syn match   sphscriptTypeSpecifier	"[a-zA-Z0-9][\$%&!#]"ms=s+1

" Define the default highlighting.
" For version 5.7 and earlier: only when not done already
" For version 5.8 and later: only when an item doesn't have highlighting yet
if version >= 508 || !exists("did_sphscript_syntax_inits")
  if version < 508
    let did_sphscript_syntax_inits = 1
    command -nargs=+ HiLink hi link <args>
  else
    command -nargs=+ HiLink hi def link <args>
  endif

  hi sphscriptTriggers	term=underline ctermfg=DarkGreen guifg=SeaGreen gui=bold

  HiLink sphscriptVariables    sphscriptTriggers
  HiLink sphscriptLineNumber    Comment
  HiLink sphscriptDatatype      Type
  HiLink sphscriptNumber        Number
  HiLink sphscriptError         Error
  HiLink sphscriptStatement     Statement
  HiLink sphscriptString        String
  HiLink sphscriptComment       Comment
  HiLink sphscriptTodo          Todo
  HiLink sphscriptFunction      Identifier
  HiLink sphscriptMethods       PreProc
  HiLink sphscriptEvents        Special
  HiLink sphscriptTypeSpecifier Type

  delcommand HiLink
endif

let b:current_syntax = "sphscript"

" vim: ts=8
