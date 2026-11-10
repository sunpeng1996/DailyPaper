---
title: 'Double Blind Evals: Resolving the Dual Confidentiality Dilemma in AI Safety
  Auditing'
title_zh: 双盲评估：解决AI安全审计中的双向保密困境
authors:
- Andrew Trask
- Sol Messing
- Vai Pahwa
- Pegah Maham
- Rene Kolga
- Austin Frantz
- Andrew Tash
- Kate Thomas
- Sean McGregor
- George Balston
affiliations:
- A VERI
- Google
- Singapore AISI
- OpenMined
- MLCommons
arxiv_id: '2611.12604'
url: https://arxiv.org/abs/2611.12604
pdf_url: https://arxiv.org/pdf/2611.12604
published: '2026-11-09'
collected: '2026-11-10'
category: Eval
direction: AI安全评估 · 双向保密机制
tags:
- AI Safety
- Secure Enclave
- Double Blind Evaluation
- Model Auditing
- Privacy Preserving
one_liner: 基于硬件安全enclave实现AI安全审计场景下评估集与模型权重的双向保密互盲评估
practical_value: '- 跨部门/跨公司模型效果评估场景可复用该方案：乙方提供的推荐/Agent大模型在甲方安全enclave内完成推理，无需暴露模型权重，甲方无需泄露内部标注测试集，解决双方信任问题

  - 大模型供应商对外提供效果验证服务时，可直接复用H100 enclave + PySyft的落地方案，无需向客户暴露模型权重，同时保障客户测试prompt不被泄露，降低商务对接成本

  - 涉及敏感用户数据的推荐/广告模型合规审计场景，可采用该方案满足监管要求，审计方无需获取用户隐私数据、厂商无需暴露模型细节即可完成合规校验'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
AI安全评估存在双向保密冲突：评估方需保密测试prompt避免基准泄露或被模型方针对性拟合，延长基准使用寿命；模型方需保密权重/推理代码避免IP泄露，传统合同、零日志策略无法从技术层面解决该信任问题。
### 方法关键点
基于NVIDIA H100的硬件级安全enclave（运行时内存硬件加密），搭配OpenMined PySyft隐私计算框架，实现双盲评估的密码学保障：评估方测试prompt全程不向模型方泄露，模型权重/推理代码全程不向评估方泄露。
### 关键结果
完成全球首次该类方案落地试点，在GCP环境下使用私有AILuminate基准集评估Google DeepMind的Gemini 2.5 Flash Lite专有模型，实现了前沿大模型与闭源基准的双向保密互盲验证。
