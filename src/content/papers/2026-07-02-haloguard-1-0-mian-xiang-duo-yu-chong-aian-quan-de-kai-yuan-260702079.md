---
title: 'HaloGuard 1.0: An Open Weights Constitutional Classifier for Multilingual
  AI Safety'
title_zh: HaloGuard 1.0：面向多语种AI安全的开源权重宪法分类器
authors:
- Navaneeth Sangameswaran
- Preetham S
- Ashmiya Lenin
affiliations:
- Astroware AI, Delaware, USA
- Karunya Institute of Technology and Sciences, Coimbatore, India
arxiv_id: '2607.02079'
url: https://arxiv.org/abs/2607.02079
pdf_url: https://arxiv.org/pdf/2607.02079
published: '2026-07-02'
collected: '2026-07-04'
category: LLM
direction: LLM安全防护 · 多语种prompt安全分类
tags:
- LLM Safety
- Constitutional Classifier
- Multilingual
- Open Weights
- Prompt Guard
one_liner: 推出开源小参数量多语种prompt安全宪法分类器，性能优于体积大30倍的现有开源防护模型
practical_value: '- 搭建电商/导购Agent、LLM服务的输入安全层时，可直接复用HaloGuard开源模型，小算力开销下实现低FPR的多语种prompt安全校验，规避违规内容生成风险

  - 做分类类任务（如合规审核、意图识别）的小模型训练时，可参考1:1配对反事实数据构造方法，固定主题和词汇仅翻转意图，有效降低边界场景误判率

  - 跨境多语种业务的分类任务可借鉴「语言为表层形式」的标注策略，均衡覆盖多语种正负样本，避免将非通用语默认为对抗信号'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM向Agent场景迁移时攻击面指数级扩大，前置prompt安全防护作为第一道防线，核心痛点是边界场景FP/FN平衡难，现有开源防护模型参数量大、部署成本高。
### 方法关键点
1. 基于宪法范式构造语料，46条安全政策+2940个子类目驱动合成数据生成；
2. 构造1:1配对反事实样本，固定主题和词汇仅翻转意图，针对性降低边界场景误判；
3. 两层无危害设计分别优化边界和基线FP，46语种均衡标注不将语言作为对抗信号。
### 关键结果
0.8B版本在7个prompt安全基准上平均F1达90.9，FPR4.3、FNR9.5，性能优于30倍大的27B基线；4B版本平均F1达92.1，FPR低至3.5，额外参数重点提升精度而非召回；剩余错误大部分为基准标注错误而非模型漏判。
