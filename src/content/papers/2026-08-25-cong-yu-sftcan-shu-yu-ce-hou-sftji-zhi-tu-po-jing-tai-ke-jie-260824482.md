---
title: 'Beyond Static Interpretability: Anticipating Post-SFT Mechanisms from Pre-SFT
  Parameters for Better Tuning'
title_zh: 从预SFT参数预测后SFT机制，突破静态可解释性局限优化微调
authors:
- Hang Chen
- Jiaying Zhu
- Wenya Wang
affiliations:
- Nanyang Technological University
- The Chinese University of Hong Kong
arxiv_id: '2608.24482'
url: https://arxiv.org/abs/2608.24482
pdf_url: https://arxiv.org/pdf/2608.24482
published: '2026-08-25'
collected: '2026-08-26'
category: Training
direction: 大模型SFT优化 · 前瞻式机制定位
tags:
- SFT
- Mechanistic Interpretability
- PEFT
- LoRA
- Parameter Localization
one_liner: 仅用预SFT参数与1%训练数据预测微调后关键机制，显著提升SFT效果与模型通用性
practical_value: '- SFT阶段可借鉴轻量探针微调思路：用1%训练数据、1%原学习率跑1个epoch获得初始梯度方向，无需全量预跑即可定位关键参数，大幅降低微调前分析成本

  - 做参数高效微调时，可参考双粒度定位策略：组件级给重要的注意力、MLP层动态分配1-32的LoRA rank，平均rank保持8，比固定rank的LoRA效果更好且不增加总参数量

  - 针对电商/推荐场景的复杂垂直SFT任务（如多步推理类的商品适配、推荐理由生成），优先用前瞻式参数定位，避免静态定位选错参数导致微调效果差、通用能力掉点多

  - 多任务联合SFT时，用该方法提前定位不同任务的关键参数，规避共享冲突神经元，降低多任务干扰，适合同时做搜索、推荐、广告多场景的大模型微调'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统「定位-微调」范式依赖预SFT模型的静态可解释性定位关键参数，但预SFT模型未适配目标任务，定位结果和微调后实际生效的参数偏差大，尤其是新任务/复杂任务会误导SFT，冻结不该冻的参数、放开不重要的参数，导致任务效果差、通用能力退化，本质是可解释性的回溯属性和微调的前瞻需求存在矛盾。

### 方法关键点
- 理论上把SFT建模为连续参数演化过程，用泰勒展开把后SFT的机制定位目标和预SFT模型的动态梯度关联，无需跑完整个SFT即可估计参数重要性
- 工程上先做探针SFT：用1%训练数据、1%原学习率跑1个epoch得到微更新后的模型θ'，捕获初始梯度方向
- 双粒度定位pipeline：①神经元级：只更新前20%重要性最高的神经元，其余冻结；②组件级：给注意力头的Wq/Wk/Wv/Wo、MLP的Wup/Wgate/Wdown按重要性动态分配1-32的LoRA rank，平均rank保持8
- 用K值外推梯度距离，采样10个K值平均得到最终参数重要性排序，规避单K值偏差

### 关键结果
在Mistral-7B、Llama-2-13B、Qwen3-30B上验证，覆盖NLU、逻辑推理、数学推理三类任务，相比SOTA baseline CircuitLoRA，组件级方案的目标任务准确率（TTA）在逻辑推理、数学推理任务上分别提升2.33pct、1.4pct，通用能力准确率（PTA）分别提升2.02pct、1.82pct；任务复杂度越高（如7位算术、6步推理）优势越明显，相比静态定位、探针定位的准确率高30pct以上。

**最值得记住的一句话**：静态可解释性是「用旧地图走新路」，前瞻式机制定位才能提前找到微调真正需要的参数，兼顾目标任务效果和通用能力保留。
