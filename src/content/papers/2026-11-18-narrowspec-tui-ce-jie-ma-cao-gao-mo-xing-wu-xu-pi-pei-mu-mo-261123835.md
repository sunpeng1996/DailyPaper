---
title: 'NarrowSpec: Draft Hidden Width Need Not Match the Target in Speculative Decoding'
title_zh: NarrowSpec：推测解码草稿模型无需匹配目标模型隐层宽度
authors:
- Alagappan Valliappan
- Ankit More
- Dheevatsa Mudigere
- Jatin Mitra
affiliations:
- NVIDIA
arxiv_id: '2611.23835'
url: https://arxiv.org/abs/2611.23835
pdf_url: https://arxiv.org/pdf/2611.23835
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: LLM推理优化 · 低延迟生成提速
tags:
- Speculative Decoding
- LLM Inference
- Serving Optimization
- Low-Latency Generation
- Model Compression
one_liner: 缩窄推测解码草稿模型残差流宽度，以极小接受率损失换取1.06~1.44倍端到端解码提速
practical_value: '- 电商智能客服、Agent推理、生成式推荐文案/候选生成等依赖LLM低延迟生成的场景，可直接将现有DFlash/EAGLE-3等推测解码草稿模型的隐层宽度缩窄为目标模型的1/2或1/4，仅需在边界加适配层重新训练，接受率损失<5%即可获得10%~40%的解码提速

  - 对于复用目标模型LM head的草稿架构，训练时增加输出适配层，推理阶段将适配层与LM head一次性折叠为窄投影，完全不改变输出logits，无效果损失还可降低每步GEMM计算量

  - 草稿宽度选型优先匹配部署硬件：数据中心GPU（如B200/H100）优先验证1/2宽度方案，低带宽边缘GPU/端侧设备优先验证1/4宽度方案，可最大化收益

  - 该裁剪思路可迁移至生成式推荐的辅助小模型：用于预筛候选item、预生成候选文案的小模型无需匹配上游大模型的隐层宽度，缩窄后可显著降低推理开销，对效果影响极小'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于目标模型隐态的特征条件式Speculative Decoding草稿（如DFlash、EAGLE-3）均默认继承目标模型的隐层宽度，导致草稿侧计算冗余；过往优化多聚焦提升接受长度、裁剪单个组件，未对整个残支流宽度做系统性优化，存在较大的latency下降空间。

### 方法关键点
- 直接将草稿模型的整个残支流宽度设置为目标模型的1/2或1/4，仅在草稿与目标张量交互的边界增加宽度适配层，其余所有投影矩阵同步缩窄，不改动注意力头数、头维度、MLP中间维度、KV cache尺寸等其他架构参数。
- 复用目标模型词表投影的草稿（如DFlash）训练时增加输出适配层映射回目标宽度，推理阶段一次性将适配层与目标LM head折叠为窄投影，仅存在浮点级精度差异，无实际效果损失。
- 自有词表的草稿（如EAGLE-3）训练时直接将嵌入表适配层折叠为窄嵌入表，推理阶段无需额外适配计算。

### 关键结果
在SPEED-Bench 880条覆盖编码、数学、RAG、角色扮演的多场景prompt上测试，对比全宽草稿基线：
- B200 GPU batch 1、temperature 0场景下，1/2宽草稿接受率最多下降3%，端到端解码提速1.06~1.09×；1/4宽草稿接受率最多下降5.4%，提速1.06~1.12×。
- 低带宽GB10 GPU下收益更高，1/4宽草稿端到端提速最高达1.44×，接受率损失与B200场景差异小于1.8%。
- batch从1到512、上下文长度从8k到32k范围内收益稳定，无窄草稿慢于全宽草稿的情况。

特征条件式草稿模型的隐层宽度是独立于目标模型的可调参数，无需强制匹配，根据部署硬件选择合适宽度即可在极小效果损失下获得显著的推理提速。
