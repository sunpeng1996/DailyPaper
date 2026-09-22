---
title: LoRA-generating hypernetworks for efficient on-device LLM generative personalization
title_zh: 面向端侧LLM生成式个性化的LoRA生成超网络
authors:
- Sean Augenstein
- Li Ding
- Jihwan Lee
- Keith Rush
- Andrey Zhmoginov
affiliations:
- Google
arxiv_id: '2609.24979'
url: https://arxiv.org/abs/2609.24979
pdf_url: https://arxiv.org/pdf/2609.24979
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: 端侧LLM · LoRA个性化生成
tags:
- LoRA
- Hypernetwork
- On-Device LLM
- Personalization
- PEFT
one_liner: 提出仅需端侧前向传播即可生成用户个性化LoRA的超网络，适配端侧资源约束，效果优于ICL与PEFT
practical_value: '- 端侧电商个性化场景（如个性化商品文案生成、用户专属购物助手）可直接复用该架构：无需端侧梯度计算，仅输入用户历史交互/会话文本前向生成个性化LoRA，彻底避免ICL挤占上下文窗口、抬升推理延迟的问题

  - 训练阶段可复用已对齐的ICL效果做蒸馏，不需要从零对齐超网络生成LoRA的质量，能大幅降低超网络的训练成本与收敛周期

  - 建议做个性化分层：用户长期兴趣/写作风格适配采用该超网络生成持久化LoRA，实时查询级个性化搭配RAG/ICL，既最大化效果又最小化端侧资源消耗

  - 小参数LLM个性化场景优先选用该方案：实测在1B/2B量级模型上ROUGE得分较ICL/PEFT高1-2分，覆盖70%以上用户的效果提升，适配端侧、边缘设备部署需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
端侧小参数LLM受硬件算力、内存限制，通用能力天然弱于云端大模型，但端侧设备绑定单一用户，存在大量可复用的长期行为、语言风格、兴趣特征，是提升效果的核心抓手。现有LLM个性化方案存在明显短板：ICL会增加输入上下文长度，不仅抬升推理延迟，还会出现上下文质量衰减；PEFT需要梯度计算，对端侧资源消耗过高无法落地，亟需兼顾效果、延迟、计算成本的端侧个性化方案。
## 方法关键点
- 超网络架构最大化复用端侧已有资产：冻结端侧已部署的Base LLM，新增轻量Embedder LoRA将用户历史上下文编码为用户特征向量；再经过带瓶颈层的2层MLP组，输出适配Base LLM各注意力层的个性化LoRA参数，新增参数量仅为Base LLM的1%-3%
- 训练分两阶段：先通过LLM2Vec式对比学习预训练Embedder LoRA，学习区分不同用户的语言特征；再端到端训练，输入用户的两批无重叠样本，一批用于生成LoRA，另一批用于计算交叉熵损失优化超网络参数，同时引入ICL作为教师模型做知识蒸馏，进一步提升生成LoRA的质量
- 端侧流程极致轻量化：用户侧仅需执行一次超网络前向传播生成LoRA，即可卸载超网络参数，后续推理直接挂载LoRA，无额外推理延迟
## 关键实验
在LongLaMP-3（亚马逊评论生成）、LongLaMP-4（Reddit帖子生成）、LaMP-5（学术标题生成）3个公开个性化生成数据集上，对比无个性化基线、ICL、PEFT三个方案，在Gemma 1B/2B两个端侧级小模型上测试：超网络生成的LoRA在所有场景下ROUGE-1得分最高，较无个性化基线最高提升1.73分，覆盖70%-87%的用户效果提升，推理延迟与PEFT持平，端侧个性化计算成本仅为PEFT的1/10以下。
## 核心结论
端侧长期个性化的核心设计思路是尽可能把计算成本上移到云端训练阶段，端侧仅保留最轻量的前向生成逻辑，实现效果与资源约束的最优平衡
