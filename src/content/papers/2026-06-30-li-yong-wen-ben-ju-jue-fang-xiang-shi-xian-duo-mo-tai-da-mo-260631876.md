---
title: Harnessing Textual Refusal Directions for Multimodal Safety
title_zh: 利用文本拒绝方向实现多模态大模型安全防护
authors:
- Moreno D'Incà
- Massimiliano Mancini
- Nicu Sebe
affiliations:
- University of Trento
arxiv_id: '2606.31876'
url: https://arxiv.org/abs/2606.31876
pdf_url: https://arxiv.org/pdf/2606.31876
published: '2026-06-30'
collected: '2026-07-01'
category: LLM
direction: 多模态大模型安全 · 激活空间拒绝方向调控
tags:
- Multimodal LLM
- Activation Steering
- Safety Alignment
- Refusal Direction
- Inference-time Optimization
one_liner: 无需多模态安全数据，通过激活调控实现训练无关的多模态大模型安全增强
practical_value: '- 多模态内容审核/合规Agent落地时，可直接复用预训练LLM的文本拒绝方向做安全增强，无需收集标注高风险的多模态有害数据，大幅降低成本与合规风险

  - 激活中心化trick可迁移至多模态模型的输出调控场景：用无意义随机样本计算模态偏置，消除跨模态特征偏移，避免安全内容被误判为违规，适合电商商品图文/视频合规校验场景

  - 自适应干预强度+ReLU门控的设计可复用在所有推理时激活调控任务中，仅对可疑输入做干预，不损失正常内容的推理准确率，避免电商场景下正常商品/广告内容被误拦截

  - 无监督层选择方法无需下游多模态数据即可定位最优干预层，落地时无需额外调参，降低工程部署成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有多模态大模型（MLLM）的安全对齐高度依赖多模态有害训练数据，这类数据收集成本高、合规风险大，且标注过程易对标注人员造成心理伤害。纯文本大模型领域已验证可通过激活空间拒绝方向调控增强安全能力，但直接迁移至多模态场景时存在模态偏置，会大量误拒安全内容，亟需无需多模态安全数据的轻量安全方案。
### 方法关键点
1. 激活中心化：用随机彩色无意义图像计算模态专属偏置均值，对多模态输入的激活做中心化，分离安全语义特征与模态专属特征，解决跨模态误拒问题
2. ReLU门控干预：仅对与文本拒绝方向正相关的激活做增强，安全输入的干预强度为0，完全保留模型正常推理能力
3. 自适应调控强度：基于当前激活与文本安全/不安全聚类中心的距离动态计算干预强度，限制在训练数据覆盖的几何信任区域内，避免模型能力退化
4. 无监督层选择：基于纯文本验证集的方向一致性、类别可分性、安全间隔三个评分自动选择最优干预层，无需任何多模态标注数据
### 关键实验
在5款SOTA MLLM（Gemma3、Qwen3-VL等）上测试，对比AdaSteer、ECSO等训练无关基线，以及需多模态安全数据训练的SASA基线：图像安全数据集VISU上，不安全内容拒绝率最高提升67.9%，安全内容误拒率控制在10%以内；图像越狱基准HADES上，安全评分最高提升56.6%，接近需训练的SASA基线水平；视频越狱基准VideoSafetyBench上，QWEN3-VL的不安全内容拒绝率从28.8%提升至88.2%，同时绝大多数模型的通用任务效用损失小于1%。
### 核心结论
多模态大模型的安全能力已经内聚在预训练LLM backbone的文本拒绝方向中，无需额外多模态安全训练，仅通过轻量推理时激活调控就能实现跨模态安全增强
