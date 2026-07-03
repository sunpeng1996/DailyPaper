---
title: 'Denser neq Better: Limits of On-Policy Self-Distillation for Continual Post-Training'
title_zh: 越密越好？面向持续后训练的同策略自蒸馏局限性研究
authors:
- Meng Wang
- Haohan Zhao
- Wenzhuo Liu
- Lu Yang
- Geng Liu
- Haiyang Guo
- Guo-Sen Xie
- Gaofeng Meng
- Hongbin Liu
- Fei Zhu
affiliations:
- 中科院香港人工智能与机器人研究中心
- 中科院自动化所
- 中国科学院大学
- 南京理工大学
arxiv_id: '2607.01763'
url: https://arxiv.org/abs/2607.01763
pdf_url: https://arxiv.org/pdf/2607.01763
published: '2026-07-01'
collected: '2026-07-03'
category: Training
direction: 大模型持续后训练 · 自蒸馏与RL对比
tags:
- Continual Learning
- Self-Distillation
- SDPO
- GRPO
- LLM Post-Training
one_liner: 揭示同策略自蒸馏SDPO的适用边界，证明其持续后训练遗忘风险远高于GRPO
practical_value: '- 若用自蒸馏做垂域LLM（如客服Agent、商品文案生成）持续迭代，不要盲目追求密集token级监督，优先用定期重启冻结的teacher策略替代EMA平滑，可避免artifact放大和性能崩溃

  - 做LLM多域持续训练需兼顾新旧能力时，优先选GRPO这类序列级奖励优化方法，遗忘率比SDPO低30%以上，SDPO仅适合单域快速专精场景

  - 给Agent蒸馏CoT推理能力时，仅对短结构化任务（如工具调用、下单链路引导）做CoT蒸馏，长推理任务（如复杂需求商品搭配）蒸馏CoT反而会降低准确率

  - 业务模型迭代稳定性评估时，重点监控与训练域中等距离的任务性能，这类任务最易受参数漂移影响下跌，不要只测近域和远域任务'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前业界普遍认为同策略数据能缓解持续训练的灾难性遗忘，同策略自蒸馏（如SDPO）因无需外部奖励模型、样本效率高被广泛看好，但过往研究混淆了同策略数据来源和更新目标两个核心变量，自蒸馏的密集token级监督是否真的能在持续训练中保留旧能力尚无明确结论。

### 方法关键点
- 拆分同策略训练的两个核心变量：采样数据来源、更新目标函数，对比SDPO（密集token级自蒸馏）、GRPO（序列级相对奖励优化）两类方法在单域专精、多域持续训练中的表现
- 提出StableSDPO优化策略：采用定期重启冻结的teacher替代连续EMA更新，平衡teacher的新鲜度和稳定性，解决SDPO训练不稳定问题
- 从参数漂移（谱偏移、子空间旋转）、响应漂移、理论KL散度三层分析两类方法的遗忘机制

### 关键结果
- 数据集覆盖数学、科学、工具调用、代码4个训练域，搭配AIME、GPQA、BFCLv4等10个内/外域测试集，对比基线包含基础模型、GRPO、不同EMA率的SDPO、带CoT蒸馏的SDPO
- 单域训练时SDPO最高可提升目标域性能72%，但持续训练4个域后SDPO的旧域性能平均下跌70%，甚至完全崩溃，而GRPO所有域性能均较基线提升10%+，遗忘率仅为SDPO的1/5
- StableSDPO相比EMA更新的SDPO平均性能提升6.5个百分点

**最值得记住的一句话**：同策略数据本身不抗遗忘，只有当更新目标是KL最小的成功策略时才能保留旧能力，密集自蒸馏不是持续后训练的默认稳定方案。
