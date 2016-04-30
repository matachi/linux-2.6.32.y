#include <stdlib.h>
#include <string.h>
#include <time.h>

#define LKC_DIRECT_LINK
#include "lkc.h"

static inline bool sym_has_prompt(struct symbol *sym)
{
	struct property *prop;

	for_all_prompts(sym, prop)
		return true;

	return false;
}

bool valid_symbol(struct symbol *sym)
{
	return (sym->type == S_BOOLEAN || sym->type == S_TRISTATE) &&
	        sym->name && sym_has_prompt(sym) && sym->curr.tri == 0;
}

void print_random_symbols(unsigned int num, char *kconfig)
{
	unsigned int i, k;
	unsigned int j = 0;
	struct symbol *sym;
	unsigned int number_of_symbols = 0;
	struct symbol **symbols;
	unsigned int random_nums[num];

	conf_parse(kconfig);
	conf_read(NULL);
	srand(time(NULL));

	for_all_symbols(i, sym) {
		if (valid_symbol(sym)) ++number_of_symbols;
	}
	symbols = malloc(number_of_symbols * sizeof(struct symbol *));
	for_all_symbols(i, sym) {
		if (valid_symbol(sym)) symbols[j++] = sym;
	}

	j = 0;
	while (j < num) {
		i = rand() % number_of_symbols;
		for (k = 0; k < j; ++k) {
			if (random_nums[k] == i) break;
		}
		if (k == j) random_nums[j++] = i;
	}

	for (i = 0; i < num; ++i) {
		printf("%s\n", symbols[random_nums[i]]->name);
	}

	free(symbols);
}

int main(int ac, char** av)
{
	print_random_symbols(atoi(av[2]), av[1]);
	return EXIT_SUCCESS;
}
