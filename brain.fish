function __brain_complete_edit
    brain _complete_edit
end

complete -c brain -f
complete -c brain -n __fish_use_subcommand -a "edit list new"

complete -c brain \
    -n "__fish_seen_subcommand_from edit" \
    -a "(__brain_complete_edit)"
