# Spark架构总结
## RPC框架

### 关键类
|	类			|说明											|
|:--------------:|:----------------------------------------------|
| NettyRpcEnv 	| 每个进程中都有一个'NettyRpcEnv'对象来负责rpc通信。	|
| Dispatcher	| 处理远端节点发送到本进程的消息。被NettyRpcEnv组合。	|
| EndpointData | Dispatcher 的内部类，通信实体包含了实体名称、实体 Endpiont 和 EndpointRef 。|
| Outbox | 对远端节点发送的消息列表，包含了和远端通信的本地客户端。每个远端RPCAddress都会对应一个Outbox。|
| RpcEndpointRef | 远端通信实体的本地引用。|
| RpcEndpoint | RPC通信实体。|

### NettyRpcEnv
每个进程中都有一个NettyRpcEnv对象来负责rpc通信。

__主要成员__
* `server: TransportServer` 本进程的rpc通信实体。实际就是Netty的tcp服务端，server成员是在NettyRpcEnv初始化时创建的。
* `dispatcher: Dispatcher` rpc消息分发对象。负责将消息分发到不同的对的RpcEndpiont。
* `outboxes: ConcurrentHashMap[RpcAddress, Outbox]` 保存每个远端地址对应的Outbox对象。outbox中保存了一个client对象（tcp通信客户端），和一个该客户端要发的消息链表messages。
* `transportContext: TransportContext` tcp通信的消息处理对象，封装了消息编解码、Netty的消息处理handler。在NettyRpcHandler中封装了netty通信的client对象（TransporClient对象）。
* `clientConnectionExecutor` 用于创建client连接的线程池。

__主要方法__
```java
def setupEndpoint(name: string, endpoint: RpcEndpoint): RpcEndpointRef
```
* 将本地Endpoint注册到Dispathcer，返回一个对应的RpcEndpointRef。
* 调用

