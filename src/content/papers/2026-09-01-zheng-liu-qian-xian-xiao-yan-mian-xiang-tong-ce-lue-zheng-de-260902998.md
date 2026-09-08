---
title: 'Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation'
title_zh: 蒸馏前先校验：面向同策略蒸馏的Prompt级教师门控机制
authors:
- Zhiwei Zhang
- Zechen Sun
- Fei Zhao
- Kang Peng
- Bin Liang
- Huayu Deng
- Yao Hu
- Kam-Fai Wong
- Mu Chuan
affiliations:
- AllSpark Team
arxiv_id: '2609.02998'
url: https://arxiv.org/abs/2609.02998
pdf_url: https://arxiv.org/pdf/2609.02998
published: '2026-09-01'
collected: '2026-09-08'
category: Training
direction: 大模型训练 · 同策略蒸馏优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- LLM Training
- GPU Optimization
- GRPO
one_liner: 通过prompt级教师可靠性校验的同策略蒸馏框架，同时提升模型效果与集群GPU利用率
practical_value: '- 做垂类小模型蒸馏（如电商query理解、商品文案生成模型）时，可直接复用TGOPD的prompt级门控逻辑，避免大教师模型的自信错误传导给小模型，在逻辑类任务上可获得3%左右的效果提升

  - 异步蒸馏部署场景下，无需新增GPU资源，仅利用教师节点原有空闲算力生成可靠性探针，即可将教师GPU利用率从10%左右提升至70%+，集群整体利用率最高提升18个百分点

  - 无自动verifier的开放域场景（如推荐文案生成），可简化实现：门控关闭时直接丢弃对应prompt的训练信号，仍可获得90%的原有收益，大幅降低落地门槛'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统On-Policy Distillation（OPD）通过大教师模型给学生自生成样本提供逐token反向KL监督，训练效率比基于轨迹奖励的RLVR高一个量级，但存在两个核心痛点：一是异步部署下教师仅需对学生生成好的样本做前向打分，GPU平均利用率仅5%~10%，大部分时间处于闲置状态；二是未做prompt级教师可靠性校验，反向KL的模式寻优特性会放大教师的自信错误，导致学生负向迁移，而基于熵、师生似然的传统可信度指标无法直接校验输出正确性。
### 方法关键点
- 利用教师空闲算力，在学生生成rollout的同步阶段生成KT=3个教师探针样本，通过任务verifier打分得到该prompt下的教师可靠性qT(x)
- 设计硬门控机制：qT(x)≥2/3时保留原OPD逐token监督，否则切换为基于verifier的GRPO轨迹级监督，两个分支互斥不混合
- 探针计算大部分重叠在教师原有空闲窗口，几乎不增加端到端训练耗时
### 关键结果
在4B、35B两个规模学生的数学、代码、指令跟随三类任务上测试，对比Vanilla OPD、TrOPD等基线：所有6个单域场景效果均更优，代码任务提升最显著（35B规模LiveCodeBench超基线3.0，甚至超过教师模型1.3）；多域训练下7个基准平均提升1.14（4B）、0.95（35B）；教师GPU利用率从9.8%提升至78.9%，集群整体利用率最高提升18个百分点。
**最值得记住的一句话**：同策略蒸馏中仅屏蔽不可靠的教师信号就能拿到90%的收益，闲置算力复用几乎不增加额外成本
