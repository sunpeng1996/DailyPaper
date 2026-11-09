---
title: 'LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression
  at Test-Time'
title_zh: LowRAM：测试时可组合KV缓存压缩的低秩键与值摊销方法
authors:
- Teresa Delgado
- Hugo Hazard
- Martin Benfeghoul
- Jun Wang
- Zafeirios Fountas
affiliations:
- Huawei Noah's Ark Lab, London
- University College London, London
arxiv_id: '2611.07025'
url: https://arxiv.org/abs/2611.07025
pdf_url: https://arxiv.org/pdf/2611.07025
published: '2026-11-04'
collected: '2026-11-09'
category: LLM
direction: LLM推理优化 · KV缓存压缩
tags:
- KV cache
- compression
- LLM inference
- low-rank
- test-time adaptation
one_liner: 提出测试时可组合的KV缓存不对称压缩方案，结合值摊销与跨层低秩键压缩，兼容现有量化、驱逐策略
practical_value: '- 部署LLM驱动的电商智能导购、长用户行为序列推荐、批量文案生成等服务时，可复用LowRAM的不对称KV压缩思路，4倍压缩下性能损失不到4%，大幅提升长上下文场景的批处理吞吐量

  - 面向多轮对话类Agent场景（如用户历史订单查询、长商品说明书QA），可复用meta-learned初始化策略，将预fill阶段梯度更新从150步降到2步，首包时间仅为基线的1.3倍，几乎不影响用户体验

  - 现有LLM服务如果已经用了KV量化、驱逐策略，可直接叠加LowRAM，10K以上长上下文场景最高可实现26.9倍压缩，仅损失5.5%性能，支撑更大批次的生成任务'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
自回归解码的KV缓存内存占用随上下文长度线性增长，是长上下文LLM推理的核心瓶颈。现有压缩方法（驱逐、量化、低秩分解）均未挖掘同一注意力头内键与值的可预测性冗余，且大多无法兼容组合多种压缩策略，难以在低性能损失下实现超高压缩比。

### 方法关键点
- 不对称压缩设计：键采用跨层共享低秩基的xKV压缩方案，利用键的能量集中特性实现低误差压缩；值采用摊销方案，测试时为每个注意力头拟合轻量MLP映射键到值，仅存储预测误差最高的p比例值残差，大幅降低值缓存占用
- 预fill开销优化：用Slim Attention的键值投影伪逆初始化MLP线性分支，再通过元学习预训练初始化参数，可将每个上下文的拟合梯度更新从300步降到2步，大幅降低首包延迟
- 可组合性：兼容现有KV驱逐、量化策略，可叠加使用进一步提升压缩比；新增选择性重建机制，解码时仅重建当前query相关的KV块，降低计算开销

### 关键结果
在Mistral-7B、Llama3.1-8B、Qwen3.5-4B三个模型上测试，4×压缩下LongBench性能保留94.4%~99.6%，RULER性能保留93.9%~100.1%；叠加量化+驱逐后，10K以上长上下文场景最高实现26.9×压缩，性能保留基线的94.5%；配合选择性重建，262K长上下文下峰值解码吞吐量是基线的5倍。

最值得记住的一句话：KV缓存的键和值结构特性差异极大，针对性采用不对称压缩策略，可在极低性能损失下实现远超单一压缩方法的压缩比。
