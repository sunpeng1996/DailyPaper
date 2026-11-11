---
title: 'ForeSpark: Joint Draft and Verification Budget Scheduling for Parallel Speculative
  Decoding'
title_zh: ForeSpark：面向并行推测解码的草稿-验证联合预算调度系统
authors:
- Jaeyong Song
- Daniel Wang
- Pratyush Patel
- Jonny Kong
- Preyas Shah
- Shobhit Kanaujia
affiliations:
- Meta
- Seoul National University
arxiv_id: '2611.13442'
url: https://arxiv.org/abs/2611.13442
pdf_url: https://arxiv.org/pdf/2611.13442
published: '2026-11-10'
collected: '2026-11-11'
category: LLM
direction: LLM推理 · 并行推测解码加速
tags:
- Speculative Decoding
- LLM Inference
- Scheduling
- Throughput Optimization
- vLLM
one_liner: 提出工作保留式推测架构，联合调度草稿与验证预算，大幅提升LLM并行推测解码吞吐量
practical_value: '- 基于vLLM部署LLM服务（如电商文案生成、用户意图理解、Agent推理）时，可直接复用ForeSpark的联合调度逻辑，相比现有DSPARK最高可提升1.77倍吞吐量，满足更高并发SLO要求

  - 上下文感知预草稿接受率预估的思路可迁移到GenRec场景，为多候选生成、草稿截断提供轻量级预估信号，减少无效的候选生成计算

  - 用凹包转换+全局排序替代组合搜索的低开销调度方法，可复用在高并发推荐/广告系统的算力配额分配场景，在微秒级延迟下完成全局最优调度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有并行推测解码系统仅优化验证阶段的预算分配，草稿阶段仍固定生成全长度块，高负载下草稿开销占单步时间的40%，其中75%的草稿计算因未被验证直接浪费；自回归草稿的动态长度控制方法不适用于并行草稿场景——并行草稿需在单次前向传播前确定块长度，且草稿与验证长度跨批次耦合，全局调度的组合复杂度高，无法适配推理步的低延迟要求。

### 方法关键点
- 上下文感知预草稿预估器：仅利用目标模型上一步的锚点上下文特征与锚点嵌入，通过轻量级单隐藏层网络预预估各候选草稿长度的token接受率，单请求仅需数次矩阵向量运算，延迟可忽略
- 轻量级联合调度器：将单请求各长度的预期收益转换为上凹包，把多请求的长度分配组合优化问题降为全局排序问题，微秒级即可完成每步的单请求草稿长度与全局验证预算的最优分配
- 后草稿预算分配：支持可变长度草稿无padding执行，草稿生成后再对token重打分，将验证预算分配给接受概率最高的token，全程不改变LLM的输出分布

### 关键结果
在ShareGPT数据集上测试Qwen3-14B、GLM5.3-Flash、GLM5.3三个不同量级的模型，对比AR解码、DFLASH2、DSPARK等基线：相同单请求生成速率下，吞吐量比SOTA DSPARK最高提升1.77倍，比AR解码最高提升2.49倍；延迟SLO约束下可承载的请求率最高为DSPARK的1.51倍，高负载下草稿时间较DSPARK最高降低76%。

### 核心结论
并行推测解码的优化不能仅局限于验证阶段，草稿与验证的联合调度可以在不改变输出分布的前提下，大幅提升高负载下的LLM推理性价比。
