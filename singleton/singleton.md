#### 单例模式

本节介绍了关于单例模式的各种形式，当要求一个类只有一个对象时，就可以使用单例模式，单例是一种经过时间考验的成熟方法，能够在不带来太多缺陷的情况下提供全局访问点

#### 应用

在许多实际应用程序汇总，我们只需要创建一个对象，如线程池、缓存、对话框、注册表设置等，如果我们为每个应用程序创建多个实例，则会导致资源的过度使用，单例模式在这种情况下工作的很好

#### 缺点

* 当使用全局变量或类的实例化非常耗费资源但是最终却没有用到它的情况下，单例的影响可以忽略不计
* 全局变量可能在某处已经被误改，但是开发人员仍然认为他们没有发生变化，而该变量还在应用程序的其他位置被使用
* 可能会对同一个对象创建多个引用，由于单例模式只创建一个对象，因此这种情况下会对同一个对象创建多个引用
* 所有依赖于全局变量的类都会由于一个类的改变而紧密耦合为全局数据，从而可能在无意中影响另一个类