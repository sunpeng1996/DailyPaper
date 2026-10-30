---
title: 'The Endgame of FSDP Communication: Layout-Aware Collectives on Copy Engines,
  RDMA, and NVSwitch'
title_zh: 面向FSDP的布局感知集合通信优化：基于拷贝引擎、RDMA与NVSwitch
authors:
- Zejian Wang
- Yifan Zhao
- Kaihui Ren
- Xiaoling Zhou
- Yubin Wang
- Chenhao Guan
- Lin Zhang
- Yufeng Li
- Zhikang Mo
- Zhuoru Ma
affiliations:
- KlingAI Research
arxiv_id: '2610.38228'
url: https://arxiv.org/abs/2610.38228
pdf_url: https://arxiv.org/pdf/2610.38228
published: '2026-10-28'
collected: '2026-10-30'
category: Training
direction: 分布式训练 · FSDP通信优化
tags:
- FSDP
- DistributedTraining
- CollectiveCommunication
- NCCL
- MoE
one_liner: 提出TIDE零拷贝集合通信方案，大幅降低FSDP大模型训练的通信与内存开销
practical_value: '- 训练生成式推荐模型、Agent垂直LLM时可直接复用TIDE优化FSDP通信，最多降低27%训练步长，MoE类稀疏推荐/Agent模型收益更高

  - 做分布式训练工程优化时，可参考其布局感知零拷贝设计，消除张量layout转换冗余拷贝，将通信任务卸载到拷贝引擎、NVSwitch，减少SM资源抢占，降低通信与计算的干扰

  - 内存紧张的训练场景（如大尺寸多模态推荐模型训练）可采用Slot-Reuse模式，复用All-Gather空闲槽位存储梯度，峰值内存最多比原生FSDP2低1.4GiB'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
FSDP2是当前大模型分布式训练的主流范式，但其参数存储的per-parameter布局和集合通信的rank-major flat buffer布局存在天然不匹配，仅layout转换开销就占Llama-3.1 70B训练步长的6.4%；同时基于SM的通信内核会抢占计算资源，最多可让并发GEMM慢69%，传统优化方案要么修改FSDP2存储契约，要么无法同时解决布局转换、SM抢占、内存开销三大痛点。

### 方法关键点
- 提出TIDE零拷贝集合通信方案，基于公开NCCL 2.31+ API实现，完全兼容FSDP2的per-parameter存储契约，无需修改模型计算内核
- TIDE-AG：通过NVSwitch组播、速率控制的递归加倍RDMA直接将All-Gather分片写入参数存储，不占用SM资源，无冗余layout拷贝
- TIDE-RS：原生支持bf16梯度直接输入、fp32归约的混合精度模式，通过拷贝引擎推送梯度、短生命周期CTA做节点局部累加、NVSwitch做跨节点归约，大幅降低SM占用
- 提供两种运行模式：In-Place模式直接读取自动微分生成的梯度，提前调度下一次All-Gather最大化计算通信重叠；Slot-Reuse模式将梯度拷贝到空闲的All-Gather槽位，及时释放梯度内存降低峰值占用

### 关键实验
在64GPU集群上测试，对比基线为Stock FSDP2、FSDP2+SymmMem，覆盖Llama-3.1 70B、Wan2.2-T2V-A14B、Qwen3-30B-A3B（MoE）三类模型：
- 步长优化：相对Stock FSDP2最多降低27.1%（MoE场景），相对FSDP2+SymmMem最多降低6.0%
- 通信SM耗时降低12.5~14.5倍，通信对并发计算的干扰最多降低一个数量级
- 内存优化：峰值内存最多比FSDP2+SymmMem低4.7GiB，Slot-Reuse模式下峰值内存低于原生FSDP2

**最值得记住的一句话**：FSDP的布局转换本质是集合通信问题而非拷贝问题，将布局放置逻辑融合到集合通信寻址中，可同时消除冗余拷贝、降低SM抢占、节省内存开销。
