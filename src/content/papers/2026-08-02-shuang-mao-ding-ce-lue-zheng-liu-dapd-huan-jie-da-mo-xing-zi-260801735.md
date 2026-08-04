---
title: 'DAPD: Dual-Anchored Policy Distillation'
title_zh: 双锚定策略蒸馏(DAPD)：缓解大模型自蒸馏中的特权幻觉问题
authors:
- Jianyu Wu
- Yizhou Wang
- Encheng Su
- Chen Tang
- Shixiang Tang
affiliations:
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
- University of Science and Technology of China
arxiv_id: '2608.01735'
url: https://arxiv.org/abs/2608.01735
pdf_url: https://arxiv.org/pdf/2608.01735
published: '2026-08-02'
collected: '2026-08-04'
category: Training
direction: 大模型后训练 · 策略蒸馏优化
tags:
- Policy Distillation
- Privilege Illusion
- Post-training
- On-policy Distillation
- LLM Alignment
one_liner: 提出双锚定策略蒸馏框架，从信息不对称根源解决大模型自蒸馏特权幻觉，跨规模稳定提分
practical_value: '- 优化LLM驱动的电商Agent推理、商品文案生成/理解模型时，可复用DAPD的信息匹配思路，避免训练时使用了人工标注完整推导、全量召回上下文等特权信息，导致推理时幻觉升高，无需修改推理逻辑仅调整蒸馏目标即可提效

  - 电商场景做小模型蒸馏对齐大模型效果时，可参考双源锚定设计，同时用人工标注的可靠样本和模型自生成的分布内样本做双向蒸馏，比仅依赖标注数据的蒸馏泛化性更好，还能降低标注成本

  - 可复用论文的动态权重调优逻辑：7B以下小模型加重标注参考的监督权重，大模型加重自生成rollout的监督权重，适配不同规模模型的蒸馏优化，提升训练性价比'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-policy自蒸馏（OPSD）是大模型后训练提升推理能力的主流方案，但存在特权幻觉问题：训练时教师模型可访问参考答案、工具输出等特权信息，学生模型推理时无法获取这些信息，却会生成依赖特权信息的错误断言，导致效果下降。现有方案要么直接使用特权信息、要么过滤教师信号，均未解决根源的信息不对称问题，且仅依赖参考作为唯一监督源，浪费了模型自生成rollout中的有效推理信号。

### 方法关键点
- 双路径锚定（DPA）：引入自条件分布作为可训练桥接，构造两条对齐路径：无特权路径对齐无特权信息下的参考与rollout行为，特权路径对齐有特权信息下的两者行为，从根源消除信息不对称
- 双源锚定（DSA）：同时做参考引导rollout、rollout引导参考的双向蒸馏，平衡参考的正确性和rollout的学生可达性，避免单源监督偏差
- 仅修改训练损失，无推理额外开销

### 关键实验
在Qwen3全系列模型（1.7B~32B）上验证，覆盖推理、编码、指令跟随6类基准，对比OPSD、PurifiedOPSD等主流基线：Qwen3-4B上平均比OPSD高2.00分，错误断言降低73%；跨规模增益稳定，4B提升2.69分，32B提升2.78分，解决了OPSD在大模型上增益消失的问题；仅用推理数据训练的模型，分布外编码任务上比OPSD高1.37分。

最值得记住的一句话：解决蒸馏幻觉的核心不是过滤特权信号，而是从训练目标层面匹配教师和学生的信息可得性，同时用好参考和自生成样本的互补价值
