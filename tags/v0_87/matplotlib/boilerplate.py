# wrap the plot commands defined in axes.  The code generated by this
# file is pasted into pylab.py.  We did try to do this the smart way,
# with callable functions and new.function, but could never get the
# docstrings right for python2.2.  See
# http://groups-beta.google.com/group/comp.lang.python/messages/1b14640f3a4ad3dc,b3d7453af21e5f82,17739e70ac6f710c,9d5291fce29cbbb1,c5b578e4ffc6af28,056ff270daa2f414?thread_id=dcd63ec13096a0f6&mode=thread



# note we check for __doc__ is not None since py2exe optimize removes
# the docstrings

_fmtplot = """\
# This function was autogenerated by boilerplate.py.  Do not edit as
# changes will be lost
def %(func)s(*args, **kwargs):
    # allow callers to override the hold state by passing hold=True|False
    b = ishold()
    h = popd(kwargs, 'hold', None)
    if h is not None:
        hold(h)
    try:
        ret =  gca().%(func)s(*args, **kwargs)
        draw_if_interactive()
    except:
        hold(b)
        raise
    %(mappable)s
    hold(b)
    return ret
if Axes.%(func)s.__doc__ is not None:
    %(func)s.__doc__ = _shift_string(Axes.%(func)s.__doc__) + \"\"\"
Addition kwargs: hold = [True|False] overrides default hold state\"\"\"
"""

_fmtmisc = """\
# This function was autogenerated by boilerplate.py.  Do not edit as
# changes will be lost
def %(func)s(*args, **kwargs):

    ret =  gca().%(func)s(*args, **kwargs)
    draw_if_interactive()
    return ret
if Axes.%(func)s.__doc__ is not None:
    %(func)s.__doc__ = _shift_string(Axes.%(func)s.__doc__)
"""

# these methods are all simple wrappers of Axes methods by the same
# name.
_plotcommands = (
    'axhline',
    'axhspan',
    'axvline',
    'axvspan',
    'bar',
    'barh',
    'boxplot',
    'cohere',
    'clabel',
    'contour',
    'contourf',
    'csd',
    'errorbar',
    'fill',
    'hist',
    'hlines',
    'imshow',
    'loglog',
    'pcolor',
    'pcolormesh',
    'pcolor_classic',
    'pie',
    'plot',
    'plot_date',
    'psd',
    'scatter',
    'scatter_classic',
    'semilogx',
    'semilogy',
    'specgram',
    'spy',
    'spy2',
    'stem',
    'vlines',
    'quiver',
    )

_misccommands = (
    'cla',
    'grid',
    'legend',
    'table',
    'text',
    )

cmappable = {
    #'clabel' : 'if ret.mappable is not None: gci._current = ret.mappable',
    'contour' : 'if ret._A is not None: gci._current = ret',
    'contourf': 'if ret._A is not None: gci._current = ret',
    'scatter' : 'gci._current = ret',
    'pcolor'  : 'gci._current = ret',
    'imshow'  : 'gci._current = ret',
    'spy2'  : 'gci._current = ret',
    'specgram'  : 'gci._current = ret[-1]',

}


for func in _plotcommands:
    if cmappable.has_key(func):
        mappable = cmappable[func]
    else:
        mappable = ''
    print _fmtplot%locals()


for func in _misccommands:
    print _fmtmisc%locals()



# define the colormap functions
_fmtcmap = """\
# This function was autogenerated by boilerplate.py.  Do not edit as
# changes will be lost
def %(name)s():
    'set the default colormap to %(name)s and apply to current image if any.  See help(colormaps) for more information'
    rc('image', cmap='%(name)s')
    im = gci()


    if im is not None:
        im.set_cmap(cm.%(name)s)
    draw_if_interactive()

"""

cmaps = (
    'autumn',
    'bone',
    'cool',
    'copper',
    'flag',
    'gray' ,
    'hot',
    'hsv',
    'jet' ,
    'pink',
    'prism',
    'spring',
    'summer',
    'winter',
)
# add all the colormaps (autumn, hsv, ....)
for name in cmaps:
    print _fmtcmap%locals()
