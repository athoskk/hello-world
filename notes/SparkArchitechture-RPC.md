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
* `dispatcher: Dispatcher` rpc消息分发对象。负责将消息分发到不同的对的RpcEndpiont。处理请求消息的分发对象。
* `outboxes: ConcurrentHashMap[RpcAddress, Outbox]` 保存每个远端地址对应的Outbox对象。outbox中保存了一个client对象（tcp通信客户端），和一个该客户端要发的消息链表messages。
* `transportContext: TransportContext` tcp通信的消息处理对象，封装了消息编解码、Netty的消息处理handler。在NettyRpcHandler中封装了netty通信的client对象（TransporClient对象）。
* `clientConnectionExecutor` 用于创建client连接的线程池。

__主要方法__
```java
def setupEndpoint(name: string, endpoint: RpcEndpoint): RpcEndpointRef
```
* 将本地Endpoint注册到Dispathcer，返回一个对应的RpcEndpointRef。
* 调用dispatcher.registerRpcEndpoint。endpoint: RpcEndpoint用于处理消息，包含了通信实体的url／ip／port等信息。每个通信实体在初始化过程中都会调用该接口将自己注册到dospatcher中以便接收其他通信实体的消息。

```
def asyncSetupEndpointRefByURI(uri: String): Future[RpcEndpointRef]
```
* 获取对端通信实体的引用，以便与该通信实体进行通信。uri: String 中包含该引用对应的远端实体的ip, prot。
* 该方法会被RpcRnv.setupEndpointRef 方法调用，会创建一个NettyRpcEndpointRef对象。
* 该方法中会使用endpiont-verifer 实体给远端实体发送CheckExistence消息，检查url对应的远端是否已经启动。对端收到这个消息后，远端的RpcEndpointVerifer对象处理该消息，然后调用dispatcher.verif 方法检查通信实体是否已经注册。

```
def send(message: RequestMessage): Unit
```
* 发送消息给对端实体，一般被NettyRpcEndpointRef 的 send 方法调用，RequestMessage 中包含发送方的地址、接受方的RPCEndpointRef（包含对端地址相关信息、用于通信的本地client: TransportClient）

### Dispatcher
处理远端节点发送到本进程的消息。被NettyRpcRnv组合。

**主要成员**

```
private val threadpool: ThreadPoolExecutor
```
* 处理接受Rpc 请求的线程池(dispather-event-loop)。运行MessageLoop 对象对receives 中的每个Endpoint 对象进行遍历。
* 针对每个Endpoint 再遍历inbox 来处理消息。

```
private val receiver = new LinkedBlockingQueue[EndpointData]
```
* 保存收到消息的本地EndpointData ，通过dispacher.registerRpcEndpoint 方法将本地Endpoint 保存到里面。相当于Dispathcer的消息队列。
* EndpointData 中的inbox：Inbox保存发送到通信实体的消息。

```
private val endponts = new ConcurrentHashMap[String, EndpointData]
```
* 保存本地EndpointData，EndpointData 中包含了通信实体的RPCEndpoint、RpcEndpointRef以及接收消息队列Inbox。通过dispatcher.registerRpcEndpont方法将本地Endpoint保存到里面。
