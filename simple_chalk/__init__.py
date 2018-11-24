import simple_chalk.src.utils as _
from .src.makeAChalkInstance import makeAChalkInstance as newChalk

chalk = newChalk()

__all__ = ["chalk", "newChalk"]


def doesntStartWith(prefix):
    return _.not_(_.startsWith(prefix))


chalkClass = type(chalk)


def setGlobal(attrName):
    globals()[attrName] = getattr(chalk, attrName)
    __all__.append(attrName)


_.passThrough(
    chalk,
    [
        type,
        vars,
        _.invokeAttr("keys"),
        list,
        _.keepWhen(doesntStartWith("_")),
        _.forEach(setGlobal),
    ],
)
