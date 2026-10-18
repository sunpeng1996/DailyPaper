---
title: Can World and Action Modeling Benefit Each Other under Unified Causal Training?
title_zh: 统一因果训练下世界建模与动作建模的互惠性验证研究
authors:
- Yue Su
- Bokai Lin
- Xinkai Wang
- Chubin Zhang
- Xiangnan Wu
- Kuan Zhang
- Weiyang Jin
- Jiwen Yu
- Yiming Li
- Cewu Lu
affiliations:
- MMLab@HKU
- MVIG@SJTU
- THU
- SII
- UCAS
arxiv_id: '2610.21095'
url: https://arxiv.org/abs/2610.21095
pdf_url: https://arxiv.org/pdf/2610.21095
published: '2026-10-14'
collected: '2026-10-18'
category: Agent
direction: 具身Agent · 世界与动作建模统一训练
tags:
- Agent
- World Model
- Causal Training
- Policy Learning
- Embodied AI
one_liner: 提出OneWM统一因果训练框架，验证世界与动作建模的双向互惠增益
practical_value: '- 多任务联合训练可复用双向增益思路：将用户行为（对应动作）、场景状态（对应世界）两类任务放在共享架构下训练，同时提升两类任务性能

  - Agent导购/客服决策系统可引入场景预测分支作为辅助loss：通过预测用户动作带来的场景变化，提升策略泛化性，适配业务场景迭代

  - 统一架构设计可降低多任务部署成本：共享底层特征表示，无需为状态预测、动作生成独立搭建模型，减少推理资源消耗'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
世界建模（预测动作对环境的影响）与动作建模（生成适配目标的策略）相关性强，但二者在统一因果训练下的双向增益关系未被明确验证，现有两类任务通常独立训练，性能与泛化性存在天花板。
### 方法关键点
提出OneWM轻量统一因果训练框架，共享视频-动作底层架构，将动作同时作为两类任务的核心信号：
1. 世界建模分支以指定动作为条件，预测未来多视角视觉观测
2. 动作建模分支以目标为输入生成动作序列，两类任务共享梯度联合更新
### 关键结果
在LIBERO、LIBERO-Plus、RoboCasa365等具身测试集及真实场景策略实验中：
1. 引入动作条件的世界建模辅助任务，可显著提升策略性能与跨场景泛化能力
2. 动作建模分支的训练反过来可提升同架构下多视角世界预测的保真度，双向增益均得到验证
