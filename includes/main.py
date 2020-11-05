def define_env(env):

  env.variables['greeting'] = 'Hello'
  env.variables['farewell'] = 'Goodbye'

  @env.macro
  def helloworld():
      return "Hello, world !"

  @env.filter
  def reverse(x):
      "Reverse a string (and uppercase)"
      return x.upper()[::-1]

  env.macro(len)
  env.filter(len)



# """
# PRIMER on [mkdocs-macros]
# (https://mkdocs-macros-plugin.readthedocs.io/en/latest/python/):

#   - 'define_env(env)' is mkdocs-macros hook function.

#   - 'env' variable passed into the 'define_env' is an object containing a bunch
#   of useful information about the project and page. It has the following
#   items: variables, macro, filters, filter, project_dir, conf. See mkdocs-macros docs for more info.

#   - You can access [global] variables with:

#     env.[variables|macro|filters|filter|project_dir|conf].*

#     env.conf['site_name']
#     env.conf.site_name

#   - You can register [global] variables with:

#     env.variables['key'] = "value"

#   - You can export macros/functions [for use in Markdown files with]:

#     env.macro(func, 'name') # exported as 'name'

#     env.macro(math.floor) # exported as 'floor'

#   - OR define a macro/function and export it altogether with:

#     @env.macro
#     def foo():
#         ...
#         return str

#   - You can define filters with:

#     @env.filter
#     def bar():
#         ...
#         return str

#   - E.g:

#     @env.macro
#     def site_info():
#         "Return general info on the website (name, description and theme)"

#         info = (
#           env.conf['site_name'],
#           env.conf['site_description'],
#           env.conf['theme'].name
#         )
#         return "%s/%s (theme: %s)" % info
# """
