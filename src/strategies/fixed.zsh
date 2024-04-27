#--------------------------------------------------------------------#
# Fixed Command Suggestion Strategy                                  #
#--------------------------------------------------------------------#
# Always suggests a fixed command regardless of the input.
#

_zsh_autosuggest_strategy_fixed() {
    # Reset options to defaults and enable LOCAL_OPTIONS
	emulate -L zsh

	# Enable globbing flags so that we can use (#m) and (x~y) glob operator
	setopt EXTENDED_GLOB
    local user_input="$1"
    escaped_input=$(echo "$user_input" | sed 's/[\x01-\x1F\x7F]/\\&/g')

    # Use the Python script to get the suggestion
    local suggestion=$(python3 ai.py "$escaped_input")

	echo $suggestion
	typeset -g suggestion="$suggestion"
}
