---
title: Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation
title_zh: 面向大语言模型不确定性估计的贝叶斯稀疏低秩适配方法
authors:
- Jijie Zhang
- Zhe Ren
- Quan Zhang
- Dandan Guo
affiliations:
- 吉林大学
- 密歇根州立大学
arxiv_id: '2607.02182'
url: https://arxiv.org/abs/2607.02182
pdf_url: https://arxiv.org/pdf/2607.02182
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: 大模型微调 · LoRA 不确定性校准
tags:
- LoRA
- Uncertainty Estimation
- Bayesian Learning
- PEFT
- Calibration
one_liner: 在LoRA秩维度引入可学习随机掩码，实现低开销LLM不确定性校准且不损失推理精度
practical_value: '- 电商/推荐场景用LoRA微调领域LLM（如文案生成、Query理解）时，可复用DALorRA的秩掩码设计，仅增加520个参数即可缓解过拟合与过自信问题，无需修改原有LoRA逻辑

  - 需做LLM输出置信度校准的场景（如Agent工具调用决策、推荐理由可信度打分），DALorRA训练速度比传统贝叶斯LoRA快30%+，参数开销可忽略，适合上线落地

  - 小样本垂直领域微调任务可直接复用其变分贝叶斯秩剪枝逻辑，无需手动调优LoRA rank超参，自动适配任务所需最优低秩容量'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM做任务适配微调时普遍存在过自信问题，错误预测也常输出高置信度，严重阻碍可信部署；传统贝叶斯LoRA方案多对LoRA的A/B权重做概率建模，额外参数多、计算开销大，且固定rank的设计易引入冗余容量，加剧小样本场景过拟合，亟需轻量的校准方案。
### 方法关键点
- 提出DALorRA，在LoRA的A、B矩阵间插入可学习对角随机掩码D，权重更新改为ΔW=BDA，每个掩码元素对应一个秩分量的激活概率
- 对掩码元素的伯努利分布做变分推断，用Gumbel-Sigmoid重参数化实现端到端训练，损失为负证据下界，包含预期对数似然和掩码分布与先验的KL散度两项
- 推理时采样10个掩码做模型平均，等效于低成本多模型集成，兼顾校准效果与效率
### 关键结果
基于Llama3.1-8B、Llama2-7B在10个常识推理、OOD迁移任务上对比8种基线：
- 校准效果（ECE）平均优于基线15%+，OBQA数据集上ECE低至1.82%，比标准LoRA低79%
- 训练速度比标准LoRA快30%~40%，仅新增520个参数，远低于BLoB的200万+、C-LoRA的57万+额外参数
- OOD迁移场景下（OBQA迁移到化学/物理题）准确率最高领先基线8.3%，同时保持ECE最低

**核心洞见**：LoRA校准无需对权重做复杂概率建模，仅在秩维度做动态剪枝和集成，就能以可忽略的开销同时实现精度、校准效果、效率的三重收益
