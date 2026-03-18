function __brain_complete_files
    brain _complete_files
end

complete -c brain -f
complete -c brain -n __fish_use_subcommand -a "edit list add remove"

complete -c brain \
    -n "__fish_seen_subcommand_from edit" \
    -a "(__brain_complete_files)"
