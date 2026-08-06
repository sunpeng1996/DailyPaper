---
title: 'When Teachers Mislead: Spurious-Signal-Aware On-Policy Distillation'
title_zh: 面向虚假信号感知的在策略蒸馏框架SA-OPD
authors:
- Yinuo Jiang
- Yongjie Ye
- Zhou Tao
- Xiang Zhuang
- Qiang Zhang
- Huajun Chen
- Tiankai Li
affiliations:
- Zhejiang University
- ByteDance
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2608.03632'
url: https://arxiv.org/abs/2608.03632
pdf_url: https://arxiv.org/pdf/2608.03632
published: '2026-08-03'
collected: '2026-08-06'
category: Training
direction: LLM/VLM 在策略蒸馏训练优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- Spurious Signal
- LLM Training
- VLM Training
one_liner: 提出结合输入接地性与优化影响过滤虚假信号的在策略蒸馏框架，效果显著优于现有基线
practical_value: '- 做Agent/生成式推荐小模型蒸馏时，可复用SA-OPD的token过滤逻辑，过滤掉教师模型依赖语言模板而非用户/商品上下文的误导信号，避免小模型学到无意义套话，提升生成内容和业务场景的贴合度

  - 蒸馏多模态商品理解模型（图文打标、视频理解等）时，可直接复用输入接地性评估方法：对比带业务输入和不带输入时的teacher-student divergence差值，快速定位虚假信号，比单纯用置信度、熵的筛选效果更好，VLM场景增益更明显

  - 训练时采用动态FLMR阈值控制过滤的损失占比，避免过度过滤有效信号，平衡训练稳定性和效果，无需人工反复调筛选比例阈值，降低工程调优成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有在策略蒸馏（OPD）通过token级教师信号对齐学生模型，解决了离线蒸馏的分布偏移问题，但现有筛选方法默认教师信号完全可靠，忽略了教师的token级判断可能受语言先验、格式惯例、刻板推理模板驱动，而非依赖当前任务输入，这类虚假信号会产生大梯度但对任务提升无帮助，甚至导致学生学到无关偏差，多模态场景下该问题尤其突出。

### 方法关键点
- 定义虚假信号为同时满足「低输入接地性」和「高优化影响」的token：输入接地性通过对比带原始输入和移除输入仅保留生成前缀时的teacher-student divergence差值衡量，差值越小说明信号越依赖模板先验；优化影响用divergence绝对值衡量，绝对值越大梯度影响越大
- 采用动态阈值过滤机制，通过控制过滤的损失质量比（FLMR）上限，自动调整筛选比例，避免过度过滤有效信号，适配不同任务和训练阶段
- 仅对保留的token计算reverse-KL损失，无额外可训练参数，仅增加少量前向计算开销

### 关键结果
在LLM数学推理、VLM视觉理解/视觉推理三个场景下测试，对比Vanilla OPD、TIP、FiRe-OPD等基线：VLM场景下视觉理解平均得分从50.5提升到54.0，视觉推理平均得分从60.4提升到63.5；LLM数学推理平均得分从28.5提升到30.4，额外开销仅2.64%~7.53%。

**最值得记住的一句话**：在策略蒸馏中，仅筛选置信度高、师生差异大的token是不够的，还要判断教师信号是否真的依赖当前任务输入，才能避免学生继承教师的无关先验偏差。
