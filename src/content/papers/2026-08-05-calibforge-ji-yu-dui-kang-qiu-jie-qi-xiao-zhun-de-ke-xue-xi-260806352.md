---
title: 'CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal
  Tasks'
title_zh: CalibForge：基于对抗求解器校准的可学习终端任务规模化生成
authors:
- Fanzhe Meng
- Guoxin Chen
- Jiale Zhao
- Shuang Sun
- Zhiyu Lin
- Wayne Xin Zhao
- Ruihua Song
- Ji-Rong Wen
- Kai Jia
affiliations:
- Renmin University of China
- Independent Researcher
- AweAI Team
arxiv_id: '2608.06352'
url: https://arxiv.org/abs/2608.06352
pdf_url: https://arxiv.org/pdf/2608.06352
published: '2026-08-05'
collected: '2026-08-07'
category: Agent
direction: Agent训练数据 · 难度校准
tags:
- Agent Training
- Task Synthesis
- Adversarial Calibration
- Terminal Agent
- SFT Data Construction
one_liner: 提出多求解器/对比式校准策略生成适配难度的终端任务，显著提升Agent跨基准性能
practical_value: '- 训练业务Agent（如电商导购、广告投放、客服Agent）时，可复用对比校准策略：用业务强弱基线模型筛选训练样本，保留强模型可解、弱模型不可解的样本，大幅提升SFT效率，避免无效数据

  - 构造交互式模拟任务（如推荐系统用户行为模拟、电商运营场景化任务）时，可使用多求解器分歧作为样本保留标准，优先保留不同能力模型结果有差异的样本，提升训练数据泛化性

  - 业务bad case优化可复用反馈驱动修订思路：不要直接丢弃不符合要求的任务/case，而是根据模型失败轨迹调整任务描述、验证规则，让任务难度适配当前模型能力区间，减少无效标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有终端Agent训练任务仅验证可执行性，无法精准控制难度，过易的任务无法带来能力提升，过难的任务完全无法求解，导致训练数据利用率低、模型泛化性差，亟需自动化生成适配目标模型能力区间的高质量训练任务的方案。
### 方法关键点
- 构建对抗式作者-求解器循环：任务生成Agent先完成线索调研、任务编写、结构化校验、自验证，再基于多个求解器的执行结果迭代修订任务，直到落在可学习区
- 两种校准策略：多求解器校准要求异构求解器池出现至少1个通过、至少1个失败的结果分歧；对比式校准要求指定强求解器通过、弱求解器失败，精准锚定目标难度区间
- 输出完整可执行任务：包含任务指令、Docker运行环境、验证测试用例，可直接用于SFT轨迹蒸馏
### 关键结果
共生成5431个校准后的终端任务，在Qwen3-30B和Qwen3.5-35B上SFT后，Terminal-Bench 2.0准确率分别达32.58%、47.57%，较基线最高提升24.71个百分点；OOD场景下SWE-bench Pro解决率提升27.68个百分点，Doc2Repo通过率提升30.04个百分点；消融实验显示对比校准比单求解器反馈多带来6.75个百分点的准确率提升。
### 核心结论
训练数据的价值核心不在于数量，而在于是否落在目标模型的可学习区，基于求解行为的校准能大幅提升数据的训练效率和迁移性
