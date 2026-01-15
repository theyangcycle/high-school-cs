# Read input
bronze_before, bronze_after = map(int, input().split())
silver_before, silver_after = map(int, input().split())
gold_before, gold_after = map(int, input().split())
plat_before, plat_after = map(int, input().split())

# Work backwards from top to bottom
# Platinum: no one leaves, so promotions IN = increase
gold_to_plat = plat_after - plat_before

# Gold: after = before - promoted_out + promoted_in
# So: promoted_in = after - before + promoted_out
silver_to_gold = gold_after - gold_before + gold_to_plat

# Silver: same logic
bronze_to_silver = silver_after - silver_before + silver_to_gold

print(bronze_to_silver)
print(silver_to_gold)
print(gold_to_plat)