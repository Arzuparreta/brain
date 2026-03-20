function __brain_complete_files
    brain complete_files
end

complete -c brain -f
complete -c brain -n __fish_use_subcommand -a "edit list add remove rename see"

complete -c brain \
    -n "__fish_seen_subcommand_from edit remove see" \
    -a "(__brain_complete_files)"
complete -c brain -n "__fish_seen_subcommand_from rename" -a "(__brain_complete_files)"
