---
title: Learning Robust Personalized Prompts for LLM-Driven Sequential Recommendation
title_zh: 面向大语言模型驱动序列推荐的鲁棒个性化提示学习框架
authors:
- Xiaolin Zheng
- Qiyong Zhong
- Jiajie Su
- Xiang Chen
affiliations:
- Zhejiang University
arxiv_id: '2610.03923'
url: https://arxiv.org/abs/2610.03923
pdf_url: https://arxiv.org/pdf/2610.03923
published: '2026-10-02'
collected: '2026-10-06'
category: GenRec
direction: 生成式推荐 · 个性化提示学习
tags:
- Sequential Recommendation
- Prompt Learning
- LLM4Rec
- Personalization
- Semantic Drift
one_liner: 提出LRPRec框架，解决LLM驱动序列推荐的提示敏感、个性化不足与语义漂移问题
practical_value: '- 可复用连续提示优化范式：先通过LoRA对LLM做推荐域适配，冻住全量权重后仅优化提示向量，提示采用离散模板初始化+hinge式语义漂移约束的方案，可直接解决生成式推荐的提示敏感问题，减少手工调提示成本

  - 轻量化个性化注入trick：无需为每个用户维护独立软提示，仅用冻住的LLM编码用户行为序列得到偏好embedding，加性注入共享提示即可实现指令级个性化，参数开销极低，适配电商级大规模用户场景

  - 生成式推荐评估优化：可采用VHR@1（Valid HitRatio@1）作为线上核心评估指标，同时衡量生成有效性和推荐准确率，避免LLM输出无效内容导致的性能虚高，更贴合业务实际部署要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM驱动的序列推荐将下一代物品预测转为prompt条件下的自回归生成任务，但现有方案对提示写法高度敏感，语义等价的提示仅改动少量措辞就会导致性能大幅波动，手工调参成本极高。现有连续提示学习方法直接应用于推荐场景存在两大痛点：一是仅学习全局共享的任务级提示，缺乏用户级个性化适配；二是优化过程中容易出现语义漂移，提示向量脱离LLM可理解的语义空间，生成质量下降，注入个性化信号会进一步放大漂移风险。

### 方法关键点
- 提示拆分：将输入拆分为共享可学习的背景/任务提示向量、实例相关的序列化行为序列/候选集两部分，共享提示采用成熟离散模板的token embedding作为初始化锚点
- 个性化注入机制：用冻住的LLM编码用户行为序列得到偏好embedding，经线性投影后直接加性注入共享提示向量，实现用户级指令适配，仅新增极少量参数
- 语义漂移约束：采用hinge正则限制共享提示向量与初始化锚点的L2距离不超过阈值，保证提示始终处于LLM有效语义空间内
- 两阶段训练：先通过LoRA微调LLM适配推荐域，再冻住全部LLM权重，仅优化共享提示与投影层参数，避免梯度干扰

### 关键结果
在MovieLens、Steam、LastFM三个基准数据集上对比20+基线，LRPRec的VHR@1分别达到0.4947、0.5412、0.5016，相对最优基线提升7%~11%，且ValidRatio达到100%，完全消除无效生成。

### 核心结论
LLM驱动推荐的连续提示优化需平衡个性化表达与语义稳定性，仅约束共享提示组件、个性化部分采用加性注入的设计可实现两者完全解耦。
