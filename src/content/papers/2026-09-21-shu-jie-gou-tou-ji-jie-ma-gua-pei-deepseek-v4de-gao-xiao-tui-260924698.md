---
title: Adapting Tree-Structured Speculative Decoding to DeepSeek-V4 for Efficient
  Inference
title_zh: 树结构投机解码适配DeepSeek-V4的高效推理实现
authors:
- Changxu Liu
- Zhaogeng Li
affiliations:
- Baidu Inc.
- Fudan University
arxiv_id: '2609.24698'
url: https://arxiv.org/abs/2609.24698
pdf_url: https://arxiv.org/pdf/2609.24698
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: LLM推理优化 · 树结构投机解码适配
tags:
- speculative decoding
- tree-structured speculation
- DeepSeek-V4
- inference optimization
- compressed attention
one_liner: 针对DeepSeek-V4压缩注意力特性优化树结构投机解码，最高提升推理吞吐量18.5%
practical_value: '- 电商/Agent场景使用DeepSeek系列大模型做推理服务时，可直接复用该适配方案，在小批量开放域对话、个性化文案生成等低可预测性场景可获得10%+的吞吐量提升

  - 临时状态隔离的工程设计可直接迁移到所有带上下文压缩的LLM投机解码适配：用scratch pad暂存分支压缩状态，仅提交接受路径的状态到持久缓存，避免跨分支状态串扰

  - 调参可直接复用实验结论：验证预算D选6~7即可，超过后吞吐量不再提升反而浪费算力；小批量（bs=4左右）、低可预测生成任务优先开启树结构解码收益最高

  - 该方案与DSpark等draft端投机优化正交可叠加，无需改动现有draft侧逻辑，仅优化verify侧即可获得双重收益'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
自回归解码是LLM推理延迟的核心来源，树结构投机解码相比线性投机可覆盖更多候选分支提升单轮接受token数，但DeepSeek-V4的CSA/HCA在线压缩注意力机制会导致共享前缀的不同分支压缩后状态不一致，无法直接兼容树结构解码，现有方案未解决该适配问题。
### 方法关键点
- 设计三阶段投机前向流程：draft extend生成候选树、draft decode基于树拓扑计算表征、target verify执行分支感知的因果验证
- 引入临时scratch pad隔离各分支的压缩状态，仅将接受路径的状态提交到持久缓存，从根源解决跨分支状态串扰问题
- 配套性能优化：减少不必要的持久缓存读写、不同压缩粒度（C4/C128）采用差异化刷新策略、端侧处理元数据降低主机控制开销
- 全流程集成到SGLang推理栈，兼容CUDA Graph等现有推理优化路径
### 关键实验结果
对比同验证预算下的线性投机解码基线，在GSM8K、MBPP、ShareGPT三个数据集，验证预算D=5~8、batch size 1~64的范围内：
1. 树解码接受长度全场景优于基线，D=8时相对提升达18.6%；
2. 吞吐量最高提升18.5%，D≥6时平均提升9%~10%，仅D=5小部分场景收益接近0；
3. D超过6后接受长度持续提升但吞吐量进入平台期，二者完全解耦。
### 核心结论
树结构投机解码与draft端优化（如DSpark）正交可叠加，其净收益=多分支带来的接受率提升 - 跨分支状态差异带来的验证开销，适配带压缩注意力的大模型时核心要解决状态一致性问题
