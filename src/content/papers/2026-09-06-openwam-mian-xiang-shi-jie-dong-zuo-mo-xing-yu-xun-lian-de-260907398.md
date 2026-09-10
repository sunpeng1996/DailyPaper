---
title: 'OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model
  Pretraining'
title_zh: OpenWAM：面向世界动作模型预训练的开源模块化研究框架
authors:
- Yuran Wang
- Siqiao Huang
- Mingleyang Li
- Chenhao Zhang
- Jiaqi Liang
- Weiyang Jin
- Yue Chen
- Xuemin Chi
- Donghao Zhou
- Qize Yu
affiliations:
- National University of Singapore
- Tsinghua University
- Peking University
- The University of Hong Kong
- Zhejiang University
arxiv_id: '2609.07398'
url: https://arxiv.org/abs/2609.07398
pdf_url: https://arxiv.org/pdf/2609.07398
published: '2026-09-06'
collected: '2026-09-10'
category: Agent
direction: 具身Agent · 世界动作模型预训练
tags:
- World Model
- Embodied Agent
- Modular Framework
- Pretraining
- OOD Generalization
one_liner: 开源模块化世界动作模型预训练栈，拆解设计空间提炼优化原则，实现跨仿真到真实机器人的优异泛化性能
practical_value: '- 模块化拆解系统设计空间的思路可复用：落地LLM4Rec、Agent推荐系统时可将生成主干、特征表征、信息流等模块解耦，通过对照实验快速定位最优设计，避免黑盒迭代低效问题

  - 跨域预训练协同优化结论可借鉴：推荐场景跨品类/跨域预训练时，可采用显式跨模块信息流+同步联合去噪设计，大幅提升OOD泛化能力的同时最小化ID精度损失

  - 多源数据混合训练配方可复用：融合公共行为数据+业务私有数据做预训练时，可参考70%任务域数据+30%泛化域数据的配比，兼顾业务精度和泛化性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有World-Action Model(WAM)为紧耦合架构，生成主干、视觉表征、信息流、训练流程等模块深度绑定，无法量化不同设计选择的实际收益，难以开展系统性优化。
### 方法关键点
1. 开源OpenWAM研究栈，将WAM设计空间拆解为可组合模块，统一训练、推理、部署、评估接口，支持可控实验
2. 通过对照实验提炼3条核心设计原则：上游知识迁移需要能力足够的生成主干+紧凑高信息密度隐空间；世界-动作协同需要专属动作容量、显式世界到动作信息流、同步联合去噪；具身预训练核心提升OOD泛化，单阶段联合训练第一人称与机器人数据可兼顾世界覆盖度与动作grounding
3. 基于以上原则构建OpenWAM-α，采用6400小时第一人称人类+机器人数据预训练
### 关键结果
在8个仿真基准+真实机器人实验（覆盖单臂/双臂/灵巧手）上性能排名前列，OOD泛化相对提升12.12pp，ID精度仅损失0.68pp，实现从仿真到真实世界的性能对齐。
