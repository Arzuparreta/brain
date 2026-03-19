
function __brain_complete_files
    brain complete_files
end

complete -c brain -f
complete -c brain -n "__fish_use_subcommand" -a "edit add list remove rename"
complete -c brain -n "__fish_seen_subcommand_from edit remove" -a "(__brain_complete_files)"
complete -c brain -n "__fish_seen_subcommand_from rename" -a "(__brain_complete_files)"
