---
title: 'Modular TTT: Rethinking Test-Time Training as Composable Modules'
title_zh: Modular TTT：将测试时训练重构为可组合模块的统一框架
authors:
- Bohao Tang
- Zhen Qin
- Yuqi Pan
- Zheng Li
- Pengfei Liu
- Ya Zhang
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- ByteDance Seed
arxiv_id: '2608.07110'
url: https://arxiv.org/abs/2608.07110
pdf_url: https://arxiv.org/pdf/2608.07110
published: '2026-08-06'
collected: '2026-08-10'
category: Training
direction: 测试时训练 · 模块化框架与设计空间消融
tags:
- Test-Time Training
- Modular Framework
- Sequence Modeling
- Fast Weights
- Long Context
one_liner: 将测试时训练（TTT）拆解为可组合模块，自动生成计算逻辑，系统消融得到最优配置性能对标GDN
practical_value: '- 长上下文场景（用户行为序列召回、长会话Agent记忆）落地TTT时，可直接复用验证有效的最优配置：小学习率初始化（1e-3）、标量衰减、单层SiLU激活，不要用深层快权重网络和归一化，兼顾效果与算力效率

  - 工程实现TTT时可参考三阶段（训练视图前向/反向、查询视图前向）抽象，用自定义算子替换自动微分路径，可获得2.2x~3.3x的训练吞吐量提升，降低大模型训练成本

  - 实时在线推荐场景可借鉴TTT快权重更新思路，将用户实时行为作为在线训练信号，用模块化TTT快速迭代不同的在线更新规则，无需每次手写全链路梯度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有测试时训练（TTT）变体均为硬编码实现，修改单个组件往往需要重写全链路前向/反向逻辑，无法隔离不同模块的贡献，导致TTT设计空间极不清晰，算法迭代和落地成本居高不下。
### 方法关键点
- 将TTT内部学习器抽象为有向无环图（DAG），把快权重网络、损失函数、学习率、权重衰减、归一化拆分为独立可配置的模块化组件
- 为每个基础原语注册三类规则：训练视图前向、训练视图反向、因果查询视图前向，框架自动组合生成完整的TTT计算图与快权重状态转移逻辑，无需手动推导全局更新规则
- 内置优化的自定义算子，替换自动微分路径，大幅提升训练效率
### 关键实验
- 在100B规模英文预训练语料上训练160M/410M/1.45B三类规模模型，对比基线包括LLaMA、GDN、LaCT等主流序列模型
- 系统消融得到最优配置：小学习率初始化（1e-3）、标量衰减、单层SiLU激活、MSE/内积损失，410M规模下验证损失比默认配置低0.287
- 工程效率比官方TTT实现提升2.2x~3.3x，1.45B规模最优变体下游多选择任务平均准确率达56.44%，仅比GDN低0.14%，性能基本持平
### 核心结论
浅层TTT搭配经过验证的轻量化优化，效果远好于复杂的深层TTT结构，模块化抽象是快速探索算法设计空间的核心手段
