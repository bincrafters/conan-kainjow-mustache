#include <cstdlib>
#include <kainjow/mustache.hpp>

int main()
{
    kainjow::mustache::mustache tmpl{"{{#employees}}{{name}}, {{/employees}}"};
    kainjow::mustache::data employees{kainjow::mustache::data::type::list};
    employees << kainjow::mustache::data{"name", "Steve"} << kainjow::mustache::data{"name", "Bill"};
    tmpl.render({"employees", employees}, std::cout);

    return EXIT_SUCCESS;
}
