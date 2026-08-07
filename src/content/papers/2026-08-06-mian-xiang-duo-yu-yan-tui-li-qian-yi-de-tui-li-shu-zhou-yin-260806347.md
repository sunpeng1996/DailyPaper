---
title: 'RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual
  Reasoning Transfer'
title_zh: 面向多语言推理迁移的推理枢轴引导在策略自蒸馏方法RP-OPSD
authors:
- Xinye Wang
- Junxiao Liu
- Shujian Huang
affiliations:
- 南京大学计算机软件新技术国家重点实验室
arxiv_id: '2608.06347'
url: https://arxiv.org/abs/2608.06347
pdf_url: https://arxiv.org/pdf/2608.06347
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 多语言LLM推理迁移训练优化
tags:
- Self-Distillation
- Multilingual-Reasoning
- Cross-lingual-Transfer
- On-Policy-Training
- Reasoning-Pivot
one_liner: 提出推理枢轴引导的在策略自蒸馏框架，高效实现跨语言推理能力迁移
practical_value: '- 做多语言电商/广告类LLM Agent（如小语种商品问答、营销文案生成、本地化客服）时，可复用推理枢轴识别思路，通过带/不带高资源语言参考解答的同模型分布差定位推理关键token，将蒸馏算力集中在高价值位置，降低小语种模型适配成本

  - 跨语言能力迁移场景下可采用双损失路由架构：推理关键token对齐高资源语言的特权教师实现能力迁移，表层表达token对齐冻结的原语言参考模型，避免迁移时丢失目标语言地道表达，适配本地化业务要求

  - 做自蒸馏优化时，可复用两个同模型不同输入的teacher视图对比的思路，替代传统教师-学生分布差作为权重信号，避免引入校准误差，提升蒸馏效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多语言推理迁移方法存在明显短板：SFT用的翻译推理样本是off-policy的，自带翻译偏差；RL类方法仅依赖最终答案正确性奖励，信号稀疏，无法约束中间推理过程；OPSD类在策略自蒸馏方法对所有生成token分配相同权重，会稀释高价值推理信号，导致小语种推理能力迁移效率极低，亟需定向区分推理关键节点与表层文本的迁移方案。
### 方法关键点
- 核心假设：目标语言推理链由表层文本和推理枢轴组成，表层变体不影响推理结果，推理枢轴（如算子选择、子目标决策、推理转折词）的漂移会直接导致推理错误
- 推理枢轴识别：通过同一模型的两个stop-gradient的teacher视图的KL差计算特权推理敏感度得分，两个视图仅在是否提供英语参考解答上有差异，差值越大说明该token越接近推理枢轴
- 双路由训练：基于推理枢轴转移门做动态权重分配，高权重token对齐带参考解答的特权教师做推理迁移，低权重token对齐冻结的原语言参考模型做表层表达锚定，梯度仅回传给学生分布
### 关键实验
在覆盖17种语言的AfriMGSM（12个非洲小语种）、PolyMath（5个中高资源语言）两个数学推理基准上测试，对比SFT、GRPO、COPSD等7个强基线；Qwen3-1.7B上AfriMGSM平均pass@12达19.07%，较COPSD提升2.37个点，PolyMath平均DW-ACC达17.97%，较COPSD提升1.98个点；Qwen3-4B上AfriMGSM平均pass@12达26.83%，较COPSD提升5.2个点，效果跨模型、跨语言稳定。
### 核心结论
跨语言能力迁移不需要对齐全序列，仅需要将特权监督集中在会改变推理状态的枢轴位置，同时锚定表层表达即可实现高效迁移，避免不必要的分布偏移。
