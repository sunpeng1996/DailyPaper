---
title: 'Why Knowing Both Hops Is Not Enough: Understanding Two-Hop Generalization
  in Language Models'
title_zh: 大语言模型两跳推理泛化失败的机制解析与优化方法
authors:
- Zili Zhang
- Yilin Wang
- Heng Wang
- Herun Wan
- Minnan Luo
affiliations:
- Xi'an Jiaotong University
- University of Illinois Urbana-Champaign
arxiv_id: '2608.07261'
url: https://arxiv.org/abs/2608.07261
pdf_url: https://arxiv.org/pdf/2608.07261
published: '2026-08-07'
collected: '2026-08-10'
category: Reasoning
direction: 大模型推理 · 两跳泛化机制优化
tags:
- Multi-hop Reasoning
- OOD Generalization
- Mechanistic Interpretability
- Looped Transformer
- Representation Alignment
one_liner: 揭示大模型两跳推理非对称泛化机制，提出循环架构大幅提升OOD推理准确率
practical_value: '- 电商导购Agent/商品知识库问答场景：可借鉴循环架构设计，对齐中间实体表示与底层输入格式，无需额外标注两跳训练样本，即可提升OOD多跳查询（如“敏感肌适用的平价防晒替代”）的回答准确率

  - 多跳推理任务的效果验证：可通过logit lens快速定位实体表示的关键过渡层，用实体表示一致性校验代替全链路人工评估，降低导购、搜索等场景的多跳效果验证成本

  - 垂直领域LLM推理能力微调：无需盲目扩充训练数据，可先通过线性探测检查上层网络是否学会基于中间表示推理，针对性微调上层网络即可降低训练成本、提升推理泛化性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM虽能完成复杂多跳任务，但普遍存在已知两个独立单跳事实、却无法组合推理出两跳结果的异常失败，现有研究对该现象的内部机制解释不足，且OOD场景下两跳泛化能力几乎为0，严重制约了导购Agent、商品知识问答、多条件搜索等落地场景的可靠性。

### 方法关键点
- 构造受控符号实验环境，将原子事实划分为ID/OOD子集，组合出II/IO/OI/OO四类两跳样本，排除预训练数据的混杂干扰
- 用logit lens定位两跳推理的关键过渡层，通过因果补丁实验验证：同实体跨上下文表示的一致性与两跳泛化能力正相关
- 揭示失败根因：上层网络在单跳训练阶段仅学会实体表示到输出的线性映射，未掌握基于中间表示的推理能力，存在训练-推理 mismatch
- 提出两种优化方案：针对性微调上层网络的表示推理能力；采用上下层参数共享的循环架构，对齐中间表示与底层输入格式，复用推理回路

### 关键结果
在符号数据集与维基百科真实两跳数据集上测试：标准训练下IO/OO类OOD两跳样本准确率接近0；采用循环架构后，GPT backbone符号任务IO准确率达0.97、OO达0.84，真实自然语言数据集IO准确率0.79、OO达0.66。

> 最值得记住的结论：两跳推理的OOD失败并非模型缺乏对应知识，而是上层网络的功能与推理需求不匹配，对齐跨层表示格式即可低成本提升泛化能力
