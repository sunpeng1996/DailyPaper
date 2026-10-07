---
title: 'Aligning Performance with Contribution: Towards Contribution-Aware Fair Recommendation'
title_zh: 贡献感知公平推荐：实现用户贡献与推荐性能对齐
authors:
- Shuai Zhang
- Hui Fang
- Zun Sun
affiliations:
- Shanghai University of Finance and Economics
- Singapore University of Technology and Design
arxiv_id: '2610.08245'
url: https://arxiv.org/abs/2610.08245
pdf_url: https://arxiv.org/pdf/2610.08245
published: '2026-10-06'
collected: '2026-10-07'
category: RecSys
direction: 公平推荐 · 用户贡献-性能对齐
tags:
- Fairness
- RecommenderSystem
- MultiObjectiveOptimization
- UserModeling
- IncentiveMechanism
one_liner: 定义贡献-性能公平范式，推出模型无关CPFR框架，兼顾推荐精度与贡献对齐公平性
practical_value: '- 可复用三维用户贡献评估特征：交互量、训练损失对齐度、梯度强度，无需额外数据即可量化用户对模型的价值，可直接用于用户分层运营、高价值用户权益倾斜等业务场景

  - 双正则化多目标优化设计可直接迁移：跨组单调约束+组内方差约束的损失设计，配合MoCo优化器解决梯度冲突，能平滑控制公平性与精度的trade-off

  - 用户分层可采用Jenks Natural Breaks方法，相比等宽分箱、K-means更稳定，能最大化组间差异最小化组内差异，适合所有用户分层类优化场景

  - 业务可通过调整λ1、λ2超参数灵活适配运营需求：侧重高价值用户体验调大λ2，侧重同贡献用户公平调大λ1，无需重构训练流程'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐公平性研究多围绕敏感属性平等，未考虑用户作为数据贡献者的异质性，高贡献用户（提供高质量交互数据）的推荐收益未被倾斜，会打击用户长期参与意愿，损害推荐生态的健康度，因此需要建立贡献与推荐性能对齐的公平机制。

### 方法关键点
- 贡献-性能公平定义包含两大核心准则：跨组单调（贡献越高的用户组平均推荐性能不低于低贡献组）、组内公平（同贡献层级用户性能差异最小）
- 三维用户贡献量化逻辑：融合交互量、训练损失对齐度（负平均训练损失）、优化强度（平均梯度范数）三个归一化信号，加权得到用户贡献得分
- 训练流程设计：用Jenks自然断点法将用户划分为有序贡献组，设计LUIF（组内损失差正则）、LUGF（跨组损失逆序惩罚）两个可微正则项，与推荐损失联合优化，采用MoCo多目标优化器解决梯度冲突

### 关键实验结果
在MovieLens-100K、MovieLens-1M、Amazon Office三个公开数据集上，基于NCF、DCN、DeepFM三个骨干模型对比Vanilla、AFRL、CUGF、FairNS四个基线，CPFR在90%以上配置下综合质量Q最优，保留90%以上的基准精度，UGF（跨组对齐度）相对基线最高提升30%以上，UIF（组内差异）无明显劣化。

贡献对齐的公平性不仅不会大幅损失精度，还能通过激励用户提供更多高质量交互，长期提升整个推荐系统的性能。
