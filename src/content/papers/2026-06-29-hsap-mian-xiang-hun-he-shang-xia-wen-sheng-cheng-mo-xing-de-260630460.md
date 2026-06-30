---
title: 'HSAP: A Hierachical Sequence-aware Parallelism for Hybrid-Context Generative
  Models'
title_zh: HSAP：面向混合上下文生成模型的分层序列感知并行算法
authors:
- Songxin Zhang
- Zejian Xie
- Zhuoyang Song
- Cong lin
- Junyu Lu
- Jiaxing Zhang
- Bingyi Jing
affiliations:
- Southern University of Science and Technology
- International Digital Economy Academy
arxiv_id: '2606.30460'
url: https://arxiv.org/abs/2606.30460
pdf_url: https://arxiv.org/pdf/2606.30460
published: '2026-06-29'
collected: '2026-06-30'
category: Training
direction: 大模型长序列训练 · 序列并行
tags:
- Sequence Parallelism
- Long Context
- LLM Training
- Hybrid Context
- Distributed Training
one_liner: 结合两类序列并行范式，解决混合上下文打包长序列的高效分布式训练问题
practical_value: '- 做LLM4Rec长上下文用户建模/长序列推荐训练时，可复用该分层拓扑设计：将InterSP放在跨节点InfiniBand连接组，IntraSP放在同节点NVLink连接组，优化通信效率

  - 推荐场景多长短不一序列打包训练场景下，可借鉴序列感知JIT编译思路调度P2P通信，砍掉冗余的跨序列计算与通信，提升训练吞吐

  - 需要支持超512K长度的超长序列训练时，该框架突破了IntraSP并行度不超过注意力头数的限制，可平滑扩展更大序列长度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM和多模态生成模型都向超长上下文发展，训练时激活内存压力大，需要序列维度分布式并行。业界普遍用序列打包将多个短混合上下文序列拼为长序列，减少padding的计算浪费，但现有序列并行方案存在固有缺陷：InterSP（环注意力类）不支持混合上下文打包，易产生注意力交叉污染、冗余开销大；IntraSP（DeepSpeed-Ulysses类）并行度受限于注意力头数量，无法支持更大序列长度，该矛盾尚未解决。

### 方法关键点
- 提出SAP（序列感知并行）算法：基于JIT编译思想，根据打包序列的实际注意力掩码结构，提前为每个设备rank生成定制化的P2P通信、计算指令序列，砍掉不必要的跨段传输和计算，消除通信气泡
- 提出分层HSAP框架：正交结合InterSP（跨组）和IntraSP（组内）两类序列并行，突破IntraSP并行度上限限制；同时做拓扑匹配优化，将通信密集的IntraSP all-to-all放在同节点NVLink，通信量适中的InterSP P2P放在跨节点InfiniBand，用固定全局内存buffer控制内存峰值无抖动。

### 关键实验结果
在FineWeb、Slim-Pajama预训练数据集、UltraChat SFT数据集上，对比DeepSpeed-Ulysses、DistFlashAttn、Megatron-LM等SOTA基线：32K序列长度下HSAP吞吐达到3598 token/s，对比原生打包方法提升42%，对比padding批处理提升180%；支持扩展到512K以上序列长度，同等并行度下注意力计算耗时比DistFlashAttn降低约50%，不会像Ulysses一样在大并行度下出现OOM。

最值得记住的一句话：面向混合上下文打包长序列，分层结合两类序列并行+序列感知JIT调度，可同时获得更高训练吞吐和更大可扩展序列长度。
